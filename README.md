## How to set up a local dev environment with Docker-Compose

Install Docker Desktop https://docs.docker.com/docker-for-mac/install/

Docker-Compose comes pre-installed with Docker Desktop for MacOS

Copy docker/shell.env.template to docker/shell.env and copy docker/mariadb.env.template to docker/mariadb.env

Open each of the new files ending in .env and enter the secret values. These files are not kept in version control, so changes to them should not leave your computer.

From the deliverability-analysis-tools root directory create the docker-compose environment:
```
docker-compose up -d
```

See if both containers are running:
```
docker-compose ps
```
which should return something like:
```
 Name               Command             State           Ports
----------------------------------------------------------------------
mariadb   docker-entrypoint.sh mysqld   Up      0.0.0.0:3306->3306/tcp
shell     /bin/bash -c sleep infinity   Up
```

You can also use regular docker commands like:
```
docker container ps
```

The deliverability-analysis-tools directory is connected as a volume
to the /dat directory in the `shell` container, so any changes to that
directory on your local machine should immediately take effect in the
docker container.

## Populate the local database from production
You will need to have kubectl installed and have proper RBAC permissions.

This is a useful alias for interacting with the deliverability-analysis-tools namespace in Kubernetes:
```
alias kgd="kubectl --context=global --namespace=deliverability-analysis-tools"
```

Find the MariaDB pod:
```
kgd get po -l role=mariadb
```

Exec into that pod:
```
kgd exec -it [name of mariadb pod] bash
```

From inside the pod, make a copy of the deliv-anal-tools database, entering the MariaDB root password when prompted:
```
mysqldump --compress --single-transaction --max_allowed_packet=16MB --quick --skip-lock-tables --skip-add-locks --skip-triggers --complete-insert --skip-disable-keys deliv-anal-tools -uroot -p > /tmp/deliv-anal-tools.sql
```

Back on your local computer, you can copy the file just created out of the MariaDB pod and into your local mariadb_data directory that is mounted to your local MariaDB docker container:
```
kgd cp [name of mariadb pod]:/tmp/deliv-anal-tools.sql ~/dev/deliverability-analysis-tools/mariadb_data/deliv-anal-tools.sql
```

Exec into your MariaDB Docker container:
```
docker exec -it [name of mariadb docker container on local] bash
```

Inside the MariaDB container, create the database if it doesn't already exist:
```
mysqladmin -uroot -ppassword create deliv-anal-tools
```

Also inside the MariaDB container, Load the database dump into the MariaDB container:
```
mysql -u[user] -p[password] deliv-anal-tools < /var/lib/mysql/deliv-anal-tools.sql
```

Your local dev environment should now essentially mirror the current production environment and database state.

## Useful Kubernetes commands
List all pods in the deliverability-analysis-tools namespace:
```
kgd get pods
```

List all services:
```
kgd get svc
```

List all cronjobs:
```
kgd get cronjob
```

List all jobs:
```
kgd get job
```

Exec into the shell pod:
```
kgd exec -it [name of shell pod] bash
```

Exec into MariaDB shell on MariaDB pod:
```
kgd exec -it [name of mariadb pod] mysql -u[username] -p
```

Delete the shell pod:
```
kgd delete pod [name of shell pod]
```

Get logs from the shell pod:
```
kgd logs [name of shell pod]
```

Port-forward to the MariaDB pod (to be able to connect MySQL Client on local machine):
```
kgd port-forward svc/mariadb 3306:3306
```

Once the port-forward is set up, you can open a new connection in a MySQL client GUI to 127.0.0.1:3306 with your username and password for deliv-anal-tools database. You can also change the first number in the port-forward command to any open port on your local computer.

### Step by step process for setting up from beginning to end:

#### 1: download/clone the kube-access directory, run `git pull origin master` and then run `./ez.pz` within that directory

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1a: when the command prompt asks which gcloud project to use, select `sharpspring
-us`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`NOTE` the kube-access repo has a link for installing gcloud manually if you have
 issues
 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1b: run the following command within the `kube-access` directory `./populate-gke
-cluster-config`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1c: You should now be able to run the following command in terminal 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`kubectl --context global -n deliverability-analysis-tools get po`

#### 2: Add the following to your bash profile (could be found within .bashrc, .bash_profile, etc.) - This will allow the `kgd` prefix in the following commands to work
```
alias kgd="kubectl --context=global --namespace=deliverability-analysis-tools"
```
#### 3: Install Docker Desktop https://docs.docker.com/docker-for-mac/install/

#### 4: Copy docker/shell.env.template to docker/shell.env and copy docker/mariadb.env.template to docker/mariadb.env

#### 5: Open each of the new files ending in .env and enter secret values. 

These files are not kept in version control, so changes to them should not leave your computer (you'll notice that if
 using Pycharm, the files will be colored differently than the rest within the project, as there is a `.gitignore` rule.
  
#### 6: Copying the database from production

You will need to have kubectl installed and have proper RBAC permissions (RBAC permissions should have been set up by systems).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6a: Find the MariaDB pod:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`kgd get po -l role=mariadb`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6b: Exec into that pod

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`kgd exec -it [name of shell pod] bash`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6c: From inside the pod, make a copy of the deliv-anal-tools database, entering the MariaDB root password when prompted:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```mysqldump --compress --single-transaction --max_allowed_packet=16MB --quick --skip-lock-tables --skip-add-locks --skip-triggers --complete-insert --skip-disable-keys deliv-anal-tools -uroot -p > /tmp/deliv-anal-tools.sql```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6d: Back on your local computer, you can copy the file just created out of the
 MariaDB pod and into your local mariadb_data directory that you will then use later and mount it to your local
  docker container
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`kgd cp [name of mariadb pod]:/tmp/deliv-anal-tools.sql ~/dev/deliverability-analysis-tools/mariadb_data/deliv-anal-tools.sql`
  
#### 7: Creating the Docker Container

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7a: From the deliverability-analysis-tools root directory create the docker-compose environment: 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`docker-compose up -d`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7b: See if the containers are up and running 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`docker-compose ps`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7b: Exec into your MariaDB Docker container:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `docker exec -it [name of mariadb docker container on local] bash`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7c: Inside the MariaDB container, create the database if it doesn't already exist:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `mysqladmin -uroot -ppassword create deliv-anal-tools` 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7d: Load the database dump into the MariaDB container:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `mysql -u[user] -p[password] deliv-anal-tools < /var/lib/mysql/deliv-anal-tools.sql`

After all this, you should be able to utilize all of the above tooltips 
and various commands to set things up the way you need them.

<hr></hr>
<br>

## Setting up ECFG and Installing Secrets

This process details including new secret keys into the DAT repo/namespace to allow 
our scripts to securely use passwords from various services
<br>

### Installing ECFG


1. Choosing a place for a new repo, clone the following:
    ```
    git clone https://github.com/Santiclause/ecfg.git
    ```


2. Install Go, if not already done.
    ```
    brew install go
    ```


3. CD inside of the root ecfg folder that was cloned and run the following:
    ```
    go install ./cmd/ecfg
    ```


4. Edit your bash/zsh profile to include an alias for ecfg

    zsh: `nano ~/.zprofile` or `nano ~/.zshrc`
    ```
    alias ecfg="/Users/'$LOGNAME'/go/bin/ecfg"
    ```

    bash: `nano ~/.bash_profile` or `nano ~/.bashrc`
    ```
    alias ecfg="/Users/'$LOGNAME'/go/bin/ecfg"
    ```


5. Reload your Terminal either be restarting it or running the following commands.

    zsh: `source ~/.zprofile` or `source ~/.zshrc`

    bash: `source ~/.bash_profile` or `source ~/.bashrc`


6. Confirm ecfg works by running the command `ecfg`. You should see the following if successfully installed:
    ```
    “No entry for ecfg in section 1 of the manual”
    ```
<hr></hr>    
<br>

### Creating a New Secret


Assuming `Installing ECFG` was completed, this will walk you through creating a new secret

1. Create a new JSON file anywhere on your computer, 
preferably somewhere nearby your working github directories 
and make sure it contains the following.

    ```
    {
      "_public_key": "",
      "data2encrypt": ""
    }
    ```

    1a. `_public_key` holds the public key value. (Can be copied from secrets.ecfg.yaml in the DAT repo)

    1b. `data2encrypt` can be named anything. The assigned value would be the plain-text password/data you are wanting to encrypt.


2. CD to the directory where this file was saved.


3. Run `ecfg encrypt fileNameChosen.json`

    3a. If successful you should see something like: `Wrote 233 bytes to secret.json.`


4. Open the JSON file again and confirm you see the plain-text secret is now an encrypted secret.


5. Add this secret as a new line in `secrets.ecfg.yaml`. 
Whatever you decide to name the secret here is what the environment variable will be called.
    
    example:

    ```
    secrets:
      deliverability-analysis-tools-secrets:
        data:
          some_new_secret: "the long encrypted secret value"
          another_secret: "another encrypted value"
    ```

    There are two environment variables here called "some_new_secret" and "another_secret"


6. Add the same entry that you added to `secrets.ecfg.yaml` to your docker `docker/shell.env` file, but make sure the secret is UNENCRYPTED.

    Both files are shown below to give a better idea of the alignment.

    example `shell.env`:

    ```
    # Environment variables for shell docker-compose service:
    #
    # This host name is defined in docker-compose.yaml and necessary for networking

    SOME_NEW_SECRET=totallyUnencryptedPassword
    ANOTHER_SECRET=anotherUnencryptedPassword
    ```

    example `secrets.ecfg.yaml`:

    ```
    secrets:
      deliverability-analysis-tools-secrets:
        data:
          some_new_secret: "the long encrypted secret value"
          another_secret: "another encrypted value"
    ```

7. Push the updates `secrets.ecfg.yaml` to the DAT Repo and Merge

<hr></hr>
<br>

### Confirming The Secret Was Created Properly


1. Find the kgd shell pod: `kgd get po`

2. Exec into the kgd shell pod: `kgd exec -it nameOfShellPodCopied bash`

3. Run `env` inside the kgd shell pod
    
4. Confirm you see the newly added secret in the list that prints out after typing env
    - You should see this as being decrypted which is expected!

<br>

#### Concerning Docker/Local Secrets:

For Docker, you need to restart your container by doing docker compose up -d before the environment variable will work in local testing.

You can similarly docker exec -it shell bash and run env there too and see if you can see the environment variable that was added to shell.env.






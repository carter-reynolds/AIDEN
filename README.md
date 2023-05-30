<H1>AIDEN : <i>Artificial Intelligence Data ENgine</i></h1>

<sub><i><b>Current Model:</b> `GPT-Turbo-3.5`</i></sub>
<br>
<sub><i><b>Python Version:</b> `Python 3.7`</i></sub>
<br>
<br>

<p>AIDEN is a WIP python Chat GPT implementation. Being built using the `openAI` Python library. The name was coined after asking AIDEN what it would be called when given a list of functionalities, mocking something similar to JARVIS from Iron Man. I liked it and decided to keep it.</p>

<p>AIDEN serves mainly as an assistant just like normal Chat GPT, but eventually AIDEN will be able to fire of functions within his code simply by being told to do so, AKA saving a file, saving code examples to files, sending texts, etc. </p>

<h3>Running AIDEN </h3>
<ol>
  <li>Clone the repo </li>
  <li>Ensure Docker is installed </li>
  <li><code>cd AIDEN/docker</code> </li>
  <li><code>cp shell.env.template shell.env</code></li>
  <li>Inside of the newly copied <code>shell.env</code>, paste your OpenAI API key after <code>AIDENKEY=</code>, and save.</li>
  <li><code>cd ../</code></li>
  <li><code>docker compose up -d </code></li>
  <li><code>docker exec -it aiden_shell bash</code></li>
  <li><code>python3 main.py text </code></li>
</ol>

<p>
  <br>
  <b>Important Note on GPT-3.5-Turbo and what AIDEN is/isn't made for:</b>
  <br>
  <br>
  <i>Eventually, once AIDEN has the Chat GPT-4 model being served, he'll be able to do even more complex things like search the internet and will likely need far less context in order to perform an action he is asked. For now it's mainly here for testing and preperation for GPT-4. 
    
For example, while AIDEN can indeed keep time and give you accurate time if asked, this only works because we are manually telling him what time it is every message essentially. This type of logic has to be applied to other things AIDEN should/can do. 
    
<b>I am still experimenting actively with this behavior!</b>
    
GPT-3.5-Turbo is a powerful model but it still lacks actual connection to the internet, image processing, and true automated link viewing. Some of this functionality can be coded in, such as pulling all the headers from a website, and passing them to AIDEN to analyze and telling him it is website headers, but results can still be varied as it relies heavily on how you're telling AIDEN about the headers.
    
While you can sometimes get Chat GPT to do things it won't normally do by telling it to "imagine" or "simulate", I have very few uses here where I believe that to be necessary. Also again, it was incredibly unreliable if it was actually working or we were just bamboozling ourselves into thinking it worked. GPT-4 should allow for better system prompting that should hopefully remove the need to "trick" Chat GPT into thinking it's AIDEN to give better responses.
    
Right now, there is no 'jailbreaking' being done with AIDEN. As far as I can tell, there are no currently GPT jailbreak prompts that still <b>consistently</b> work, and AIDEN seems to stay in character if you actually don't actively try to trick him into breaking OpenAI policy. There isn't anything I plan on doing with AIDEN that would require this anyways.
</i>
</p>

<br>


<h2>AIDEN File Structure:</h2>
<p>AIDEN was recently rewritten in a Class-like structure. He may be rewritten again as functionality/core code changes.</p>
<ul>
  <li><b>Main Excutable:</b></li>
  <ul>
    <li><code>main.py</code> - runs everything</li>
  </ul>
  <li><b>AIDEN core class:</b></li>
  <ul>
    <li><code>classes/aiden/system.py</code> - All the code for AIDEN and Chat GPT connectivity/functionality. You can change AIDEN's name by changing the value of <code>self.name</code>, but there may still be some hardcoded stuff in the rules file referencing AIDEN.</li>
  </ul>
  <li><b>AIDEN Rules:</b></li>
  <ul>
    <li><code>classes/rules/master.py</code> - Handles loading the rules from rule_list.py</li>
    <li><code>classes/rules/rule_list.py</code> - Stores any rules in bulk via a list of dictionaries (currently not really being used)</li>
  </ul>
  <li><b>User code:</b></li>
  <ul>
    <li><code>class/user/system.py</code> - User related data, not used for much at the moment. Eventually planned to integrate with SQL and store more user metadata to send to AIDEN 🤷‍♂️</li>
  </ul>
</ul>


<h2>Docker File Structure:</h2>
<p>AIDEN runs within a Docker container, which uses the following files:</p>
<ul>
  <li><b>Docker Enviroment Variables:</b></li>
  <ul>
    <li><code>docker/shell.template.env</code></li>
  </ul>
  <li><b>Docker Compose/Build File:</b></li>
  <ul>
    <li><code>docker-compose.yaml</code></li>
  </ul>
  <li><b>Docker Environment:</b></li>
  <ul>
    <li><code>environment.yaml</code></li>
  </ul>
  <li><b>Docker Config File:</b></li>
  <ul>
    <li><code>Dockerfile</code></li>
  </ul>
</ul>
    
  

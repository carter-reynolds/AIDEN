<b>IMPORTANT REPO NOTE:<br><br>Master branch protection is disabled for some reason even knowing I pay for Github Pro and documentation claims I should have that functionality.<br><br>_Please be mindful on Master and it would be preferred to make a separate branch with a PR if suggesting/making changes or additions!_</b>
<br><br><br><br>
<H1>AIDEN : <i>Artificial Intelligence Data ENgine</i></h1>

<sub><i><b>Current Model:</b> `GPT-Turbo-3.5`</i></sub>
<br>
<sub><i><b>Python Version:</b> `Python 3.7`</i></sub>
<br>
<br>

<p>AIDEN is a WIP python Chat GPT implementation. Being built using the `openAI` Python library. The name was coined after asking AIDEN what it would be called when given a list of functionalities, mocking something similar to JARVIS from Iron Man. I liked it and decided to keep it.</p>

<p>AIDEN serves mainly as an assistant just like normal Chat GPT, but eventually AIDEN will be able to fire of functions within his code simply by being told to do so, AKA saving a file, saving code examples to files, sending texts, etc. </p>

<a href="https://platform.openai.com/docs/api-reference/chat/create?lang=python"><b>AIDEN works using with this Documentation from OpenAI</b></a>

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
    
Example psuedo-code to allow AIDEN to keep track of time:
```python
'''
Assume AIDEN is being told silently at launch that all messages contain a timestamp
in order for AIDEN to keep track of time.
'''
user_input  = input("Message: ") 
system_time = time.now()
user_input  = f"{user_input} | Message Timestamp: {system_time}"
    
# Send the message to AIDEN with timestamp appended to original message
response = AIDEN.communicate('user', user_input)
```
AIDEN then just reviews chat history essentially and uses some built in logic for keeping track of time within the current session. You could then ask AIDEN at any point what time it is or do any time conversions on the current time. You can also ask AIDEN what time it was when the chat started.
    
<b><a href="https://github.com/carter-reynolds/AIDEN/issues/3">I am still experimenting actively with this behavior and could use additional ideas!!!</a></b>
    
While GPT-3.5-Turbo is a powerful model it still lacks actual connection to the internet, image processing, and true automated link viewing. Some of this functionality can be coded in, such as pulling all the headers from a website, and passing them to AIDEN to analyze and telling him it is website headers, but results can still be varied as it relies heavily on how you're telling AIDEN about the headers.
    
While you can sometimes get Chat GPT to do things it won't normally do by telling it to "imagine" or "simulate", I have very few uses here where I believe that to be necessary. Also again, it was incredibly unreliable if it was actually working or we were just bamboozling ourselves into thinking it worked. GPT-4 should allow for better system prompting that should hopefully remove the need to "trick" Chat GPT into thinking it's AIDEN to give better responses.
    
Right now, there is no 'jailbreaking' being done with AIDEN. As far as I can tell, there are no current GPT jailbreak prompts that <b>consistently</b> work, and AIDEN seems to stay in character for my testing usages if we don't actively try to trick him into breaking OpenAI policy. There isn't anything I plan on doing with AIDEN that would require this anyways as of now.
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
    
  

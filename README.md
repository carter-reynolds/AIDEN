<H1>AIDEN : <i>Artificial Intelligence Data ENgine</i></h1>

<sub><i><b>Current Model:</b>`GPT-Turbo-3.5`</i></sub>
<br>
<sub><i><b>Python Version:</b>`Python 3.7`</i></sub>
<br>
<br>

<p>AIDEN is a WIP python Chat GPT implementation. Being built using the `openAI` Python library</p>

<p>AIDEN serves mainly as an assistant just like normal Chat GPT, but eventually AIDEN will be able to fire of functions within his code simply by being told to do so, AKA saving a file, saving code examples to files, sending texts, etc. </p>

<p>Also there are plans to eventually have 2 versions of AIDEN set up, one acting in the role of another AIDEN model or the user itself, and have it communicate back and forth with the original instance of AIDEN. </p>

<h3>Running AIDEN </h3>
<ol>
  <li>Clone the repo </li>
  <li>Ensure Docker is installed </li>
  <li><code>cd AIDEN/docker</code> </li>
  <li><code>cp shell.env.template shell.env</code></li>
  <li>Paste your OpenAI API key after <code>AIDENKEY=</code></li>
  <li><code>cd ../</code></li>
  <li><code>docker compose up -d </code></li>
  <li><code>docker exec -it aiden_shell bash</code></li>
  <li><code>python3 main.py text </code></li>
</ol>
<hr></hr>
<p>
  <br>
  <b>Important Note on GPT-3.5:</b>
  <br>
  <br>
  <i>
    Eventually, once AIDEN has the Chat GPT-4 model, we'll be able to do even more complex things with AIDEN like search the internet, but for now it's mainly here for testing and       preperation. He can keep time since we send a timestamp at the start of chat and with every user message. Right now, there is no 'jailbreaking' being done with AIDEN
  </i>
</p>
<hr>
<h2>File Structure:</h2>
<p>AIDEN was recently rewritten in a Class-like structure. He may be rewritten again as functionality/core code changes.</p>
<ul>
  <li><b>Main Excutable:</b></li>
  <ul>
    <li><code>main.py</code> - runs everything</li>
  </ul>
  <li><b>AIDEN core class:</b></li>
  <ul>
    <li><code>classes/aiden/system.py</code></li>
  </ul>
  <li><b>AIDEN Rules:</b></li>
  <ul>
    <li><code>classes/rules/master.py</code> - Handles loading the rules from rule_list.py</li>
    <li><code>classes/rules/rule_list.py</code> - Stores any rules in bulk via a list of dictionaries (currently not really being used)</li>
  </ul>
  <li><b>User code:</b></li>
  <ul>
    <li><code>class/user/system.py</code></li>
  </ul>
</ul>
    
  

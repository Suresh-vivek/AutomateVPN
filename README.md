# AutomateVPN

## What is VPN ?
VPN stands for **Virtual Private Network** , it is a technology that creates a safe and encrypted connectionover a less secure network, such as **Internet**.
Basically it connects you to a remote server(another country) by changing your **IP Address**
and it use tunneling protocols to establish a secure connection.

## How to Setup VPN ?

Here we are using Windscribe VPN

**Step 1:** Create a free account on Windscribe.Visit <a href="https://windscribe.com/">Windscibe</a> and register yourself.

**Step 2:** Open your Terminal and add the windscribe signing key to apt using following command.

<pre><code>
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key FDC247B7
</pre> </code>


**Step 3:** Add the repository to your source.list using following command

<pre><code>
echo 'deb https://repo.windscribe.com/ubuntu bionic main' | sudo tee /etc/apt/sources.list.d/windscribe-repo.list
</pre></code>


**Step 4:** Update your system packages

<pre><code>
sudo apt-get update
</pre></code>

**Step 5:** Install windscribe-cli using following command.

<pre><code>
sudo apt-get install windscribe-cli
</pre></code>

**Step 6:** Login to windscribe with your credentials used in Step 1 while creating account on Windscribe.

<pre><code>
windscribe login
</pre></code>

## Working with VPN using Windscribe

**1.** To check status of VPN

<pre><code>
windscribe status
</pre></code>

it will show either you are connected to VPN or not


**2.** To connect to windscribe

<pre><code>
windscribe connect
</pre></code>

it will change your IP Address and connects you to a different server


**3.**To disconnect from windscribe

<pre><code>
windscribe disconnect
</pre></code>

**4.** To print VPN services Locations 

<pre><code>
windscribe locations
</pre></code>

**5.** To connect to a specific Server

<pre><code>
windscribe connect <short Name>
</pre></code>

**6.** To logout from windscribe

<pre><code>
windscribe logout
</pre></code>


## Steps to Automate VPN using Python

**Step 1:** Open the terminal and create a file using gedit by the following command

<pre><code>
gedit AutomateVPN.py
</pre></code>
*Python must be installed in your system*


**Step 2:** Copy code from Automate_VPN.py and save it to AutomateVPN.py

**Step 3:** Close the Terminal , Reopen the terminal and type the following Command

<pre><code>
windscribe login
</pre></code>

<pre><code>
python3 AutomateVPN.py
</pre></code>

This will run the program and it will change your IP Address every 15-20 minutes.

To disconnect VPN
Close the Terminal , Reopen the terminal and type the following Command

<pre><code>
windscribe disconnect
</pre></code>



# AutomateVPN

## What is VPN ?
VPN stands for **Virtual Private Network** , it is a technology that creates a safe and encrypted connectionover a less secure network, such as **Internet**.
Basically it connects you to a remote server(another country) by changing your **IP Address**
and it use tunneling protocols to establish a secure connection.

## How to Setup VPN ?

Here we are using Windscribe VPN

**Step 1:** Create a free account on Windscribe.Visit <a href="https://windscribe.com/">Windscibe</a> and register yourself.

**Step 2:** Open your Terminal and add the windscribe signing key to apt using following command.

'''
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key FDC247B7
'''

**Step 3:** Add the repository to your source.list using following command

'''
echo 'deb https://repo.windscribe.com/ubuntu bionic main' | sudo tee /etc/apt/sources.list.d/windscribe-repo.list
'''

**Step 4:** Update your system packages

'''
sudo apt-get update
'''

**Step 5:** Install windscribe-cli using following command.

'''
sudo apt-get install windscribe-cli
'''

**Step 6:** Login to windscribe with your credentials used in Step 1 while creating account on Windscribe.

'''
windscribe login
'''

## Working with VPN using Windscribe

**1.** To check status of VPN

'''
windscribe status
'''
it will show either you are connected to VPN or not

**2.** To connect to windscribe

'''
windscribe connect
'''
it will change your IP Address and connects you to a different server

**3.**To disconnect from windscribe

'''
windscribe disconnect
'''

**4.** To print VPN services Locations 

'''
windscribe locations
'''

**5.** To connect to a specific Server

'''
windscribe connect <short Name>
'''

**6.** To logout from windscribe

'''
windscribe logout
'''


## Steps to Automate VPN using Python

**Step 1:** Open the terminal and create a file using gedit by the following command

'''
gedit AutomateVPN.py
'''
*Python must be installed in your system*

**Step 2:** Copy code from Automate_VPN.py and save it to AutomateVPN.py

**Step 3:** Close the Terminal , Reopen the terminal and type the following Command

'''
windscribe login
'''

'''
python3 AutomateVPN.py
'''

This will run the program and it will change your IP Address every 15-20 minutes.

To disconnect VPN
Close the Terminal , Reopen the terminal and type the following Command

'''
windscribe disconnect
'''



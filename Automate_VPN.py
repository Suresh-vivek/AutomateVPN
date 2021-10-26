# import required modules
import os 
from time import sleep
import random

# List of VPN server code

codeList = ["TR", "US-C", "US", "US-W" , "CA" , "CA-W", "FR","DE","NL","NO","RO","CH","GB","HK"]

try:
    #connect to VPN
    os.system("windscribe connect")
    while True:
        # assigning a random VPN server code
        choicecode = random.choice(codeList)

        # Changing IP address after a particular Time-period
        sleep(random.randrange(120,300))

        #connecting to a different VPN server
        print("!!!  Changing the IP address.......")
        os.system("windscribe connect "+ choicecode)

except:
    # disconnect VPN
    os.system("windscribe disconnect")
    print("Sorry , some error has occured.....")
    
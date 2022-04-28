import os
import json
from client import clientChat
try:

    os.system('sudo apt-get install python3')
    os.system('sudo apt-get install pip')
    os.system('sudo pip3 install colorama')
    os.system('sudo pip3 install sucket')
    os.system('sudo pip3 install threading')
    os.system('sudo chmod +x client.py')
    os.system('sudo chmod +x server.py')
except Exception as e:
    print(e)


from colorama import Fore, init
init()

fblue = Fore.BLUE
fred = Fore.RED
fgreen = Fore.GREEN
fpurple = Fore.MAGENTA
freset = Fore.RESET

print(fpurple, """ █████╗  ██████╗ ██████╗
██╔══██╗██╔════╝██╔════╝
███████║██║     ██║     
██╔══██║██║     ██║     
██║  ██║╚██████╗╚██████╗
╚═╝  ╚═╝ ╚═════╝ ╚═════╝           
version: 1.0
by: l3nn1x\n\n\n""", freset)
cliCon = {}

with open('clientConf.json', 'r') as f:
    cliCon = json.load(f)
clientChat(host=cliCon['server-host'], port=cliCon['server-port'])

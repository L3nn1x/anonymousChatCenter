import time
import json
from client import clientChat
from server import serverChat
import socket
import os
hostname = socket.gethostname()

from colorama import Fore, init
init()


fblue = Fore.LIGHTBLUE_EX
fred = Fore.RED
fgreen = Fore.GREEN
fpurple = Fore.MAGENTA
freset = Fore.RESET

numoptions = ['1', '2', '3', '4', '5', '6', '7']
stroptions = ['set_IP', 'set_PORT', 'set_server_IP', 'set_server_PORT', 'run_client.py', 'run_server.py', 'quit']
options = {}
for index in range(len(numoptions)):
    options[numoptions[index]] = stroptions[index]
def selectOptions(select=str):
    options = {}
    for index in range(len(numoptions)):
        options[numoptions[index]] = stroptions[index]

    if select.isdigit():
        if options[select] == 'run_server.py' or options[select] == 'run_client.py' or options[select] == 'quit':
            return [select]


        else:
            selection = input(options[select]+': ')
            return [select, selection]
    else:
        print('\n [*] please make an selection\n')


def makeAction(command=list):
    updateValue = {}

    if options[command[0]] == stroptions[0]: # client IP configuration
        with open('clientConf.json', 'r') as f:
            updateValue = json.load(f)
            updateValue['client-host'] = command[1]
        with open('clientConf.json', 'w') as f:
            json.dump(updateValue, f)
    elif options[command[0]] == stroptions[1]: # client PORT configuration
        with open('clientConf.json', 'r') as f:
            updateValue = json.load(f)
            updateValue['client-port'] = int(command[1])
        with open('clientConf.json', 'w') as f:
            json.dump(updateValue, f)

    elif options[command[0]] == stroptions[2]: # server IP configuration
        with open('serverConf.json', 'r') as f:
            updateValue = json.load(f)
            updateValue['server-host'] = command[1]
        with open('serverConf.json', 'w') as f:
            json.dump(updateValue, f)
    elif options[command[0]] == stroptions[3]: # server PORT configuration
        with open('serverConf.json', 'r') as f:
            updateValue = json.load(f)
            updateValue['server-port'] = command[1]
        with open('serverConf.json', 'w') as f:
            json.dump(updateValue, f)







logo = """\t\t █████╗  ██████╗ ██████╗
\t\t██╔══██╗██╔════╝██╔════╝
\t\t███████║██║     ██║     
\t\t██╔══██║██║     ██║     
\t\t██║  ██║╚██████╗╚██████╗
\t\t╚═╝  ╚═╝ ╚═════╝ ╚═════╝  """

print(fpurple, logo, fred,"""         
\t\tversion: 1.0
\t\tby: l3nn1x\n\n\n""", freset)
cliCon = {}

for index in range(len(numoptions)):
    print(fgreen, f'\t\t::[{numoptions[index]}]::', freset, fblue, stroptions[index], freset, '\n')

while True:
try:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    print(fpurple, logo, fred, """         
    \t\tversion: 1.0
    \t\tby: l3nn1x\n\n\n""", freset)

    for index in range(len(numoptions)):
        print(fgreen, f'\t\t::[{numoptions[index]}]::', freset, fblue, stroptions[index], freset, '\n')


    user = input(f'\n::[{hostname}]:: make a selection: ',)


    if options[user] == 'quit':
        break
    if options[user] == 'run_server.py':
        with open('serverConf.json', 'r') as f:
            serCon = json.load(f)
            serverChat(host=serCon['server-host'], port=serCon['server-port'])

    elif options[user] == stroptions[4]:  # run client.py
        with open('clientConf.json', 'r') as f:
            config = json.load(f)
            clientChat(host=config['client-host'], port=config['client-port'])

        serverChat()
    selOp = selectOptions(user)
    makeAction(selOp)
except Exception as E:
    print(e)
    time.sleep(3)
    continue
    

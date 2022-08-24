from server import serverChat
from testConnection import test_Connection
import socket
import os
import time
import json
from client import clientChat
hostname = socket.gethostname()

from colorama import Fore, init
init()


fblue = Fore.LIGHTBLUE_EX
fred = Fore.RED
fgreen = Fore.GREEN
fpurple = Fore.MAGENTA
freset = Fore.RESET

numoptions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
stroptions = ['set_IP', 'set_PORT', 'set_server_IP', 'set_server_PORT', 'run_client.py',
              'run_server.py', 'test_configurations', 'show_configurations', 'quit']
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

    #12397
    if options[command[0]] == stroptions[0]: # client IP configuration
        updateValue = {}
        with open('clientConf.json', 'r') as f:
            updateValue = json.load(f)
            updateValue['client-host'] = command[1]
        with open('clientConf.json', 'w') as f:
            json.dump(updateValue, f)
    elif options[command[0]] == stroptions[1]: # client PORT configuration
        updateValue = {}
        with open('clientConf.json', 'r') as f:
            updateValue = json.load(f)
            updateValue['client-port'] = int(command[1])
        with open('clientConf.json', 'w') as f:
            json.dump(updateValue, f)

    elif options[command[0]] == stroptions[2]: # server IP configuration
        updateValue = {}
        with open('serverConf.json', 'r') as f:
            updateValue = json.load(f)
            updateValue['server-host'] = command[1]
        with open('serverConf.json', 'w') as f:
            json.dump(updateValue, f)
    elif options[command[0]] == stroptions[3]: # server PORT configuration
        updateValue = {}
        with open('serverConf.json', 'r') as f:
            updateValue = json.load(f)
            updateValue['server-port'] = int(command[1])
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


        if options[user] == stroptions[8]: # THIS IF STATEMENT QUITS THE SYSTEM
            break

        if options[user] == stroptions[6]: # THIS IF STATEMENT TEST THE SERVERS AND THE CLIENT
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            print(fpurple,'[#] testing server connection...', freset)
            server_ = test_Connection('serverConf.json')
            print(fpurple, '[#] testing client connection...', freset)
            client_ = test_Connection('clientConf.json')
            user = input('click any key to continue..')
            continue

        if options[user] == stroptions[7]: # THIS IF STATEMENT SHOWS THE CONFIGURATIONS
            with open('clientConf.json', 'r') as f:
                with open('serverConf.json', 'r') as f2:
                    print(f.read())
                    print(f2.read())
                    user = input('click any key to continue..')
                    continue

        if options[user] == 'run_server.py': # THIS IF STATEMENT RUNS THE SERVER
            with open('serverConf.json', 'r') as f:
                serCon = json.load(f)
                serverChat(host=serCon['server-host'], port=serCon['server-port'])


        elif options[user] == 'run_client.py':  # THIS IF STATEMENT RUNS THE CLIENT
            with open('clientConf.json', 'r') as f:
                config = json.load(f)
                clientChat(host=config['client-host'], port=config['client-port'])



        selOp = selectOptions(user)
        makeAction(selOp)
    except Exception as e:
        print(e)
        time.sleep(3)
        continue

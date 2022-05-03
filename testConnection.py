import json
from colorama import Back, init, Fore
from server import serverChat
from client import clientChat

fred = Fore.RED
fgreen = Fore.GREEN
freset = Fore.RESET
green = Back.GREEN
red = Back.RED
reset = Back.RESET

init()
def test_Connection(file='',):
    """must be a json file"""
    if 'client' in file:
       with open(file, 'r') as f:
            load = json.load(f)
            client_ = clientChat(load['client-host'], load['client-port'], testMode=True)
            if client_ == True:
                print(green, str(load), reset)
                print(fgreen, 'client is connectable!', freset)
            else:
                print(red, str(load), reset)
                print(fred, '[!] client is not connectable.', freset)
    elif 'server' in file:
        with open(file, 'r') as f:
            load = json.load(f)
            server_ = serverChat(host=load['server-host'], port=load['server-port'], testMode=True)
            if server_ == True:
                print(green, str(load), reset)
                print(fgreen, 'server is connectable!', freset)
            else:
                print(red, str(load), reset)
                print(fred, '[!] server is not connectable.', freset)

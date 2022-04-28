import os
try:
    os.system('sudo apt-get install python3')
    os.system('sudo apt-get install pip')
    os.system('sudo pip3 install colorama')
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
                        """, freset)


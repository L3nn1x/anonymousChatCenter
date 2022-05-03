import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init
import os
import time
# init colors
init()

# set the available colors
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX,
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX,
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
]

# choose a random color for the client
client_color = random.choice(colors)


def clientChat(host=str, port=int, testMode=False):
    if testMode == False:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    # server's IP address
    # if the server is not on this machine,
    # put the private (network) IP address (e.g 192.168.1.2)
    SERVER_HOST = host
    SERVER_PORT = port # server
    separator_token = "<SEP>" # we will use this to separate the client name & message

    # initialize TCP socket
    s = socket.socket()

    # connect to the server
    if testMode == True:
        try:
            s.connect((SERVER_HOST, SERVER_PORT))
            return True
        except:
            return False
    if testMode == False:

        print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")

        s.connect((SERVER_HOST, SERVER_PORT))
        sucess = "[+] Connected."

        print(Fore.GREEN, sucess,  Fore.RESET)
        # prompt the client for a name
        name = input("Enter your name: ")

        def listen_for_messages():
            while True:
                message = s.recv(1024).decode()
                print("\n" + message)

        # make a thread that listens for messages to this client & print them
        t = Thread(target=listen_for_messages)
        # make the thread daemon so it ends whenever the main thread ends
        t.daemon = True
        # start the thread
        t.start()
        print(colors[-1], '\n[*] press enter to continue..\n', Fore.RESET)
        while True:

            # input message we want to send to the server
            to_send = input('\nsend txt: ')
            # a way to exit the program
            if to_send.lower() == 'q':
                break
            # add the datetime, name & the color of the sender
            date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            to_send = f"{client_color}[{date_now}] {name}{separator_token}{to_send}{Fore.RESET}"
            # finally, send the message
            s.send(to_send.encode())


        # close the socket
        s.close()

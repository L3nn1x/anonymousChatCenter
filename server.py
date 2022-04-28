import socket
from threading import Thread
from colorama import Fore, init
import json

fblue = Fore.BLUE
fred = Fore.RED
fgreen = Fore.GREEN
fpurple = Fore.MAGENTA
freset = Fore.RESET



init()
def serverChat(host='192.168.1.23', port=5002):
    # server's IP address
    SERVER_HOST = host
    SERVER_PORT = port # port we want to use
    separator_token = "<SEP>" # we will use this to separate the client name & message

    # initialize list/set of all connected client's sockets
    client_sockets = set()
    # create a TCP socket
    s = socket.socket()
    # make the port as reusable port
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # bind the socket to the address we specified
    s.bind((SERVER_HOST, SERVER_PORT))
    # listen for upcoming connections
    s.listen(5)

    while True:
        print('')
        break
    print(fpurple, f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}", freset)

    def listen_for_client(cs):
        """
        This function keep listening for a message from `cs` socket
        Whenever a message is received, broadcast it to all other connected clients
        """
        while True:
            try:
                # keep listening for a message from `cs` socket
                msg = cs.recv(1024).decode()
            except Exception as e:
                # client no longer connected
                # remove it from the set
                print(fred, f"[!] Error: {e}", freset)
                client_sockets.remove(cs)
            else:
                # if we received a message, replace the <SEP>
                # token with ": " for nice printing
                msg = msg.replace(separator_token, ": ")
            # iterate over all connected sockets
            for client_socket in client_sockets:
                # and send the message
                client_socket.send(msg.encode())


    while True:
        # we keep listening for new connections all the time
        client_socket, client_address = s.accept()
        print(fgreen, f"[+] {client_address} connected.", freset)
        # add the new connected client to connected sockets
        client_sockets.add(client_socket)
        # start a new thread that listens for each client's messages
        t = Thread(target=listen_for_client, args=(client_socket,))
        # make the thread daemon so it ends whenever the main thread ends
        t.daemon = True
        # start the thread
        t.start()

    # close client sockets
    for cs in client_sockets:
        cs.close()
    # close server socket
    s.close()
serCon = {}

with open('serverConf.json', 'r') as f:
    serCon = json.load(f)

serverChat(host=serCon['server-host'], port=serCon['server-port'])
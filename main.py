import socket
import sys
import time
import threading
s = socket.socket()


def SendMessage():
    message = input(str(">> "))
    message = message.encode()
    s.send(message)
    print("")


def join():
    host = input(str("Inserisci il nome della stanza del server: "))
    port = 8080
    s.connect((host, port))
    print("Connesso al server")
    while 1:
        incoming_message = s.recv(1024)
        incoming_message = incoming_message.decode()
        print("Server:", incoming_message)
        print("")


def make():

    host = socket.gethostname()
    print("Il nome della stanza è:", host)
    port = 8080
    s.bind((host, port))
    print("")
    print("Server creato con successo")
    print("")
    print("Attendo connessione con altri server..")
    print("")
    s.listen(1)
    conn, addr = s.accept()
    print("Un utente si è connesso al server....")
    print("")
    while 1:
        message = input(str(">> "))
        message = message.encode()
        conn.send(message)
        print("")
        incoming_message = conn.recv(1024)
        incoming_message = incoming_message.decode()
        print("Server:", incoming_message)
        print("")


command = input(str("Cosa vuoi fare? [Join, Create]\n>> "))
if(command == "Join".lower()):
    join()

elif(command == "make".lower()):
    make()

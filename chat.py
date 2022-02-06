
import socket
s = socket.socket()

HasQuitted = False


def Main():

    def join():

        host = input(str("Inserisci il nome della stanza del server: "))
        port = 8080
        s.connect((host, port))
        print("Connesso al server\nAttendi che l'admin della stanza mandi un messaggio.\nPer uscire usa la combinazione ctrl+C")
        try:
            while 1:
                incoming_message = s.recv(1024)
                incoming_message = incoming_message.decode()

                print("Server:", incoming_message)
                if(incoming_message == "exit".lower()):
                    print(
                        "L'host ha quittato dalla stanza, riavvio il programma...")
                    Main()
                print("\nPuoi mandare un messaggio!")

                message = input(str(">> "))
                message = message.encode()
                s.send(message)
                print("Messaggio Mandato\nAttendi che l'admin della stanza risponda...")
                print("")
        except ConnectionAbortedError:
            print(
                "L'host è uscito o c'è un problema di connessione, chiudo il programmma...\n\n")
            return

    def make():
        global HasQuitted
        host = socket.gethostname()
        print("Il nome della stanza è:", host)
        port = 8080
        s.bind((host, port))
        print("")
        print('Server creato con successo\nPer uscire digita "exit"')
        print("")
        print("Attendo connessione con altri server..")
        print("")
        s.listen(1)
        conn, addr = s.accept()
        print("Un utente si è connesso al server....")
        print("")

        while 1:
            try:
                print("\nPuoi mandare un messaggio!")
                message = input(str(">> "))
                if(message == "exit".lower()):
                    print("Ok, chiudo la stanza.")
                    conn.close()
                message = message.encode()
                conn.send(message)
                print("Messaggio Mandato\nAttendi che l'utente sconosciuto risponda...")
                print("")
                incoming_message = conn.recv(1024)
                incoming_message = incoming_message.decode()

                print("Utente Sconosciuto:", incoming_message)
                print("")
            except ConnectionAbortedError:
                print(
                    "L'utente è uscito o c'è un problema di connessione, chiudo il programma\n\n")
                return
    command = input(str("Cosa vuoi fare? [Join, Make,Exit,help]\n>> "))
    if(command == "Join".lower()):
        join()

    elif(command == "make".lower()):
        make()
    elif(command == "exit".lower()):
        print("Ok! Esco Dal Programma...")
        return
    elif(command == "help".lower()):
        print("Descrizione dei Comandi:\nJoin: Ti permette di entrare in una stanza\nMake: Ti fa creare una stanza\nExit: Ti fa uscire dal programma\nHelp: Manda questo messaggio.")
        print("\n\n")
        Main()
    else:
        print("Comando non esistente.")
        Main()


Main()

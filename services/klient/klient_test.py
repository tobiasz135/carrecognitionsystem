import socket,json
from klient import *


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Connect to server and send data
        sock.connect((HOST, PORT))

        # Receive data from the server and shut down
        while True:
            try:
                received = sock.recv(1024)
                if not received:
                    break
            except:
                break
            print("Received: {}".format(received))


    finally:
        sock.close()



# network_access.py

import socket
from config import NETWORK_CONFIG

class NetworkAccess:
    def __init__(self):
        self.ip_address = NETWORK_CONFIG['ip_address']
        self.port = NETWORK_CONFIG['port']

    def create_socket(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Socket successfully created")
        except socket.error as err:
            print("Socket creation failed with error %s" %(err))

        return s

    def bind_socket(self, s):
        try:
            s.bind((self.ip_address, self.port))
            print("Socket binded to %s" %(self.port))
        except socket.error as err:
            print("Socket bind failed with error: %s" %(err))

    def listen_socket(self, s):
        s.listen(5)
        print("Socket is listening")

    def accept_connection(self, s):
        c, addr = s.accept()
        print("Got connection from", addr)

        return c, addr

    def close_socket(self, s):
        s.close()

if __name__ == "__main__":
    network = NetworkAccess()
    s = network.create_socket()
    network.bind_socket(s)
    network.listen_socket(s)
    c, addr = network.accept_connection(s)
    network.close_socket(s)
import socket
import time

DF_UPDATE_RATE = 25
MSG_LEN_MIN = 9
CHUNK_SIZE = 64


class Server():
    def __init__(self, addr: tuple, num_clients: int, operator):
        self.num_clients = num_clients
        self.operator = operator
        self.socket = None
        self.addr = addr
        self.client = None
    
    def init(self):
        print("Starting...")

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(self.addr)
        self.socket.listen(self.num_clients)

        print("Waiting for client...")
        client, addr = self.socket.accept()
        print("Got connection: " + str(addr))
        self.client = client

    def start(self):
        while True:
            data = self.client.recv(CHUNK_SIZE)
            data = data.decode('utf-8')
            if len(data) <= MSG_LEN_MIN:
               continue

            if self.operator.collect(data):
                return

            #time.sleep(5)

if __name__ == '__main__':
    print("Fall Prevention Server Library")
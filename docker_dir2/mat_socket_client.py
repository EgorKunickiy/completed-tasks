import socket
import sys


class Client:
    def __init__(self):
        self.host = '0.0.0.0'
        self.port = 5001

    @staticmethod
    def __processing_str(args: tuple) -> str:
        return ' '.join(args[1:])

    def send(self, args):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(bytes(self.__processing_str(args), encoding='UTF-8'))
            data = s.recv(1024).decode('UTF-8')
            print(data)


if __name__ == "__main__":
    client = Client()
    client.send(sys.argv)

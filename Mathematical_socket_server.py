import socket
from mathematical_logic import multi_func


class ValidationException(Exception):
    pass


class Server:
    def __init__(self):
        self.__host = '127.0.0.1'
        self.__port = 65432

    def processing(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.__host, self.__port))
            s.listen()
            conn, address = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024).decode('UTF-8')
                    print(data)
                    query = multi_func(data)
                    if not data:
                        break
                    conn.sendall(bytes(str(query), encoding="UTF-8"))


if __name__ == "__main__":
    server = Server()
    server.processing()
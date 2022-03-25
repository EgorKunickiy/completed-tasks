import socket
from create_db import processing_to_query


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
                    query = processing_to_query(data)
                    conn.sendall(bytes(str(query), encoding="UTF-8"))
                    if data:
                        break


if __name__ == "__main__":
    server = Server()
    server.processing()

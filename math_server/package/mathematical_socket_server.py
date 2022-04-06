import socket
from create_db import processing_to_query
import concurrent.futures


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
                    pool = concurrent.futures.ProcessPoolExecutor()

                    data = conn.recv(1024).decode('UTF-8')
                    query = pool.submit(processing_to_query, (data, ))
                    query.add_done_callback(conn.sendall(bytes(str(query.result()), encoding="UTF-8")))
                    if data:
                        break


if __name__ == "__main__":
    server = Server()
    server.processing()

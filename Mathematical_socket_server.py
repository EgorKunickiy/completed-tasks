import socket
import operator


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
                    query = self.__multi_func(data)
                    if not data:
                        break
                    conn.sendall(bytes(str(query), encoding="UTF-8"))

    @staticmethod
    def __multi_func(data: str):
        try:
            name_operator, num1, num2 = data.split(', ')
            num1 = float(num1)
            num2 = float(num2)
            result = getattr(operator, name_operator)(num1, num2)
            return result
        except AttributeError:
            return ' '
        except ValueError:
            return ' '


if __name__ == "__main__":
    server = Server()
    server.processing()

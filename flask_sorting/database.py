import pymongo
from config_for_db import NAME, PORT, HOST
from timeit import default_timer as timer


class DataBase:
    def __init__(self, host: str, port: int, name: str):
        self.__host = host
        self.__port = port
        self.__client = pymongo.MongoClient(host, port)
        self.__db = self.__client[name]
        self.__posts = self.__db.posts

    def add_el(self, data: list, time: float):
        self.__posts.insert_one({str(data): str(time)})

    def find_el(self, data: list):
        for post in self.__posts.find():
            if str(data) in post.keys():
                return post[str(data)]
        return None

    def delete_el(self, data):
        for post in self.__posts.find():
            if str(data) in post.keys():
                self.__posts.delete_one({str(data): post[str(data)]})

    def show(self):
        for post in self.__posts.find():
            print(post)


if __name__ == "__main__":
    db = DataBase(HOST, PORT, NAME)
    #db.add_el([34, 5, 6, 7], 2.56)
    db.show()
    t = timer()
    print(db.find_el([34, 5, 6, 7]))
    result = timer() - t
    print(result)

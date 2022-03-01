from time import perf_counter


class FindTime:
    def __init__(self):
        self.time = 0

    def get_time(self):
        return self.time

    def __enter__(self):
        self.start = perf_counter()
        self.end = 0.0
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = perf_counter()
        self.time = self.end - self.start


if __name__ == "__main__":
    with FindTime() as timer:
        a = 1
        for i in range(10000):
            a += 1

    print(timer.get_time())

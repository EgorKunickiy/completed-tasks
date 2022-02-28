from time import perf_counter


class FindTime:
    def __init__(self, state: bool):
        self.state = state

    def __enter__(self):
        self.start = perf_counter()
        self.end = 0.0
        if not self.state:
            return lambda: self.end - self.start
        else:
            return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = perf_counter()
        if self.state:
            print(self.end - self.start)


if __name__ == "__main__":
    with FindTime(True) as timer:
        a = 1
        for i in range(10000):
            a += 1

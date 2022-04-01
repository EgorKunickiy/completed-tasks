from multiprocessing import Pool
from random import random


def find_pi(count_point: int) -> float:
    point_in_round = sum([1 for i in range(count_point)
                          if random()**2 + random()**2 <= 1])
    return 4*point_in_round / count_point


def main():
    with Pool(3) as pool:
        values = (5, 15, 20, 100, 1000, 10000, 10000000)
        data = pool.map(find_pi, values)
        print(data)


if __name__ == '__main__':
    main()

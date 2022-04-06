from multiprocessing import Pool, cpu_count
from random import random


def find_pi(count_point: int) -> int:
    point_in_round = sum([1 for i in range(count_point)
                          if random()**2 + random()**2 <= 1])
    return point_in_round


def main():
    n = 100_000_000
    part_count = [n//cpu_count() for i in range(cpu_count())]
    with Pool(processes=cpu_count()) as pool:
        data = pool.map(find_pi, part_count)
        print(4 * sum(data) / n)


if __name__ == '__main__':
    main()

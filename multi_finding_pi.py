from multiprocessing import Pool, cpu_count
from random import random

CPU_COUNT = cpu_count()
pool = None


def find_pi(count_point: int) -> int:

    point_in_round = 0
    for i in range(count_point):
        if random() ** 2 + random() ** 2 <= 1:
            point_in_round += 1

    return point_in_round


def main():
    n = 100_000_000
    part_count = [n//CPU_COUNT for i in range(CPU_COUNT)]
    with pool:
        data = pool.map(find_pi, part_count)
        print(4 * sum(data) / n)


if __name__ == '__main__':
    pool = Pool(processes=CPU_COUNT)
    main()

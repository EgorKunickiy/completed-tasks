import random


def find_pi(count_point: int) -> float:
    point_in_round = sum([1 for i in range(count_point)
                          if random.random()**2 + random.random()**2 <= 1])
    return 4*point_in_round / count_point


if __name__ == "__main__":
    print(find_pi(10))
    print(find_pi(1000))
    print(find_pi(10000))
    print(find_pi(1000000))
    print(find_pi(10000000))

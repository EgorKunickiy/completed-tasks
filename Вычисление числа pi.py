import random

def find_pi(count_point: int) ->float:
    point_in_round = 0
    counter = 0
    while counter != count_point:
        x = random.random()
        y = random.random()
        counter += 1
        if x**2 + y**2 <= 1:
            point_in_round += 1

    return 4*point_in_round / count_point

if __name__ == "__main__":
    print(find_pi(10))
    print(find_pi(1000))
    print(find_pi(10000))
    print(find_pi(1000000))
    print(find_pi(10000000))

import itertools

'''here I used the itertools module to find all possible combinations of different lengths,
then selected from them those whose sum is equal to num '''

def combinations(num: int, *args):
    elements = [i for i in args]
    elements.sort()
    max_len = num // elements[0]
    while max_len != 0:
        for combination in itertools.combinations_with_replacement(elements, max_len):
            if sum(combination) == num:
                print(combination)
        max_len -= 1

if __name__ == "__main__":
    combinations(10, 1, 2, 5)
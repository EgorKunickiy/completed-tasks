import itertools

def sum_v_and_p(combination: list, dict_elem: dict) -> list:
    sum_v = 0
    sum_p = 0
    for it in combination:
        list_values = dict_elem[it]
        sum_p += list_values[0]
        sum_v += list_values[1]
    return [sum_p, sum_v]

def combinations_bag ( p: int, v: int, dict_elem: dict):
    result = []
    max_price = 0
    for i in range(1, len(dict_elem)):
        for combination in itertools.combinations(dict_elem.keys(), i):
            sums_of_values = sum_v_and_p(combination, dict_elem)
            if sums_of_values[0] <= p and sums_of_values[1] <= v:
                if sums_of_values[0] > max_price:
                    result.clear()
                    max_price = sums_of_values[0]
                    result.append(combination)
                elif sums_of_values[0] == max_price:
                    result.append(combination)

    return result

if __name__ == "__main__":
    #first value is price, second is volume
    el = {
        1: [6, 4],
        2: [3, 6],
        3: [7, 1],
        4: [6, 5]
    }
    print(combinations_bag(12, 9, el))

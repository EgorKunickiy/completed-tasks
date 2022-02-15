import functools

def func_for_sort(elem):
    return elem[0]
def check_condition(data_list):
    if isinstance(data_list, list) and \
            all(map(lambda x: type(x) == tuple, data_list)) and \
            all(map(lambda x: len(x) == 2, data_list)) and \
            all(map(lambda x: type(x[1]) == str and x[1].isalnum(), data_list)):

        number_set = {data[0] for data in data_list}
        max_index = len(data_list) - 1

        return sum(number_set) == max_index*(max_index+1) / 2

    else:
        return False

def construct_the_line(data_list):

    if check_condition(data_list):
        data_list.sort(key=func_for_sort)
        return ''.join(list(map(lambda x: x[1], data_list)))
    else:
        return False

if __name__ == '__main__' :
    print(construct_the_line([(4, 'y'), ('o', 1), (3, 't'), (0, 'm'), (2, 'n')]))

    print(construct_the_line([(4, 'y'), (1, 'o'), (3, 't'), (0, 'm'), (2, 'n')]))

    print(construct_the_line([(4, 'y'), (1, 'o'), (3, 't'), (5, 'm'), (2, 'n')]))

    print(construct_the_line([(4, 'y'), (1, 'o'), (1, 't'), (0, 'm'), (2, 'n')]))

    print(construct_the_line([(4, 'y'), (1, 'o'), (3, 9), (0, 'm'), (2, 'n')]))
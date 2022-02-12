def check_condition(data_list):
    if type(data_list) == list and \
            all(map(lambda x: type(x) == tuple, data_list)) and \
            all(map(lambda x: len(x) == 2, data_list)) and \
            all(map(lambda x: type(x[1]) == str and x[1].isalnum(), data_list)):

        number_set = {data[0] for data in data_list}
        max_index = len(data_list) - 1
        # чтобы проверить правильность индексации, я занес все индексы в set
        # и сравнил сумму элементов set с суммой чисел от 0 до max_index
        return sum(number_set) == max_index*(max_index+1) / 2

    else:
        return False

def construct_the_line(data_list):

    if check_condition(data_list):
        word = ['' for i in range(len(data_list))]
        for data in data_list:
            word[data[0]] = data[1]
        return ''.join(word)
    else:
        return False

if __name__ == '__main__' :

    print(construct_the_line([(4, 'y'), ('o', 1), (3, 't'), (0, 'm'), (2, 'n')]))

    print(construct_the_line([(4, 'y'), (1, 'o'), (3, 't'), (0, 'm'), (2, 'n')]))

    print(construct_the_line([(4, 'y'), (1, 'o'), (3, 't'), (5, 'm'), (2, 'n')]))

    print(construct_the_line([(4, 'y'), (1, 'o'), (1, 't'), (0, 'm'), (2, 'n')]))

    print(construct_the_line([(4, 'y'), (1, 'o'), (3, 9), (0, 'm'), (2, 'n')]))
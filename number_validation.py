import yaml


class SumException(Exception):
    pass


class DivException(Exception):
    pass


class DiffException(Exception):
    pass


def read_file():
    with open('validation_rules.yaml', 'r') as file:
        dict_rules = yaml.safe_load(file)

    return dict_rules


def multi_func(first_num: int, second_num: int, validation_rules: dict):
    try:
        if not(validation_rules['sum']['max'] >= second_num
               >= validation_rules['sum']['min']):
            print(f'{second_num}', end='')
            raise SumException

        elif not(validation_rules['sum']['max'] >= first_num
                 >= validation_rules['sum']['min']):
            print(f'{first_num}', end='')
            raise SumException

        else:
            print('sum: ' + str(first_num + second_num))
    except SumException:
        print(f" not in range({validation_rules['sum']['min']}, "
              f"{validation_rules['sum']['max']}) for sum")

    try:
        if not(validation_rules['div']['max'] >= second_num
               >= validation_rules['div']['min']):
            print(f'{second_num}', end='')
            raise DivException

        elif not(validation_rules['div']['max'] >= first_num
                 >= validation_rules['div']['min']):
            print(f'{first_num}', end='')
            raise DivException
        elif second_num == 0:
            raise ZeroDivisionError
        else:
            print('div: ' + str(first_num / second_num))

    except DivException:
        print(f" not in range({validation_rules['div']['min']}, "
              f"{validation_rules['div']['max']}) for div")
    except ZeroDivisionError:
        print('division by zero')

    try:
        if not(validation_rules['diff']['max'] >= second_num
               >= validation_rules['diff']['min']):
            print(f'{second_num}', end='')
            raise DiffException

        elif not(validation_rules['diff']['max'] >= first_num
                 >= validation_rules['diff']['min']):
            print(f'{first_num}', end='')
            raise DiffException

        else:
            print('diff: ' + str(first_num - second_num))

    except DiffException:
        print(f" not in range({validation_rules['diff']['min']}, "
              f"{validation_rules['diff']['max']}) for diff")


if __name__ == "__main__":
    dict_rules = read_file()
    multi_func(10, 5, dict_rules)
    multi_func(8, 7, dict_rules)
    multi_func(100, 8, dict_rules)

import yaml
from operator import *


class ValidationException(Exception):
    pass


def read_file():
    with open('validation_rules.yaml', 'r') as file:
        dict_rules = yaml.safe_load(file)
    return dict_rules


def multi_func(first_num: int, second_num: int, validation_rules: dict):
    names_operator = list(validation_rules.keys())
    for operator in names_operator:
        try:
            result = globals()[operator](first_num, second_num)
            if not(validation_rules[operator]['max'] >= result
                   >= validation_rules[operator]['min']):
                print(f'{result}', end='')
                raise ValidationException

            else:
                print(operator + ": " + str(result))

        except ValidationException:
            print(f" not in range({validation_rules[operator]['min']},"
                  f"{validation_rules[operator]['max']}) for {operator}")
    print('---------------------------------------------------')

if __name__ == "__main__":
    dict_rules = read_file()
    multi_func(10, 5, dict_rules)
    multi_func(8, 7, dict_rules)
    multi_func(100, 8, dict_rules)

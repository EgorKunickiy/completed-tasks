import yaml
import operator


class ValidationException(Exception):
    pass


def read_file():
    with open('validation_rules.yaml', 'r') as file:
        dict_rules = yaml.safe_load(file)
    return dict_rules


def multi_func(first_num: int, second_num: int, validation_rules: dict):
    names_operator = list(validation_rules.keys())
    for name_oper in names_operator:
        try:
            result = getattr(operator, name_oper)(first_num, second_num)
            if not(validation_rules[name_oper]['max'] >= result
                   >= validation_rules[name_oper]['min']):
                print(f'{result}', end='')
                raise ValidationException

            else:
                print(name_oper + ": " + str(result))

        except ValidationException:
            print(f" not in range({validation_rules[name_oper]['min']},"
                  f"{validation_rules[name_oper]['max']}) for {name_oper}")
    print('---------------------------------------------------')

if __name__ == "__main__":
    dict_rules = read_file()
    multi_func(10, 5, dict_rules)
    multi_func(8, 7, dict_rules)
    multi_func(100, 8, dict_rules)

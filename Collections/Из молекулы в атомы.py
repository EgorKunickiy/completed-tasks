from collections import deque, defaultdict


def sum_dict(dict1: dict, dict2: dict) -> dict:
    result = defaultdict(int)
    new_dict = defaultdict(int)
    new_dict = dict1.copy()
    new_dict.update(dict2)
    for i in new_dict.keys():
        result[i] = dict1[i] + dict2[i]
    return result


def nesting(molecule: str) -> list:
    parentheses = {'(': ')', '[': ']', '{': '}'}
    stack = deque()
    start = -1
    end = 0
    for i in range(len(molecule)):
        if molecule[i] in parentheses.keys():
            stack.append(molecule[i])
            if start == -1:
                start = i
        elif molecule[i] in parentheses.values() and parentheses[stack[-1]] == molecule[i]:
            stack.pop()
            if len(stack) == 0:
                if end == 0:
                    end = i
                return [start, end]


def parse_molecule(molecule: str) -> dict:
    result = defaultdict(int)
    atom = ''
    count = ''
    i = 0
    while i <= len(molecule)-1:
        if molecule[i].isupper() and len(atom) == 0:
            atom += molecule[i]
        elif molecule[i].isupper() and len(atom) > 0:
            if len(count) > 0:
                result[atom] = int(count)
                atom = molecule[i]
                count = ''

            else:
                result[atom] = 1
                atom = molecule[i]

        elif molecule[i].islower():
            atom += molecule[i]
        elif molecule[i].isdigit():
            count += molecule[i]
        elif molecule[i] in ['(', '[', '{']:
            if len(count) > 0:
                result[atom] = int(count)
                atom = ''
                count = ''
            else:
                result[atom] = 1
                atom = ''

            slice_str = nesting(molecule[i::])
            pre_res = parse_molecule(molecule[i+1:slice_str[1]+i])
            i += slice_str[1] + 1
            if i <= len(molecule)-1 and molecule[i].isdigit():
                coef = ''
                while i <= len(molecule)-1 and molecule[i].isdigit():
                        coef += molecule[i]
                        i += 1
                if len(coef) > 0:
                    new_dict = defaultdict(int)
                    pre_res = {x: y*int(coef) for x, y in pre_res.items()}
                    for key, value in pre_res.items():
                        new_dict[key] = value
                    pre_res = new_dict.copy()
                i -= 1
                result = sum_dict(result, pre_res)
                return result
        i += 1

    if len(atom) > 0 and len(count) > 0:
        result[atom] = int(count)
        atom = ''
        count = ''
    elif len(atom) > 0:
        result[atom] = 1
        atom = ''

    return result


if __name__ == "__main__":
    print(parse_molecule('H2O'))
    print(parse_molecule('Mg(OH)2'))
    print(parse_molecule('K4[ON(SO3)2]2'))
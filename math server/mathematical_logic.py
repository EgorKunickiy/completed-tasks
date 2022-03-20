import operator

LIST_OF_OPERATOR = {
    'add': operator.add,
    'floordiv': operator.floordiv,
    'mod': operator.mod,
    'mul': operator.mul,
    'lt': operator.lt,
    'le': operator.le,
    'eq': operator.eq,
    'ne': operator.ne,
    'ge': operator.ge,
    'gt': operator.gt,
    'pow': operator.pow,
    'sub': operator.sub,
    'truediv': operator.truediv
}


def multi_func(data: str) -> str:
    try:
        name_operator, num1, num2 = data.split(' ')
        if name_operator not in LIST_OF_OPERATOR.keys():
            raise AttributeError
        num1 = float(num1)
        num2 = float(num2)
        result = LIST_OF_OPERATOR[name_operator](num1, num2)
        # additionally convert to float for Boolean
        return str(float(result))
    except AttributeError:
        return ' '
    except ValueError:
        return ' '

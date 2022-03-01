import inspect


def validate_arguments(function_to_validation):
    sig_func = inspect.signature(function_to_validation)
    names_args = list(sig_func.parameters.keys())

    def function_to_receive_arguments(*args):
        if len(names_args) == 1:
            for arg in args:
                assert (isinstance(arg, sig_func.parameters[names_args[0]].annotation)), 'does not match the data type'
        else:
            for arg, name_arg in zip(args, names_args):
                assert (isinstance(arg, sig_func.parameters[name_arg].annotation)), 'does not match the data type'

        function_to_validation(*args)
    return function_to_receive_arguments


@validate_arguments
def func(a: str, b: int, c: dict):
    print('ok')


@validate_arguments
def func2(*args: int):
    print('ok')


if __name__ == "__main__":
    func2(1, 2, 3, 445)
    func('qwer', [6, 7, 8], {2: 4})

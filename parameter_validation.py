def validate_arguments(function_to_validation):
    def a_wrapper_accepting_arguments(a: str, b: int, c: dict):
        assert isinstance(a, str), "a не является строкой"
        assert isinstance(b, int), "b не является обьектом целочисленного типа"
        assert isinstance(c, dict), "c не является словарем"
        function_to_validation(a, b, c)
    return a_wrapper_accepting_arguments

@validate_arguments
def func(a: str, b: int, c: dict):
    print('ok')


if __name__ == "__main__":
    func('qwer', 4, {2: 4})
    func(2, 3, {2: 4})

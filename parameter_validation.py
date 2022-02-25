def func(a: str, b: int, c: dict):
    assert isinstance(a, str), "a не является строкой"
    assert isinstance(b, int), "b не является обьектом целочисленного типа"
    assert isinstance(c, dict), "c не является словарем"


if __name__ == "__main__":
    func('qwer', 4, {2: 4})
    func(2, 3, {2: 4})

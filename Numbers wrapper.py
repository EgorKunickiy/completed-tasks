class NumberWrapper:
    def __init__(self, *args):
        self.__list_of_number = list(args)

    def __len__(self):
        return len(self.__list_of_number)

    def __gt__(self, other: 'NumberWrapper'):

        assert len(self.__list_of_number) == len(other.__list_of_number), 'Objects have different lengths'
        for i, j in zip(self.__list_of_number, other.__list_of_number):
            if i < j:
                return False
            return True

    def __lt__(self, other: 'NumberWrapper'):
        assert len(self.__list_of_number) == len(other.__list_of_number), 'Objects have different lengths'
        for i, j in zip(self.__list_of_number, other.__list_of_number):
            if i > j:
                return False
            return True

    def __eq__(self, other: 'NumberWrapper'):
        assert len(self.__list_of_number) == len(other.__list_of_number), 'Objects have different lengths'
        assert isinstance(other, NumberWrapper), 'Objects have different class'
        for i, j in zip(self.__list_of_number, other.__list_of_number):
            if i != j:
                return False
            return True

    def __add__(self, other):
        res = []
        assert len(self.__list_of_number) == len(other.__list_of_number), 'Objects have different lengths'
        for i, j in zip(self.__list_of_number, other.__list_of_number):
            res.append(i + j)
        return NumberWrapper(*res)

    def __sub__(self, other: 'NumberWrapper'):
        res = []
        assert len(self.__list_of_number) == len(other.__list_of_number), 'Objects have different lengths'
        for i, j in zip(self.__list_of_number, other.__list_of_number):
            res.append(i - j)
        return NumberWrapper(*res)

    def __mul__(self, other: 'NumberWrapper'):
        res = []
        assert len(self.__list_of_number) == len(other.__list_of_number), 'Objects have different lengths'
        for i, j in zip(self.__list_of_number, other.__list_of_number):
            res.append(i * j)
        return NumberWrapper(*res)

    def __truediv__(self, other):
        res = []
        assert len(self.__list_of_number) == len(other.__list_of_number), 'Objects have different lengths'
        for i, j in zip(self.__list_of_number, other.__list_of_number):
            res.append(i / j)
        return NumberWrapper(*res)

    def __str__(self):
        return f'NumberWrapper:{self.__list_of_number}'

    def append(self, num: int):
        self.__list_of_number.append(num)
        return self

    def __getitem__(self, item: int):
        return self.__list_of_number[item]

    def __setitem__(self, key: int, value: int):
        self.__list_of_number[key] = value

    def __delitem__(self, key: int):
        del self.__list_of_number[key]


if __name__ == "__main__":
    num1 = NumberWrapper(1, 2, 3)
    num2 = NumberWrapper(4, 5, 6)
    print(num2 > num1)
    print(num1 < num2)
    print(num1 == num2)
    print(len(num1))
    print(num1 + num2)
    print(num2 - num1)
    print(num2 * num1)
    print(num2 / num1)
    print(num1.append(2))
    print(num1[0])
    num1[0] = 3
    print(num1)
    del num1[2]
    print(num1)

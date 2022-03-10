class LenException(Exception):
    pass


class ClassException(Exception):
    pass


class NumberWrapper:
    def __init__(self, *args):
        self.__list_of_number = list(args)

    def __len__(self):
        return len(self.__list_of_number)

    def __gt__(self, other):
        try:
            if len(self.__list_of_number) != len(other.__list_of_number):
                raise LenException
            else:
                for i, j in zip(self.__list_of_number, other.__list_of_number):
                    if i < j:
                        return False
                return True
        except LenException:
            print('Objects have different lengths')

    def __lt__(self, other):
        try:
            if len(self.__list_of_number) != len(other.__list_of_number):
                raise LenException
            else:
                for i, j in zip(self.__list_of_number, other.__list_of_number):
                    if i > j:
                        return False
                return True
        except LenException:
            print('Objects have different lengths')

    def __eq__(self, other):
        try:
            if len(self.__list_of_number) != len(other.__list_of_number):
                raise LenException
            elif not(isinstance(other, NumberWrapper)):
                raise ClassException
            else:
                for i, j in zip(self.__list_of_number, other.__list_of_number):
                    if i != j:
                        return False
                return True
        except LenException:
            print('Objects have different lengths')
        except ClassException:
            print('Objects have different class')

    def __add__(self, other):
        try:
            if len(self.__list_of_number) != len(other.__list_of_number):
                raise LenException

            else:
                res = []
                for i, j in zip(self.__list_of_number, other.__list_of_number):
                    res.append(i + j)
                return NumberWrapper(*res)
        except LenException:
            print('Objects have different lengths')

    def __sub__(self, other):
        try:
            if len(self.__list_of_number) != len(other.__list_of_number):
                raise LenException
            else:
                res = []
                for i, j in zip(self.__list_of_number, other.__list_of_number):
                    res.append(i - j)
                return NumberWrapper(*res)
        except LenException:
            print('Objects have different lengths')

    def __mul__(self, other):
        try:
            if len(self.__list_of_number) != len(other.__list_of_number):
                raise LenException
            else:
                res = []
                for i, j in zip(self.__list_of_number, other.__list_of_number):
                    res.append(i * j)
                return NumberWrapper(*res)
        except LenException:
            print('Objects have different lengths')

    def __truediv__(self, other):
        try:
            if len(self.__list_of_number) != len(other.__list_of_number):
                raise LenException
            else:
                res = []
                for i, j in zip(self.__list_of_number, other.__list_of_number):
                    res.append(i / j)
                return NumberWrapper(*res)
        except LenException:
            print('Objects have different lengths')

    def __str__(self):
        return f'NumberWrapper:{self.__list_of_number}'

    def append(self, num):
        self.__list_of_number.append(num)
        return self

    def __getitem__(self, item):
        return self.__list_of_number[item]

    def __setitem__(self, key, value):
        self.__list_of_number[key] = value

    def __delitem__(self, key):
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

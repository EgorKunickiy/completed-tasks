import operator


class Logic:
    @staticmethod
    def multi_func(data: str) -> str:
        try:
            name_operator, num1, num2 = data.split(' ')
            num1 = float(num1)
            num2 = float(num2)
            result = getattr(operator, name_operator)(num1, num2)
            return str(result)
        except AttributeError:
            return ' '
        except ValueError:
            return ' '

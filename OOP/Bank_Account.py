class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, acc_number: int, name: str, balance: int):
        self.__account_number = acc_number
        self.__name = name
        self.__balance = balance

    def deposit(self, value):
        self.__balance += value

    def withdrawal(self, value):
        try:
            if self.__balance < value:
                raise BalanceException
            else:
                self.__balance -= value
        except BalanceException:
            print('insufficient funds in the balance sheet')

    def apply_fees(self):
        percent = self.__balance / 20
        self.__balance -= percent

    def display(self):
        print(f'Account number: {self.__account_number}')
        print(f'Name: {self.__name}')
        print(f'Balance: {self.__balance}')


if __name__ == "__main__":
    account = BankAccount(32356, 'XXXX XXXX XXX', 1234)
    account.deposit(333)
    account.display()
    account.apply_fees()
    account.display()
    account.withdrawal(1000)
    account.display()

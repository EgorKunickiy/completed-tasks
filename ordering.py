class ExceptionOfOrder(Exception):
    pass


class Dish:
    def __init__(self, quantity: int, name: str, price: float, mass: int):
        self.__quantity = quantity
        self.__name = name
        self.__price = price
        self.__mass = mass

    @property
    def get_quantity(self):
        return self.__quantity

    @property
    def get_name(self):
        return self.__name

    @property
    def get_price(self):
        return self.__price

    @property
    def get_mass(self):
        return self.__mass


class Ordering:
    def __init__(self):
        self.__list_of_dishes = None
        self.__quantity_of_dish = 0
        self.__price = 0
        self.__mass = 0
        self.__cost = 0
    @property
    def get_quantity(self):
        return self.__quantity_of_dish

    @property
    def get_list_of_dish(self) -> list:
        return self.__list_of_dishes

    @property
    def get_price(self):
        return self.__price

    @property
    def get_mass(self):
        return self.__mass

    @property
    def get_cost(self):
        return self.__cost

    def describe_the_order(self):
        try:
            if self.__list_of_dishes is None:
                raise ExceptionOfOrder
            else:
                print(f'list of dish: {list(map(lambda x: x.get_name,self.get_list_of_dish))}', sep=', ')
                print(f'total quantity: {self.get_quantity}' + '\n'
                      f'total mass: {self.get_mass}' + '\n'
                      f'total price: {self.get_price}' + '\n'
                      f'total cost: {self.get_cost}')

        except ExceptionOfOrder:
            print(f'Order is empty')

    def append_dish(self, *args: Dish):
        self.__list_of_dishes = [dish for dish in args]
        self.__recalculate_data()

    def __recalculate_data(self):
        for dish in self.__list_of_dishes:
            self.__quantity_of_dish += dish.get_quantity
            self.__mass += dish.get_mass
            self.__price += dish.get_price * dish.get_quantity
        self.__cost = self.__price

    def pay(self, value):
        self.__cost -= value
        if self.__cost == 0:
            print('order paid')
        elif self.__cost < 0:
            print(f'order paid, change: {abs(self.__cost)}')
            self.__cost = 0
        else:
            print(f'left to pay {self.get_cost}')


if __name__ == "__main__":
    dish_1 = Dish(1, 'croissant', 1.55, 130)
    dish_2 = Dish(1, 'soup', 4, 300)
    dish_3 = Dish(2, 'tea', 2.05, 100)

    ordering = Ordering()
    ordering.append_dish(dish_1, dish_2, dish_3)
    ordering.describe_the_order()
    ordering.pay(10)

    ordering_2 = Ordering()
    ordering_2.describe_the_order()

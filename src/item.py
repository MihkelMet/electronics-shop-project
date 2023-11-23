import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return self.__name

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise TypeError("Складывать можно только объекты классов с родительским классом Item")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            self.__name = new_name[:10]
            raise Exception("name is longer than 10")
        self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls, filename):
        with open(filename, encoding='utf-8') as file:
            items = csv.DictReader(file)
            list_items = []
            for item in items:
                name = item['name']
                price = float(item['price'])
                quantity = int(item['quantity'])
                i = cls(name, price, quantity)
                list_items.append(i)
            cls.all = list_items

    @staticmethod
    def string_to_number(number):
        new_number = number.split('.')
        return int(new_number[0])

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.quantity * self.price
        return total_price

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price

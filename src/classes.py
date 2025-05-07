from itertools import product
from typing import List, Optional


class Product:
    """Класс для представления продуктов"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name  # Название товара
        self.description = description  # Описание товара
        self.__price = price  # Цена товара (в рублях, с копейками)
        self.quantity = quantity  # Количество товара в наличии (в штуках)

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Складывать можно только с другим продуктом")
        return self.__price * self.quantity + other.__price * other.quantity

    @classmethod
    def new_product(cls, data: dict):
        return cls(
            name=data["name"],
            description=data["description"],
            price=data["price"],
            quantity=data["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            confirm = input(
                f"Вы действительно хотите понизить цену с {self.__price} до {new_price}? (y/n): "
            )
            if confirm.lower() == "y":
                self.__price = new_price
            else:
                print("Цена осталась прежней")
        else:
            self.__price = new_price

    @classmethod
    def new_product_upgrated(
        cls, data: dict, existing_products: Optional[List["Product"]] = None
    ):
        existing_products = existing_products or []
        for product in existing_products:
            if product.name == data["name"]:
                product.quantity += data["quantity"]
                product.__price = max(product.price, data["price"])
                return product
            return cls(
                name=data["name"],
                description=data["description"],
                price=data["price"],
                quantity=data["quantity"],
            )

    # Варинт с форматом list
    # @classmethod
    # def new_product(cls, data: list):
    #     return cls(
    #         name=data[0],
    #         description=data[1],
    #         price=data[2],
    #         quantity=data[3],
    #     )


class Category:
    """Класс для представления категорию"""

    category_count = 0  # Статическая переменная для подсчета категорий
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name  # Название категории
        self.description = description  # Описание категории
        self.__products = products  # Список товаров в категории (объекты класса Product)
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только экземпляры класса Product или его подклассов")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        # return "\n".join(str(product) for product in self.__products)
        return self.__products

    @property
    def products_list_str(self):
        return "\n".join(str(product) for product in self.__products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __iter__(self):
        return CategoryIterator(self)


class CategoryIterator:
    def __init__(self, category):
        self._products = category._Category__products
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._products):
            result = self._products[self._index]
            self._index += 1
            return result
        raise StopIteration


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: float, model: str, memory: int, color:str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать продукты разных типов")
        return self.price * self.quantity + other.price * other.quantity


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: str, color:str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать продукты разных типов")
        return self.price * self.quantity + other.price * other.quantity

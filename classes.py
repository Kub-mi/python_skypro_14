from typing import List

class Product:
    """Класс для представления продуктов"""
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name  # Название товара
        self.description = description  # Описание товара
        self.__price = price  # Цена товара (в рублях, с копейками)
        self.quantity = quantity  # Количество товара в наличии (в штуках)


    @classmethod
    def new_product(cls, data: dict):
        return cls(
            name = data['name'],
            description = data['description'],
            price = data['price'],
            quantity = data['quantity'],
        )


    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            confirm = input(f"Вы действительно хотите понизить цену с {self.__price} до {new_price}? (y/n): ")
            if confirm.lower() == 'y':
                self.__price = new_price
            else:
                print("Цена осталась прежней")
        else:
            self.__price = new_price


    @classmethod
    def new_product_upgrated(cls, data: dict, existing_products: List["Product"] = None):
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
                quantity=data["quantity"]
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

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только экземпляры класса Product или его наследников")
        self.__products.append(product)
        Category.category_count += 1

    @property
    def products(self):
        return "".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
            for product in self.__products
        )

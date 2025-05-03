from typing import List

class Product:
    """Класс для представления продуктов"""
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name  # Название товара
        self.description = description  # Описание товара
        self.price = price  # Цена товара (в рублях, с копейками)
        self.quantity = quantity  # Количество товара в наличии (в штуках)

class Category:
    """Класс для представления категорию"""
    category_count = 0  # Статическая переменная для подсчета категорий
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name  # Название категории
        self.description = description  # Описание категории
        self.products = products  # Список товаров в категории (объекты класса Product)
        Category.category_count += 1
        Category.product_count += len(products)

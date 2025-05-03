import pytest
from classes import Product, Category


@pytest.fixture
def sample_products():
    return [
        Product("Товар 1", "Описание 1", 100.0, 10),
        Product("Товар 2", "Описание 2", 200.0, 5)
    ]


@pytest.fixture
def reset_category_counts():
    """Сброс счетчиков перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


def test_product_initialization():
    product = Product("Наушники", "Bluetooth-наушники", 1500.0, 12)
    assert product.name == "Наушники"
    assert product.description == "Bluetooth-наушники"
    assert product.price == 1500.0
    assert product.quantity == 12


def test_category_initialization(reset_category_counts, sample_products):
    category = Category("Электроника", "Раздел с электроникой", sample_products)
    assert category.name == "Электроника"
    assert category.description == "Раздел с электроникой"
    assert category.products == sample_products


def test_category_and_product_count(reset_category_counts, sample_products):
    """Создание двух категорий"""
    category1 = Category("Категория 1", "Описание 1", sample_products)
    category2 = Category("Категория 2", "Описание 2", [sample_products[0]])

    assert Category.category_count == 2
    assert Category.product_count == 3  # 2 продукта в первой категории + 1 во второй

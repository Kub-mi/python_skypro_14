import pytest
from src.classes import Product, Category, Smartphone, LawnGrass


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


def test_product_price_setter_positive():
    product = Product("Товар", "Описание", 100.0, 10)
    product.price = 120.0
    assert product.price == 120.0


def test_product_price_setter_negative(capfd):
    product = Product("Товар", "Описание", 100.0, 10)
    product.price = -50.0
    out, _ = capfd.readouterr()
    assert "Цена не должна быть нулевая или отрицательная"
    assert product.price == 100.0


def test_category_add_product(reset_category_counts, sample_products):
    category = Category("Техника", "Описание", sample_products)
    new_product = Product("Новый", "Описание", 500.0, 3)
    category.add_product(new_product)
    assert "Новый, 500.0 руб. Остаток: 3 шт." in category.products_list_str


def test_product_classmethod():
    data = {
        "name": "Тест",
        "description": "Тест продукт",
        "price": 300.0,
        "quantity": 2
    }
    product = Product.new_product(data)
    assert isinstance(product, Product)
    assert product.name == "Тест"
    assert product.price == 300.0


def test_new_product_merging_existing():
    existing = [
        Product("Товар A", "Описание", 500.0, 3)
    ]

    data = {
        "name": "Товар A",
        "description": "Новое описание",  # не влияет
        "price": 600.0,  # выше старой
        "quantity": 2
    }

    updated_product = Product.new_product_upgrated(data, existing)

    assert updated_product.quantity == 5  # 3 + 2
    assert updated_product.price == 600.0  # берём максимальную цену
    assert updated_product is existing[0]  # возвращаем тот же объект


def test_price_setter_confirm_lower_price_yes(monkeypatch):
    product = Product("Товар", "Описание", 1000.0, 1)

    # Подтверждаем снижение (ввод 'y')
    monkeypatch.setattr("builtins.input", lambda _: "y")
    product.price = 800.0
    assert product.price == 800.0


def test_price_setter_confirm_lower_price_no(monkeypatch, capfd):
    product = Product("Товар", "Описание", 1000.0, 1)

    # Отказываемся понижать цену (ввод 'n')
    monkeypatch.setattr("builtins.input", lambda _: "n")
    product.price = 800.0

    assert product.price == 1000.0  # цена не изменилась

    out, _ = capfd.readouterr()
    assert "Цена осталась прежней" in out


def test_product_add():
    p1 = Product("Товар A", "Описание", 100.0, 10)
    p2 = Product("Товар B", "Описание", 200.0, 2)
    assert p1 + p2 == 1400.0


def test_product_str():
    product = Product("Товар", "Описание", 100.0, 10)
    assert str(product) == "Товар, 100.0 руб. Остаток: 10 шт."


def test_category_str():
    products = [
        Product("Товар1", "Описание", 100.0, 2),
        Product("Товар2", "Описание", 200.0, 3)
    ]
    category = Category("Категория", "Описание", products)
    assert str(category) == "Категория, количество продуктов: 5 шт."


def test_add_valid_product():
    category = Category("Смартфоны", "Категория смартфонов", [])
    phone = Smartphone("iPhone", "desc", 50000.0, 3, 90.0, "14", 128, "черный")
    category.add_product(phone)
    assert "iPhone" in category.products_list_str


def test_add_non_product_instance():
    class NotProduct:
        pass
    category = Category("Смартфоны", "Категория смартфонов", [])
    with pytest.raises(TypeError):
        category.add_product(NotProduct())


def test_add_product_subclass():
    category = Category("Газоны", "Категория трав", [])
    grass = LawnGrass("Газон", "desc", 300.0, 10, "RU", "7 дней", "Зеленый")
    category.add_product(grass)
    assert "Газон" in category.products_list_str

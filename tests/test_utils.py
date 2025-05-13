import json

from src.classes import Category, Product
from src.utils import load_data_from_json


def test_load_data_from_json(tmp_path):
    # Подготовка: создаём временный JSON-файл
    test_data = [
        {
            "name": "Электроника",
            "description": "Разные устройства",
            "products": [
                {
                    "name": "Смартфон",
                    "description": "Мощный смартфон",
                    "price": 49999.99,
                    "quantity": 10
                },
                {
                    "name": "Планшет",
                    "description": "Для учёбы",
                    "price": 29999.50,
                    "quantity": 5
                }
            ]
        }
    ]

    test_file = tmp_path / "test_data.json"
    with test_file.open("w", encoding="utf-8") as f:
        json.dump(test_data, f, ensure_ascii=False)

    # Вызов функции
    result = load_data_from_json(str(test_file))

    # Проверки
    assert isinstance(result, list)
    assert len(result) == 1
    category = result[0]
    assert isinstance(category, Category)
    assert category.name == "Электроника"
    assert category.description == "Разные устройства"
    assert len(category.products) == 2

    product1 = category.products[0]
    assert isinstance(product1, Product)
    assert product1.name == "Смартфон"
    assert product1.description == "Мощный смартфон"
    assert product1._BaseProduct__price == 49999.99  # если price приватный
    assert product1.quantity == 10
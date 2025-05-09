import pytest

from src.classes import LawnGrass, Smartphone


def test_lawnGrass():
    grass = LawnGrass("Товар 1", "Описание 1", 100.0, 10, "Россия", "2 мес", "Зеленый")
    assert grass.name == "Товар 1"
    assert grass.description == "Описание 1"
    assert grass.price == 100.0
    assert grass.quantity == 10
    assert grass.country == "Россия"
    assert grass.germination_period == "2 мес"
    assert grass.color == "Зеленый"


def test_add_same_grass_only():
    phone1 = Smartphone("Phone A", "desc", 10000.0, 2, 90.0, "A", 64, "Gray")
    grass1 = LawnGrass("Grass A", "desc", 200.0, 5, "RU", "5 дней", "Green")
    grass2 = LawnGrass("Grass B", "desc", 250.0, 3, "USA", "7 дней", "Dark Green")
    assert grass1 + grass2 == 5 * 200.0 + 3 * 250.0

    with pytest.raises(TypeError):
        _ = phone1 + grass1

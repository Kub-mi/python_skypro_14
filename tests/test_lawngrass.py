import pytest
from src.classes import LawnGrass


def test_lawnGrass():
    grass = LawnGrass("Товар 1", "Описание 1", 100.0, 10, "Россия", "2 мес", "Зеленый")
    assert grass.name == "Товар 1"
    assert grass.description == "Описание 1"
    assert grass.price == 100.0
    assert grass.quantity == 10
    assert grass.country == "Россия"
    assert grass.germination_period == "2 мес"
    assert grass.color == "Зеленый"
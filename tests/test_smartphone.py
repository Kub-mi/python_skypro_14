import pytest
from src.classes import Smartphone, LawnGrass


@pytest.fixture
def init_sp():
    Smartphone("Товар 1", "Описание 1", 100.0, 10, 100, "iphone 11", "256 ГБ", "Черный")


def test_smartphone():
    phone = Smartphone("Товар 1", "Описание 1", 100.0, 10, 95.5, "iphone 11", 256, "Черный")
    assert phone.name == "Товар 1"
    assert phone.description == "Описание 1"
    assert phone.price == 100.0
    assert phone.quantity == 10
    assert phone.efficiency == 95.5
    assert phone.model == "iphone 11"
    assert phone.memory == 256
    assert phone.color == "Черный"

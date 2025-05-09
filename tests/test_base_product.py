import pytest

from src.classes import BaseProduct


def test_base_product_is_abstract():
    with pytest.raises(TypeError):
        BaseProduct("Название", "Описание", 100.0, 10)  # Нельзя создать экземпляр

from src.classes import Product


def test_mixin_print(capsys):
    Product("Продукт1", "Описание продукта", 1200, 10)
    captured = capsys.readouterr()
    assert "Создан объект Product с параметрами:" in captured.out
    assert "('Продукт1', 'Описание продукта', 1200, 10)" in captured.out

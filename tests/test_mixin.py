from src.classes import Product


def test_mixin_print(capsys):
    Product("Продукт1", "Описание продукта", 1200, 10)
    captured = capsys.readouterr()
    assert (
        "Product(name=Продукт1, description=Описание продукта, _BaseProduct__price=1200, quantity=10)"
        in captured.out
    )

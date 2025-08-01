# Категории и товары на Python

Проект демонстрирует работу с объектно-ориентированным программированием на Python: создаются классы `Product` и `Category`, реализуется загрузка данных из JSON-файла, а также написаны тесты с использованием `pytest`.


## 🚀 Возможности

- Создание объектов товаров и категорий
- Подсчет количества категорий и товаров (на уровне класса)
- Загрузка данных из файла `data.json`
- Тесты для проверки инициализации и логики классов

## 🔧 Установка

1. Склонируйте репозиторий или скачайте файлы.
2. Убедитесь, что у вас установлен Python 3.7+.
3. Установите зависимости:

```bash
pip install pytest
```
## ▶️ Запуск
Пример выполнения:
```bash
python main.py
```

## 📂 Формат JSON-файла
```bash
[
  {
    "name": "Смартфоны",
    "description": "Мобильные устройства...",
    "products": [
      {
        "name": "iPhone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
      }
    ]
  }
]
```

class Product:
    def __init__(self, name, price):
        self.name = name  # Название продукта
        self.price = price  # Цена продукта

    def get_name(self):
        return self.name  # Возвращает название продукта

    def get_price(self):
        return self.price  # Возвращает цену продукта

    def get_description(self):
        return f"Название: {self.name}, Цена: {self.price}"

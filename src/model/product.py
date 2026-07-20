class Product:
    def __init__(self, id=None, name="", price=0, quantity=0):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Price: {self.price}\n"
            f"Quantity: {self.quantity}\n"
        )


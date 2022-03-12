from dataclasses import dataclass

class Amazon:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        if self.quantity == 1:
            return f"You bought a {self.name} that cost ${self.price}."
        else:
            return f"You bought {self.quantity} pcs of {self.name} that cost ${self.price}. Total sum ${self.total_cost()}."

    def total_cost(self):
        return self.price * self.quantity


@dataclass
class Ebay:
    name: str
    price: float
    quantity: int

    def total_cost(self):
        return self.price * self.quantity


cart1 = Amazon("Xbox", 300, 2)
print(cart1)
print(cart1.total_cost())

cart2 = Ebay("Playstation", 300.50, 3)
print(cart2)
print(cart2.total_cost())



from abc import ABC, abstractmethod

class Drink(ABC):
    @abstractmethod
    def get_taste(self):
        pass

    @abstractmethod
    def is_addictive(self):
        pass

class Coffee(Drink):
    def get_taste(self):
        return "strong"

    def is_addictive(self):
        return True

class Tea(Drink):
    def get_taste(self):
        return "sweet"

    def is_addictive(self):
        return False

class DrinkPurchase():
    def buy(self):
        print("Go to counter")
        print("Order drink")
        print("Pay")

class CoffeePurchase(DrinkPurchase):
    def buy(self):
        super().buy()
        return Coffee()

class TeaPurchase(DrinkPurchase):
    def buy(self):
        super().buy()
        return Tea()
from abc import ABC, abstractmethod


class Pizza(ABC):
    def __init__(self):
        self.title = ''
        self.price = 0
        self.ingredients = []
        self.ready = False
        self.vegetarian = False

    def __repr__(self):
        text = f"{self.title} pizza with {self.ingredients} and {self.price}$"
        if self.vegetarian:
            text += ' (vegetarian)'
        return text


class PizzaBuilder(ABC):
    def __init__(self):
        self.pizza = Pizza()

    @abstractmethod
    def prepare_dough(self):
        pass

    @abstractmethod
    def add_extras(self):
        pass

    @abstractmethod
    def bake(self):
        pass


class MargheritaBuilder(PizzaBuilder):

    def prepare_dough(self):
        self.pizza.title = "Margherita"
        self.pizza.price = 2
        self.pizza.ingredients.append("Dough")
        print("Preparing dough for Margherita pizza")
        self.pizza.vegetarian = True

    def add_extras(self):
        print("Adding extra cheese and jalapeno to Margherita pizza")
        self.pizza.ingredients.append("Extra cheese")
        self.pizza.price += 1
        self.pizza.ingredients.append("Jalapeno")
        self.pizza.price += 0.5
        self.pizza.vegetarian = True

    def bake(self):
        print("Baking Margherita pizza")
        self.pizza.ready = True

class PepperoniBuilder(PizzaBuilder):

    def prepare_dough(self):
        self.pizza.title = "Pepperoni"
        self.pizza.price = 3
        self.pizza.ingredients.append("Dough")
        print("Preparing dough for Pepperoni pizza")
        self.pizza.vegetarian = False

    def add_extras(self):
        print("Adding extra cheese and ham to Pepperoni pizza")
        self.pizza.ingredients.append("Extra cheese")
        self.pizza.price += 1
        self.pizza.ingredients.append("Ham")
        self.pizza.price += 0.5
        self.pizza.vegetarian = False

    def bake(self):
        print("Baking Pepperoni pizza")
        self.pizza.ready = True

class Cook:
    def __init__(self):
        self._builder = None

    def prepare_pizza(self, builder):
        self._builder = builder
        self._builder.prepare_dough()
        self._builder.add_extras()
        self._builder.bake()
        return self._builder.pizza



if __name__ == "__main__":
    cook = Cook()
    margherita = cook.prepare_pizza(MargheritaBuilder())
    print(margherita)
    print(f"Pizza price: {margherita.price}")
    print(f"Pizza ingredients: {margherita.ingredients}")

    pepperoni = cook.prepare_pizza(PepperoniBuilder())
    print(pepperoni)
    print(f"Pizza price: {pepperoni.price}")
    print(f"Pizza ingredients: {pepperoni.ingredients}")

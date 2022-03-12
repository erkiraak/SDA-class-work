class Animal:
    def __init__(self, name, age, weight, breed):
        self.name = name
        self.age = age
        self.weight = weight
        self.breed = breed

    def __str__(self):
        return f"Name: {self.name}, age: {self.age}, weight: {self.weight}"


class Dog(Animal):
    def __init__(self, name, age, weight, breed, color):
        self.color = color
        Animal.__init__(self, name, age, weight, breed)

    def bark(self):
        print("woof")

    def __str__(self):
        return super().__str__() + " " + self.name


class Cat(Animal):
    def __init__(self, name, age, weight, breed, fur):
        Animal.__init__(self, name, age, weight, breed)
        self.fur = fur

    def __str__(self):
        return super().__str__() + " " + self.breed


class CatDog(Cat, Dog):
    def __init__(self, name, age, weight, breed, fur, color):
        Cat.__init__(self, name, age, weight, breed, fur)
        Dog.__init__(self, name, age, weight, breed, color)

cat = Cat("Felix", 5, 5.0, "Cat", True)
dog = Dog("Rex", 8, 30.0, "German", "brown")
wtf = CatDog("Fex", 1, 15.0, "German cat", False, "brown")

print(cat)
print(dog)
print(wtf)

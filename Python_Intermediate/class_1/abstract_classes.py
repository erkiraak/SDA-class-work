from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def __init__(self, name, age, salary, tax_rate):
        self.name = name
        self.age = age
        self.salary = salary
        self.tax_rate = tax_rate

    @abstractmethod
    def paid_amount(self):
        return self.salary * self.tax_rate

    def __str__(self):
        return f"{self.name}, age {self.age} gets paid {self.paid_amount()}"


class Intern(Person):
    def __init__(self, name, age, salary):
        self.tax_rate = 0.9
        super().__init__(name, age, salary, self.tax_rate)

    def paid_amount(self):
        if super().paid_amount() < 500:
            return 500
        else:
            return super().paid_amount()


class Junior(Person):
    def __init__(self, name, age, salary):
        self.tax_rate = 0.9
        super().__init__(name, age, salary, self.tax_rate)

    def paid_amount(self):
        if 501 < self.salary < 1500:
            self.tax_rate = 0.8
        return super().paid_amount()


class Senior(Person):
    def __init__(self, name, age, salary):
        self.tax_rate = 0.8
        super().__init__(name, age, salary, self.tax_rate)

    def paid_amount(self):
        if 1501 < self.salary:
            self.tax_rate = 0.7
        return super().paid_amount()


i = Intern("Intern", 18, 1000)
j = Junior("Junior", 23, 1600)
s = Senior("Senior", 24, 4020)

print(i)
print(j)
print(s)


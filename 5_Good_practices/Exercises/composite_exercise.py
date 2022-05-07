from abc import ABC, abstractmethod
from decorator_composite import capitalize

class Element(ABC):
    @abstractmethod
    def get_name(self):
        pass
    @abstractmethod
    def get_salary(self):
        pass
    @abstractmethod
    def get_number_of_vacation_days(self):
        pass


class Department(Element):
    def __init__(self, name):
        self.name = name
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    @capitalize
    def get_name(self):
        return self.name

    def get_salary(self):
        salary = 0
        for element in self.elements:
            salary += element.get_salary()

        return salary

    def get_number_of_vacation_days(self):
        vacation_days = 0
        for element in self.elements:
            vacation_days += element.get_number_of_vacation_days()

        return vacation_days


class Employee(ABC):
    def __init__(self, name, earnings, number_of_vacation_days):
        self.name = name
        self.earnings = earnings
        self.number_of_vacation_days = number_of_vacation_days

    @capitalize
    def get_name(self):
        return self.name

    def get_salary(self):
        return self.earnings

    def get_number_of_vacation_days(self):
        return self.number_of_vacation_days



if __name__ == "__main__":
    management = Department("management")
    engineering = Department("engineering")
    sales = Department("sales")
    marketing = Department("Marketing")

    management.add_element(engineering)
    management.add_element(sales)
    management.add_element(marketing)

    management.add_element(Employee("John", 1000, 10))
    management.add_element(Employee("Mary", 2000, 20))
    engineering.add_element(Employee("Bob", 3000, 30))
    engineering.add_element(Employee("Alice", 4000, 40))
    sales.add_element(Employee("Tom", 5000, 50))
    sales.add_element(Employee("Jerry", 6000, 60))
    marketing.add_element(Employee("Peter", 7000, 70))
    marketing.add_element(Employee("Paul", 8000, 80))

    print(management.get_name())
    print(management.get_salary())
    print(management.get_number_of_vacation_days())

    for element in management.elements:
        print(element.get_name())
        print(element.get_salary())
        print(element.get_number_of_vacation_days())
    print("\n")

    print(engineering.get_name())
    print(engineering.get_salary())
    print(engineering.get_number_of_vacation_days())

    for element in engineering.elements:
        print(element.get_name())
        print(element.get_salary())
        print(element.get_number_of_vacation_days())
    print("\n")




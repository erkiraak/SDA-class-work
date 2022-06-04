from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def __init__(self):
        pass


class Boy(Person):
    def __init__(self):
        self.number_of_children = 0
        self.gender = "M"


class Girl(Person):
    def __init__(self):
        self.number_of_children = 0
        self.gender = "F"


class Father(Person):
    def __init__(self):
        self.number_of_children = 0
        self.gender = "M"
        self.children = []

    def add_child(self, child_obj):
        self.number_of_children += 1
        self.children.append(child_obj)


if __name__ == "__main__":
    father1 = Father()
    father21 = Father()
    father22 = Father()
    boy31 = Boy()
    girl32 = Girl()
    girl33 = Girl()

    father1.add_child(father21)
    father1.add_child(father22)

    father21.add_child(boy31)
    father21.add_child(girl32)

    father22.add_child(girl33)

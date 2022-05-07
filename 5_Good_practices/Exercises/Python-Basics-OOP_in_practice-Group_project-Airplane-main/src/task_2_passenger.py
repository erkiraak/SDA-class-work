from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, id_num, name):
        self.id = id_num
        self.name = name

    @abstractmethod
    def __str__(self):
        pass


class Pilot(Person):
    def __str__(self):
        return f'{self.name} ({self.id}) is the pilot.'


class Crew(Person):
    def __str__(self):
        return f'{self.name} ({self.id}) is a crew member.'


class Passenger(Person):
    def __str__(self):
        return f'{self.name} ({self.id}) is a passenger.'

if __name__ == "__main__":
    pilot = Pilot("X01", 'John')
    print(pilot)
    crew = Crew("X02", 'Jane')
    print(crew)
    passenger = Passenger("X03", 'Jack')
    print(passenger)

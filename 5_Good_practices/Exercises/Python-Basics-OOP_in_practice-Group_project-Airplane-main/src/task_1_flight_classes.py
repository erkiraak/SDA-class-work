from abc import ABC, abstractmethod
from task_0_singleton import singleton


class FlightClass(ABC):
    @staticmethod
    @abstractmethod
    def perks():
        pass


@singleton
class FirstClass(FlightClass):
    @staticmethod
    def perks():
        return """First Class:
        Perks:
                Extra Leg Room
                Comfortable Seats
                Free Beverages"""


@singleton
class BusinessClass(FlightClass):
    @staticmethod
    def perks():
        return """Business Class:
        Perks:
                Extra Leg Room
                Comfortable Seats"""


@singleton
class EconomyClass(FlightClass):
    @staticmethod
    def perks():
        return """Economy Class:
        Perks:
                None :)"""


if __name__ == "__main__":
    print(FirstClass().perks())
    print(BusinessClass().perks())
    print(EconomyClass().perks())

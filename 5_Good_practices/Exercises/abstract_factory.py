from abc import ABC, abstractmethod


class Sedan(ABC):
    @abstractmethod
    def who_am_i(self):
        pass


class LHDSedan(Sedan):
    def who_am_i(self):
        print("LHDSedan")


class RHDSedan(Sedan):
    def who_am_i(self):
        print("RHDSedan")


class Coupe(ABC):
    @abstractmethod
    def who_am_i(self):
        pass


class LHDCoupe(Coupe):
    def who_am_i(self):
        print("LHDCoupe")


class RHDCoupe(Coupe):
    def who_am_i(self):
        print("RHDCoupe")


class StationWagon(ABC):
    @abstractmethod
    def who_am_i(self):
        pass


class LHDStationWagon(StationWagon):
    def who_am_i(self):
        print("LHDStationWagon")


class RHDStationWagon(StationWagon):
    def who_am_i(self):
        print("RHDStationWagon")


class CarFactory(ABC):
    @abstractmethod
    def create_sedan(self):
        pass

    @abstractmethod
    def create_coupe(self):
        pass

    @abstractmethod
    def create_station_wagon(self):
        pass


class LHDCarFactory(CarFactory):

    def create_sedan(self):
        return LHDSedan()

    def create_coupe(self):
        return LHDCoupe()

    def create_station_wagon(self):
        return LHDStationWagon()


class RHDCarFactory(CarFactory):

    def create_sedan(self):
        return RHDSedan()

    def create_coupe(self):
        return RHDCoupe()

    def create_station_wagon(self):
        return RHDStationWagon()


if __name__ == '__main__':
    l_factory = RHDCarFactory()
    l_sedan = l_factory.create_sedan()
    l_sedan.who_am_i()
    l_coupe = l_factory.create_coupe()
    l_coupe.who_am_i()
    l_station_wagon = l_factory.create_station_wagon()
    l_station_wagon.who_am_i()

    r_factory = RHDCarFactory()
    r_sedan = r_factory.create_sedan()
    r_sedan.who_am_i()
    r_coupe = r_factory.create_coupe()
    r_coupe.who_am_i()
    r_station_wagon = r_factory.create_station_wagon()
    r_station_wagon.who_am_i()

from task_0_singleton import singleton
from task_1_flight_classes import FirstClass, BusinessClass, EconomyClass


@singleton
class Airplane:
    def __init__(self):
        self.pilot = None
        self.crew = []
        self.passengers = {
            FirstClass(): [],
            BusinessClass(): [],
            EconomyClass(): []
        }

    def __str__(self):
        txt = "Plane State:\n"
        txt += f"Pilot:\n\t{self.pilot}\n"
        txt += f"Crew:\n"
        for c in self.crew:
            txt += "\t" + str(c) + "\n"
        txt += "Classes:\n"
        for key, p_list in self.passengers.items():
            txt += key.perks() + "\n"
            txt += "\tPassengers:\n"
            for p in p_list:
                txt += "\t\t" + str(p) + "\n"

        return txt



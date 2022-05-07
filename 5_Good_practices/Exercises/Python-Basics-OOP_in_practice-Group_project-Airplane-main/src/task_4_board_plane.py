from airplane import Airplane
from task_2_passenger import Pilot, Crew, Passenger


def board_plane(person_object, *args):
    airplane = Airplane()
    if isinstance(person_object, Pilot):
        airplane.pilot = person_object
    elif isinstance(person_object, Crew):
        airplane.crew.append(person_object)
    elif isinstance(person_object, Passenger):
        airplane.passengers[args[0]].append(person_object)
    else:
        print("Wrong type of object")
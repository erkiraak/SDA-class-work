from task_1_flight_classes import FirstClass, BusinessClass, EconomyClass
from task_3_boarder_factory import BoarderFactory
from task_4_board_plane import board_plane
from airplane import Airplane


people = [
    ("X001", "Amelia Earhart", "Pilot", ""),
    ("C001", "Maria", "Crew", ""),
    ("C002", "Laura", "Crew", ""),
    ("C003", "Matt", "Crew", ""),
    ("P001", "Rami", "Passenger", FirstClass()),
    ("P002", "Sami", "Passenger", FirstClass()),
    ("P003", "Mia", "Passenger", BusinessClass()),
    ("P004", "Pia", "Passenger", BusinessClass()),
    ("P005", "John", "Passenger", EconomyClass()),
    ("P006", "Erki", "Passenger", EconomyClass()),
]


people_objects = []
for p in people:
    people_objects.append(
        BoarderFactory.create_object(p[2], p[0], p[1])
    )

i = 0
for p_obj in people_objects:
    board_plane(p_obj, people[i][3])
    i += 1

print(Airplane())

from task_2_passenger import Pilot, Crew, Passenger


class BoarderFactory:
    @staticmethod
    def create_object(boarder_type, *args, **kwargs):
        if boarder_type.lower() == 'pilot':
            return Pilot(*args, **kwargs)
        elif boarder_type.lower() == 'crew':
            return Crew(*args, **kwargs)
        elif boarder_type.lower() == 'passenger':
            return Passenger(*args, **kwargs)
        else:
            raise ValueError('Invalid boarder type')

if __name__ == "__main__":
    bf = BoarderFactory()
    pilot = bf.create_object('Pilot', 'John Doe', 'X01')
    crew1 = bf.create_object('Crew', 'John Doe', 'X02')
    passenger1 = bf.create_object('Passenger', 'John Doe', 'X04')

    print(type(pilot))
    print(pilot)
    print(type(crew1))
    print(crew1)
    print(type(passenger1))
    print(passenger1)


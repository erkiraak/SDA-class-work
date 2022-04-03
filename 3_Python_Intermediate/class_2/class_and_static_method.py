import stdnum
import datetime


class Person:
    def __init__(self, name, id_code):
        if self.is_name_correct(name) and self.is_code_correct(id_code):
            self.name = name
            self.id_code = id_code
            self.gender = self.get_gender(self.id_code)
            self.birthday = self.get_birthday(self.id_code)
            self.age = self.get_age(self.id_code)

        else:
            raise ValueError("Input parameters incorrect")

    def __str__(self):
        return f"{self.name} ({self.gender}) is {self.age} years old and the ID code is {self.id_code}."

    @classmethod
    def create_from_string(cls, sentence):
        name, id_code = sentence.split()
        id_code = int(id_code)
        return cls(name, id_code)

    @staticmethod
    def is_name_correct(name):
        if name[0].isupper() and len(name) >= 3:
            return True
        return False

    @staticmethod
    def is_code_correct(id_code):
        return stdnum.get_cc_module("ee", "ik").is_valid(str(id_code))

    @staticmethod
    def get_birthday(id_code):
        return stdnum.get_cc_module("ee", "ik").get_birth_date(str(id_code))

    @staticmethod
    def get_gender(id_code):
        return stdnum.get_cc_module("ee", "ik").get_gender(str(id_code))

    @staticmethod
    def get_age(id_code):
        birthday = stdnum.get_cc_module("ee", "ik").get_birth_date(str(id_code))
        today = datetime.date.today()
        age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
        return age


class Student(Person):
    def __init__(self, name, id_code, scholarship):
        Person.__init__(self, name, id_code)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship

    def __str__(self):
        return super().__str__() + f" Their scholarship is ${self.scholarship}"

    @classmethod
    def create_from_string(cls, sentence):
        name, id_code, scholarship = sentence.split()
        scholarship, id_code = float(scholarship), int(id_code)
        return cls(name, id_code, scholarship)


stud1 = Student("Margaret", 49403136526, 0)
stud2 = Student.create_from_string("Max 34501234215 600")
pers1 = Person.create_from_string("Max 34501234215")
print(stud1)
print(stud2.age)
print(stud2)
print(stud1.scholarship)
print(pers1)
print(pers1.birthday)
print(Student.is_name_correct("alice"))
print(Student.get_gender(49403136526))
print(Student.is_code_correct(49403136526))
print(Student.get_birthday(49403136526))
print(Student.get_age(49403136526))

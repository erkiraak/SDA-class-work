from abc import ABC, abstractmethod
"""
Target interface - class Learner
"""


class Learner(ABC):
    @abstractmethod
    def get_full_name(self):
        pass

    @abstractmethod
    def is_adult(self):
        pass

    @abstractmethod
    def get_results(self):
        pass


"""
The old class which we want to adapt
"""


class Student:
    def __init__(self, first_name, last_name, age, email, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.grades = grades

    def __repr__(self):
        return f"{self.first_name} {self.last_name} {self.age} {self.email} {self.grades}"

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_age(self):
        return self.age

    def get_email(self):
        return self.email

    def get_grades(self):
        return self.grades

class StudentAdaper(Learner):
    def __init__(self, old_class):
        self._student = old_class

    def get_full_name(self):
        return self._student.get_first_name() + " " + self._student.get_last_name()

    def is_adult(self):
        return self._student.get_age() >= 18

    def get_results(self):
        return self._student.get_grades()


if __name__ == "__main__":
    learners = [StudentAdaper(Student("John", "Smith", 18, "johnsmith@gmail.com", [90, 80, 70])),
                StudentAdaper(Student("Jane", "Doe", 19, "janedoe@fgasd.com", [80, 70, 60])),
                StudentAdaper(Student("Jack", "Black", 20, "jackva@fassa.ede", [70, 60, 50]))]
    for learner in learners:
        print(learner.get_full_name() + " " + str(learner.is_adult()) + " " + str(learner.get_results()))

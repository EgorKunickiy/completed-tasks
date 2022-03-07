"""Answer to the question: inheritance, polymorphism, encapsulation"""


class Student:
    def __init__(self, name):
        self.__name = name


class EducationalInstitution:
    def __init__(self, list_st):
        self.__list_of_students = list_st

    @property
    def list_of_students(self):
        return self.__list_of_students

    @list_of_students.setter
    def list_of_students(self, value):
        self.__list_of_students = value


class School(EducationalInstitution):
    def __init__(self, list_student):
        super().__init__(list_student)


class University(EducationalInstitution):
    def __init__(self, list_student):
        super().__init__(list_student)


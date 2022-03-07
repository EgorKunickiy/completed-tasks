"""Answer to the question: inheritance, association, encapsulation"""


class Student:
    def __init__(self, name: str):
        self.__name: str = name


class EducationalInstitution:
    def __init__(self, list_st: list):
        self.__list_of_students: list = list_st

    @property
    def list_of_students(self):
        return self.__list_of_students

    @list_of_students.setter
    def list_of_students(self, value):
        self.__list_of_students = value


class School(EducationalInstitution):
    def __init__(self, list_student: list):
        super().__init__(list_student)


class University(EducationalInstitution):
    def __init__(self, list_student: list):
        super().__init__(list_student)


if __name__ == '__main__':
    student1 = Student('Anna')
    student2 = Student('Dima')
    student3 = Student('Egor')
    list_of_students = [student1, student2, student3]
    school = School(list_of_students)
    university = University(list_of_students)
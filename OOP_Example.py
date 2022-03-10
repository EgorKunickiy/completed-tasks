"""1 Answer to the question: inheritance, association, encapsulation"""
"""2 Answer to the question: polymorphism"""
"""3 Answer to the question: overload"""


class Student:
    def __init__(self, name: str):
        self.__name: str = name

    def __str__(self):
        return f'{self.__name}'

    def __repr__(self):
        return f'{self.__name}'

class EducationalInstitution:
    def __init__(self, list_st: list):
        self.__list_of_students: list = list_st

    @property
    def list_of_students(self):
        return self.__list_of_students

    @list_of_students.setter
    def list_of_students(self, value):
        self.__list_of_students = value

    def __str__(self):
        return f'{self.list_of_students}'

    def __add__(self, other: 'EducationalInstitution'):
        pass


class School(EducationalInstitution):
    def __init__(self, list_student: list):
        super().__init__(list_student)

    def __add__(self, other):
        if isinstance(other, School):
            return University(self.list_of_students + other.list_of_students)
        else:
            return None


class University(EducationalInstitution):
    def __init__(self, list_student: list):
        super().__init__(list_student)

    def __add__(self, other):
        if isinstance(other, University):
            return University(self.list_of_students + other.list_of_students)
        else:
            return None

def add(obj_1: EducationalInstitution, obj_2: EducationalInstitution):
    res = obj_1.list_of_students + obj_2.list_of_students
    return University(res)


if __name__ == '__main__':
    student1 = Student('Anna')
    student2 = Student('Dima')
    student3 = Student('Egor')
    list_of_students = [student1, student2, student3]
    school = School(list_of_students)
    university = University(list_of_students)
    university2 = University(list_of_students)
    print(add(university, university2))
    print(university + university2)
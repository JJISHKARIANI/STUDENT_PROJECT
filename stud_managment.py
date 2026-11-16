from students import Student
import json

class StudentManagemnt:
    def __init__(self, filename : str = "students_list.json") -> None:
        self.filename = filename
        self.__student: dict[int, Student] = {}
        self.load_from_file()











    def add_student(self, name: str, roll_number: int, grade: float) -> None:
        if roll_number in self.__student:
            raise ValueError('student is in list')
 #None anu arafers abrunebs       
        student = Student(name, roll_number, grade)
        self.__student[roll_number] = student
        print(f'successfully added {name}')

    def search_student(self, roll_number: int) -> Student:
        if roll_number not in self.__student:
            raise ValueError('student not in list')
        return self.__student[roll_number]

    def update_student(self, roll_number: int, new_name: str = None, new_grade: float = None) -> None:
        student = self.search_student(roll_number)
#aq new_name : str = None da new_ grade
        if new_name is not None:
            student.name = new_name
        if new_grade is not None:
            student.grade = new_grade

        print('student is updated')

    def delete_student(self, roll_number: int) -> None:
        if roll_number not in self.__student:
            raise ValueError("student not in list")
        
        del self.__student[roll_number]
        print(f"# {roll_number} student deleted")

    def display_all_student(self) -> None:
        if not self.__student:
            print('there is no students')
            return

        for student in self.__student.values():
            print(student)

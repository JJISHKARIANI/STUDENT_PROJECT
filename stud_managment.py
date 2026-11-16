from students import Student
import json

class StudentManagemnt:
    def __init__(self) -> None:
        self.__student: dict[int, Student] = {}
        self.load_from_file()
        # chartvistanave programis rom daiwyos failidan monacemebis wakitxbas
     
    def save_file(self):
        data = []
        for i in self.__student.values():
            data.append({
                "name": i.name,
                "roll_number": i.roll_number,
                "grade": i.grade
          })

        with open("students_list.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4) 
# leqsikonis saxit sias vwert  json fileshi
    def load_from_file(self):
        try:
            with open("students_list.json", "r", encoding="utf-8") as file:
                data = json.load(file) 
                for i in data:
                    s = Student(i["name"], i["roll_number"], i["grade"])
                    self.__student[s.roll_number] = s
        except FileNotFoundError:
            pass
                #tu file ar aris  daerorebs   
# vkitxulobt files da  titoueil arsebuli elementidan vqmnit isev obieqts da  memoryshi vabrunebt, pass tu pirvelad vrtav programas
# da ar arsebobs file ar daaerorebs
    def add_student(self, name: str, roll_number: int, grade: float) -> None:
        if roll_number in self.__student:
            raise ValueError('student is in list')
 #None anu arafers abrunebs       
        student = Student(name, roll_number, grade)
        self.__student[roll_number] = student
        self.save_file()
        print(f'successfully added {name}')
# shevinaxet json fileshic
    def search_student(self, roll_number: int) -> Student:
        if roll_number not in self.__student:
            raise ValueError('student not in list')
        return self.__student[roll_number]

    def update_student(self, roll_number: int, new_name: str = None, new_grade: float = None) -> None:
        student = self.search_student(roll_number)
#aq new_name : str = None da new_ grade : str = None aris optional tuginda sheucvli tuarada datoveb cariels da problema ar warmoiqmeneba
        if new_name is not None:
            student.name = new_name
        if new_grade is not None:
            student.grade = new_grade
# tu shemova axali saxeli, grade gadaecema new grade, new name
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

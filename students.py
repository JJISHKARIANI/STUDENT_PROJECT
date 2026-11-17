class Student:
    def __init__(self, name: str, roll_number: int, grade: float):
        self.__name = name
        self.__roll_number = roll_number
        self.__grade = grade
# private encapsulating ს ვიყენებთ მონაცემების  დაცვისათვის(გარე ჩარევიზგან), პროპერთი დეკორატორის 
# დახმარებით  ატრიბუტებად გამოძახება შეგვიძლია.
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip(): 
            raise ValueError("name cannot be space")
        self.__name = value
# strip სპეისებს წაშლის ,რადგან კოდში სპეის True არის და ველიუ ერორი ვერ დაიჭერს. 
    @property
    def roll_number(self) -> int:
        return self.__roll_number

    @property
    def grade(self) -> float:
        return self.__grade

    @grade.setter
    def grade(self, value: float):
        if not (0.0 <= value <= 100.0):
            raise ValueError(" grade must be number from 0.0 to 100.0")
        self.__grade = value
# gamoviyene chained shedareba . pirdapir  dauardeba(not)  frchxilebshi mocemuli piroba da if sheamowmebs
    def __repr__(self) -> str:
        return f"student(name={self.__name}, roll_number={self.__roll_number}, grade={self.__grade})"
# იწერება დეველოპერისთვის
    def __str__(self) -> str:
        return f"Student: name: {self.__name}, roll_number: {self.__roll_number}, grade: {self.__grade}"
# იწერება მომხმარებლისთვის რომ ლამაზად გამოჩნდეს კოდი.
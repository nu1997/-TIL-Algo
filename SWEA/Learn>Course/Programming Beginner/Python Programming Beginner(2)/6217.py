class Student:
    def __init__(self, name):
        self.name = name
    def show_info(self):
        print(f'이름: {self.name}')

class GraduateStudent(Student):
    def __init__(self, name, major):
        self.name = name
        self.major = major
    def show_info(self):
        print(f'이름: {self.name}, 전공: {self.major}')

s1 = Student('홍길동')
s2 = GraduateStudent('이순신', '컴퓨터')

s1.show_info()
s2.show_info()


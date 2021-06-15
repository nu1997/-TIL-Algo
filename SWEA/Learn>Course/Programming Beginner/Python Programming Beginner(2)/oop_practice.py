class Student:
    def __init__(self, name, gender, height):
        self.__name = name
        self.__gender = gender
        self.__height = height

    @property
    def name(self):
        return self.__name
    
    @property
    def gender(self):
        return self.__gender

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        self.__height = height

    def __repr__(self):
        return "{0}(name: {1}, gender:{2}, height: {3}) ".format(self.__class__.__name__, self.name, self.gender, self.height)

students = [
    Student("홍길동", "남", 176.5),
    Student("이순신", "남", 188.5), 
    Student("유관순", "여", 158.4), 
    Student("강감찬", "남", 182.2)
]

for student in students:
    print(student)
print('====')
for student in sorted(students, key=lambda x: x.name, reverse=False):
    print(student)
print('====')
for student in sorted(students, key=lambda x: x.height, reverse=True):
    print(student)
print('====')

#### 
# 일단 게터, 세터 뭔지 모르겠고
# 프라이빗 어쩌구 객체 메서드 다 모르겟다... 내가 머리가 나빠서 미안해.... 
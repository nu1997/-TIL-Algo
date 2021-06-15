class Student:
    def __init__(self, kor, eng, mat):
        self.kor = kor
        self.eng = eng
        self.mat = mat

    def total(self):
        self.total = self.kor + self.eng + self.mat
        print(f'국어, 영어, 수학의 총점: {self.total}')

kr, eg, mt = map(int, input().split(', '))
s1 = Student(kr, eg, mt)
s1.total()
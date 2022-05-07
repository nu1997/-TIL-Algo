class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        area = self.length ** 2
        print(f'정사각형의 면적: {area}')

s1 = Square(3)
s1.area()
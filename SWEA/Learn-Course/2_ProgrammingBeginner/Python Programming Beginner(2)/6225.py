class Rectangle:
    def __init__(self, h, v):
        self.h = h
        self.v = v

    def get_area(self):
        area = self.h * self.v
        print(f'사각형의 면적: {area}')

r1 = Rectangle(4, 5)
r1.get_area()
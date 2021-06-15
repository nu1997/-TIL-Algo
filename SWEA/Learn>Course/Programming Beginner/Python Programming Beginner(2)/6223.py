class Circle:
    def __init__(self, r):
        self.r = r

    def calc_circle(self):
        pi = 3.14
        area = self.r ** 2 * pi
        print(f'원의 면적: {area}')

r1 = Circle(2)
r1.calc_circle()

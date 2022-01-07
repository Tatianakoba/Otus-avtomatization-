from Figure import Figure


class Rectangle(Figure):
    name = 'Rectangle'
    area = None
    perimeter = None

    def __init__(self, a, b):
        self.area = a*b
        self.perimeter = (a+b)*2
        # print(self.area)
        # print(self.perimeter)

s = Rectangle(5,7)
from Figure import Figure


class Circle(Figure):
    name = 'Circle'
    area = None
    perimeter = None

    def __init__(self, r):
        P = 3.14
        self.area = P*r*r
        self.perimeter = 2*r*P
        # print(self.area)
        # print(self.perimeter)

s = Circle(10)

from Figure import Figure


class Triangle(Figure):
    name = 'Triangle'
    area = None
    perimeter = None

    def __init__(self, a, b, c):
        p = (a+b+c)/2 # Полупериметр для площади
        self.area = (p*(p-a)*(p-b)*(p-c))**0.5
        self.perimeter = a+b+c
        # print(p)
        # print(self.area)
        # print(self.perimeter)

s = Triangle(10,12,5)


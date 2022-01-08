from Figure import Figure


class Square(Figure):
    name = 'Square'
    area = None
    perimeter = None

    def __init__(self, a):
        self.area = a*a
        self.perimeter = a*4


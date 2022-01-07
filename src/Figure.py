class Figure:
    name = None
    area = None
    perimeter = None

    def add_area(self, area1):
        if not isinstance(area1, Figure):
            raise ValueError
        sum_area = self.area + area1.area # метод add_area(figure) который принимает другую геометрическую фигуру и возвращает сумму площадей этих фигур.
        print(sum_area)

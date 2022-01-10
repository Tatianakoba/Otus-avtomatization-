class Figure:
    name = None
    area = None
    perimeter = None

    def __new__(cls, *args):
        if cls is Figure:
            return None
        return object.__new__(cls)

    def add_area(self, area1):
        if not isinstance(area1, Figure):
            raise ValueError("Передан неправильный класс")
        sum_area = self.area + area1.area  # метод add_area(figure) который принимает другую геометрическую фигуру
        # и возвращает сумму площадей этих фигур.
        return sum_area

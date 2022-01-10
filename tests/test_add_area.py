import sys
sys.path.insert(0, '../src/')
from src.Triangle import Triangle
from src.Square import Square
from src.Circle import Circle
from src.Rectangle import Rectangle

def test_add_arrea():

    '''Проверка реализации метода add_area(figure)'''
    a = 2
    b = 5
    c = 4
    r = 3

    t = Triangle(a, b, c)

    s = Square(a)

    cir = Circle(r)

    rec = Rectangle(a, b)

    assert t.add_area(s) == t.area + s.area
    assert s.add_area(cir) == s.area + cir.area
    assert cir.add_area(rec) == cir.area + rec.area
    assert rec.add_area(t) == rec.area + t.area


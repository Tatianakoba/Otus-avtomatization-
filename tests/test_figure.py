import sys
sys.path.insert(0, '../src/')
from src.Triangle import Triangle
from src.Square import Square
from src.Circle import Circle
from src.Rectangle import Rectangle

def test_atr_figure():

    '''Проверка наличия артибутов name, area,perimeter у каждой фигуры'''
    a = 2
    b = 5
    c = 4
    r = 3

    t = Triangle(a, b, c)
    p = (a + b + c) / 2
    assert t.name == 'Triangle'
    assert t.area == (p*(p-a)*(p-b)*(p-c))**0.5
    assert t.perimeter == a+b+c

    s = Square(a)
    assert s.name == 'Square'
    assert s.area == a*a
    assert s.perimeter == a*4

    rec = Rectangle(a, b)
    assert rec.name == 'Rectangle'
    assert rec.area == a*b
    assert rec.perimeter == (a+b)*2

    cir = Circle(r)
    P = 3.14
    assert cir.name == 'Circle'
    assert cir.area == P*r*r
    assert cir.perimeter == 2*r*P

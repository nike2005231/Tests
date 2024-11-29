import sys
import pytest
sys.path.append(r'C:\Users\Nike\Desktop\Scripts\Python\Testing\Prog\ex1.py')
from ex1 import *

def test_1():
    assert triangle("a", 3, 4) == "Ошибка неправильные параметры функции"

def test_2():
    assert triangle(3, 4, 5) == ('Разносторонний', 'Прямоугольный', 'Площадь треугольника = 6.0')

def test_3():
    assert triangle(3, 4, 6) == ('Разносторонний', 'Тупоугольный', 'Площадь треугольника = 5.332682251925386')

def test_4():
    assert triangle(5, 6, 7) == ("Разносторонний", "Остроугольный", "Площадь треугольника = 14.696938456699069")

def test_5():
    assert triangle(1, 2, 4) == "Треугольник с такими сторонами не существует"

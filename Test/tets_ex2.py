import sys
import pytest
sys.path.append(r'C:\Users\Nike\Desktop\Scripts\Python\Testing\Prog')
from practic_1 import Ex1, Ex2, winner_Ex2, Ex3

def test_play_func_par():
    assert Ex1("asd", 12, False) == "Введены недопустимые значения"

def test_Var_1():
    assert Ex1(2, 2, 2) == "Несколько детей нашли одинаковое кол-во грибов"
    
def test_Var_2():
    assert Ex1(2, 1, 0) == "Children_1 - нашел больше всего грибов - 2, Всего найденно - 3"

def test_Var_3():
    assert Ex1(-2, 1, 0) == "Значение отрицательное, кто-то потерял все грибы!!!"

def test_Var_4():
    assert Ex1(1, 0) == "Недостаточно детей"


def test_winner_Ex2():
    Andrey = Ex2(80, 25, 12, "Andrey")
    Egor = Ex2(75, 30, 11, "Egor")
    Petya = Ex2(70, 35, 15, "Petya")

    result = winner_Ex2()

    assert "Победитель" in result
    assert "временем" in result
    assert "Andrey" in result or "Egor" in result or "Petya" in result

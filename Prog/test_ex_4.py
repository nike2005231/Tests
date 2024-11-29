class Сalculating_rectangle():
    def __init__(self, x: int, y: int):
        if x <= 0 or y <= 0:
            raise ValueError(f"x = {x} или y = {y} не могут быть <= 0")
        self.x = x
        self.y = y
    
    def Сalculating(self):
        S = self.x * self.y
        return S


# def test_calculating_1():
#     assert Сalculating_rectangle(10, 5).Сalculating() == 50
#     assert Сalculating_rectangle(2, 10).Сalculating() == 20
#     assert Сalculating_rectangle(3, 3).Сalculating() == 9

# def test_calculating_2():
#     try:
#         Сalculating_rectangle(10, 0).Сalculating()
#     except ValueError as e:
#         assert str(e) == "x = 10 или y = 0 не могут быть <= 0"

#     try:
#         Сalculating_rectangle(2, -1).Сalculating()
#     except ValueError as e:
#         assert str(e) == "x = 2 или y = -1 не могут быть <= 0"

#     try:
#         Сalculating_rectangle(-2, 3).Сalculating()
#     except ValueError as e:
#         assert str(e) == "x = -2 или y = 3 не могут быть <= 0"

class Cylinder_opening():
    def __init__(self, r: int, h: int):
        if r <= 0 or h <= 0:
            raise ValueError(f"r = {r} или h = {h} не могут быть <= 0")
        self.r = r
        self.h = h

    def Сalculating(self):
        V = (3.14 * self.r ** 2) * self.h #Не особо уверен по поводу формулы но вроде V = ПR^2*h
        return round(V)

# calc_1 = Cylinder_opening(4, 1)
# print(calc_1.Сalculating())

def test_calculating_1():
    assert Cylinder_opening(2, 1).Сalculating() == 13
    assert Cylinder_opening(7, 7).Сalculating() == 1077
    assert Cylinder_opening(4, 1).Сalculating() == 50

def test_calculating_2():
    try:
        Cylinder_opening(2, 0).Сalculating()
    except ValueError as e:
        assert str(e) == "r = 2 или h = 0 не могут быть <= 0"

    try:
        Cylinder_opening(7, -1).Сalculating()
    except ValueError as e:
        assert str(e) == "r = 7 или h = -1 не могут быть <= 0"

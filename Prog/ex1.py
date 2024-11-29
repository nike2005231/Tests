import math

def triangle(x, y, z):
    view = ""
    view_type = "" 
    P = 0 
    S = 0 
    
    if x == str(x) or y == str(y) or z == str(z):
        return "Ошибка неправильные параметры функции"

    if x**2 + y**2 == z**2 or x**2 + z**2 == y**2 or y**2 + z**2 == x**2:
        view_type = "Прямоугольный"
    elif x**2 + y**2 < z**2 or x**2 + z**2 < y**2 or y**2 + z**2 < x**2:
        view_type = "Тупоугольный"
    else:
        view_type = "Остроугольный"

    def num_math(x, y, z):
        P = (x + y + z) / 2
        S = math.sqrt(P*(P-x)*(P-y)*(P-z))
        return f"Площадь треугольника = {S}"

    if x + y <= z or x + z <= y or y + z <= x:
        return "Треугольник с такими сторонами не существует"

    elif x == y == z:
        view = "Равносторонний"
        return view, view_type, num_math(x, y, z)

    elif x == y and x != z or z == x and z != y or z == y and z != x:
        view = "Равнобедренный"
        return view, view_type, num_math(x, y, z)

    elif x != y != z:
        view = "Разносторонний"
        return view, view_type, num_math(x, y, z)
    
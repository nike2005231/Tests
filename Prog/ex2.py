def Ex1(*args):

    lst_chil = list(args)

    all_mus = 0 #Всего
    max_mus = 0 #макс кол-во одной находки
    Who = [] #кто нашел больше всего

    if len(lst_chil) < 3:
        return "Недостаточно детей"
        
    if len(set(lst_chil)) < len(lst_chil):
        return "Несколько детей нашли одинаковое кол-во грибов"

    if any(x < 0 for x in lst_chil):
        return "Значение отрицательное, кто-то потерял все грибы!!!"

    else:
        all_mus = sum(lst_chil)
        max_mus = max(lst_chil)
        for x in lst_chil:
            if x == max_mus:
                Who.append(lst_chil.index(x))
            else:
                ...

        return f"Children_{Who[0] + 1} - нашел больше всего грибов - {max_mus}, Всего найденно - {all_mus}"

#swimming 1500m basicl 40km run 10km
class Ex2():
    swim_win = 1500 
    basic_win = 40
    run_win = 10

    def __init__(self, speed_swim = 1, speed_basic = 1, speed_run = 1, name = "x"):
        self.speed_swim = speed_swim
        self.speed_basic = speed_basic
        self.speed_run = speed_run
        self.name = name

    def time(self):
        time_swim = self.swim_win / self.speed_swim  
        time_basic = (self.basic_win / self.speed_basic) * 60 
        time_run = (self.run_win / self.speed_run)  * 60
        all_time = time_swim + time_basic + time_run
        return all_time
    
        
Andrey, Egor, Petya = Ex2(80, 25, 12, "Andrey"), Ex2(75, 30, 11, "Egor"), Ex2(70, 35, 15, "Petya")

def winner_Ex2():
    participants = {"Andrey": Andrey.time(), "Egor": Egor.time(), "Petya": Petya.time()}
    winner_name = min(participants, key=participants.get)
    return f"Победитель {winner_name} со временем - {participants[winner_name]}"


def Ex3():
    lst = input("Напишите числа через пробел:\n").split()
    lst = list(map(int, lst))
    summ = sum(lst)
    prod = 0
    for x in range(len(lst) - 1):
        prod += lst[x] * lst[x + 1]
    maximum = max(lst)
    minimum = min(lst)
    mode = int(input("Выберите режим, введите число: \n1 - Сумма \n2 - Умножение \n3 - Максимум \n4 - Минимум:\n"))
    match mode:
        case 1:
            return summ
        case 2:
            return prod
        case 3:
            return maximum
        case 4:
            return minimum
        case _:
            return "Ошибка: недопустимый режим"
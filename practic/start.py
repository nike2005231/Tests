import main_window
import window_log
import sys
import time
from threading import Thread

#Обращаемся к main
app_main = main_window.QtWidgets.QApplication(sys.argv)
MainWindow_main = main_window.QtWidgets.QMainWindow()
ui_main = main_window.Ui_MainWindow()
ui_main.setupUi(MainWindow_main)

#Обращаемся к log
app_log = window_log.QtWidgets.QApplication(sys.argv)
MainWindow_log = window_log.QtWidgets.QMainWindow()
ui_log = window_log.Ui_MainWindow()
ui_log.setupUi(MainWindow_log)

list_exept = [
    ui_main.quest_1,
    ui_main.quest_2,
    ui_main.quest_3,
    ui_main.quest_4
]

list_text_edit = [
    ui_main.textEdit,
    ui_main.textEdit_2,
    ui_main.textEdit_3,
    ui_main.textEdit_4
]

list_answer = []
list_answer_people = []

time_max = int(input("Установите максимальное время в секундах\n"))

for x in list_exept:
    x.setText(input("Введите вопрос:\n"))
    list_answer.append(input("Введите ответ:\n"))

flag_time = False

def timer():
    global time_max, flag_time
    while time_max > 0:
        time.sleep(1)
        time_max -= 1
        ui_main.time.setText(str(time_max))
    if time_max == 0:
        flag_time = True
        print("Время вышло")
Thread(target=timer).start()

MainWindow_main.show()



def func_heandler():
    global list_answer_people
    global list_answer, flag_time
    if flag_time == False:
        list_answer_people = []
        for x in list_text_edit:
            list_answer_people.append(str(x.toPlainText()))

        var_req = []

        for x in range(4):
            if str(list_answer[x]) == str(list_answer_people[x]):
                var_req.append("Верен")
            else:
                var_req.append("Не верен")

        for x in range(4):
            ui_log.textBrowser.append(f"<p>Задача {x + 1} Ответ - <b>{var_req[x]}</b> Ваш ответ: {list_answer_people[x]}, Правильный ответ: {list_answer[x]}</p>")
        MainWindow_log.show()
        MainWindow_main.close()
    else:
        list_answer_people = []
        for x in list_text_edit:
            list_answer_people.append(str(x.toPlainText()))

        var_req = []

        for x in range(4):
            if str(list_answer[x]) == str(list_answer_people[x]):
                var_req.append("Верен")
            else:
                var_req.append("Не верен")
        ui_log.textBrowser.append("ВРЕМЯ ВЫШЛО ОТВЕТЫ НЕ ВАЛИДНЫ")
        for x in range(4):
            ui_log.textBrowser.append(f"<p>Задача {x + 1} Ответ - <b>{var_req[x]}</b> Ваш ответ: {list_answer_people[x]}, Правильный ответ: {list_answer[x]}</p>")
        MainWindow_log.show()
        MainWindow_main.close()



ui_main.pushButton.clicked.connect(func_heandler)
app_main.exec_()

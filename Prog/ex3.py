from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(411, 380)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_output = QtWidgets.QLabel(self.centralwidget)
        self.label_output.setGeometry(QtCore.QRect(3, 5, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_output.setFont(font)
        self.label_output.setScaledContents(False)
        self.label_output.setObjectName("label_output")
        self.btn_equl = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equl.setGeometry(QtCore.QRect(0, 260, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_equl.setFont(font)
        self.btn_equl.setObjectName("btn_equl")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 50, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_1.setFont(font)
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(110, 50, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_2.setFont(font)
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(220, 50, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_3.setFont(font)
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 120, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_4.setFont(font)
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(110, 120, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_5.setFont(font)
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(220, 120, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_6.setFont(font)
        self.btn_6.setObjectName("btn_6")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 190, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_7.setFont(font)
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(110, 190, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_8.setFont(font)
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(220, 190, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_9.setFont(font)
        self.btn_9.setObjectName("btn_9")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(110, 260, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_0.setFont(font)
        self.btn_0.setObjectName("btn_0")
        self.btn_Clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Clear.setGeometry(QtCore.QRect(220, 260, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_Clear.setFont(font)
        self.btn_Clear.setObjectName("btn_Clear")
        self.btn_sum = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sum.setGeometry(QtCore.QRect(340, 50, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_sum.setFont(font)
        self.btn_sum.setObjectName("btn_sum")
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(340, 120, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_minus.setFont(font)
        self.btn_minus.setObjectName("btn_minus")
        self.btn_division = QtWidgets.QPushButton(self.centralwidget)
        self.btn_division.setGeometry(QtCore.QRect(340, 190, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_division.setFont(font)
        self.btn_division.setObjectName("btn_division")
        self.btn_multiplication = QtWidgets.QPushButton(self.centralwidget)
        self.btn_multiplication.setGeometry(QtCore.QRect(340, 260, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.btn_multiplication.setFont(font)
        self.btn_multiplication.setObjectName("btn_multiplication")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 411, 26))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.btn_0.clicked.connect(self.func_click_but_0)
        self.btn_1.clicked.connect(self.func_click_but_1)
        self.btn_2.clicked.connect(self.func_click_but_2)
        self.btn_3.clicked.connect(self.func_click_but_3)
        self.btn_4.clicked.connect(self.func_click_but_4)
        self.btn_5.clicked.connect(self.func_click_but_5)
        self.btn_6.clicked.connect(self.func_click_but_6)
        self.btn_7.clicked.connect(self.func_click_but_7)
        self.btn_8.clicked.connect(self.func_click_but_8)
        self.btn_9.clicked.connect(self.func_click_but_9)
        self.btn_Clear.clicked.connect(self.func_click_but_Clear)
        self.btn_division.clicked.connect(self.func_click_but_division)
        self.btn_sum.clicked.connect(self.func_click_but_sum)
        self.btn_minus.clicked.connect(self.func_click_but_minus)
        self.btn_equl.clicked.connect(self.func_click_but_equl)
        self.btn_multiplication.clicked.connect(self.func_click_but_multiplication)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)


    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.label_output.setText(_translate("mainWindow", ""))
        self.btn_equl.setText(_translate("mainWindow", "="))
        self.btn_1.setText(_translate("mainWindow", "1"))
        self.btn_2.setText(_translate("mainWindow", "2"))
        self.btn_3.setText(_translate("mainWindow", "3"))
        self.btn_4.setText(_translate("mainWindow", "4"))
        self.btn_5.setText(_translate("mainWindow", "5"))
        self.btn_6.setText(_translate("mainWindow", "6"))
        self.btn_7.setText(_translate("mainWindow", "7"))
        self.btn_8.setText(_translate("mainWindow", "8"))
        self.btn_9.setText(_translate("mainWindow", "9"))
        self.btn_0.setText(_translate("mainWindow", "0"))
        self.btn_Clear.setText(_translate("mainWindow", "Clear"))
        self.btn_sum.setText(_translate("mainWindow", "+"))
        self.btn_minus.setText(_translate("mainWindow", "-"))
        self.btn_division.setText(_translate("mainWindow", "/"))
        self.btn_multiplication.setText(_translate("mainWindow", "*"))


    def func_click_but_0(self):
        self.label_output.setText(self.label_output.text() + self.btn_0.text())
    def func_click_but_1(self):
        self.label_output.setText(self.label_output.text() + self.btn_1.text())
    def func_click_but_2(self):
        self.label_output.setText(self.label_output.text() + self.btn_2.text())
    def func_click_but_3(self):
        self.label_output.setText(self.label_output.text() + self.btn_3.text())
    def func_click_but_4(self):
        self.label_output.setText(self.label_output.text() + self.btn_4.text())
    def func_click_but_5(self):
        self.label_output.setText(self.label_output.text() + self.btn_5.text())
    def func_click_but_6(self):
        self.label_output.setText(self.label_output.text() + self.btn_6.text())
    def func_click_but_7(self):
        self.label_output.setText(self.label_output.text() + self.btn_7.text())
    def func_click_but_8(self):
        self.label_output.setText(self.label_output.text() + self.btn_8.text())
    def func_click_but_9(self):
        self.label_output.setText(self.label_output.text() + self.btn_9.text())

    def func_click_but_sum(self):
        self.label_output.setText(self.label_output.text() + self.btn_sum.text())
    def func_click_but_Clear(self):
        self.label_output.setText("")
    def func_click_but_division(self):
        self.label_output.setText(self.label_output.text() + self.btn_division.text())
    def func_click_but_minus(self):
        self.label_output.setText(self.label_output.text() + self.btn_minus.text())
    def func_click_but_equl(self):
        try:
            self.label_output.setText(str(eval(self.label_output.text())))
        except:
            self.label_output.setText("Введены некоректные данные")
    def func_click_but_multiplication(self):
        self.label_output.setText(self.label_output.text() + self.btn_multiplication.text())



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
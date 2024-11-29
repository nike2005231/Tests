import sys
import pytest
sys.path.append(r'C:\Users\Nike\Desktop\Scripts\Python\Testing\Prog')
from ex3 import *

def test_retranslateUi():
    mainWindow = MainWindow()

    expected_window_title = "MainWindow"
    mainWindow.retranslateUi(mainWindow)
    assert mainWindow.windowTitle() == expected_window_title

    expected_label_text = ""
    assert mainWindow.label_output.text() == expected_label_text

    expected_btn_text = "="
    assert mainWindow.btn_equl.text() == expected_btn_text


def test_func_click_but_0():
    mainWindow = MainWindow()

    mainWindow.func_click_but_0()
    assert mainWindow.label_output.text() == "0"

def test_func_click_but_1():
    mainWindow = MainWindow()

    mainWindow.func_click_but_1()
    assert mainWindow.label_output.text() == "1"


def test_func_click_but_sum():
    mainWindow = MainWindow()

    mainWindow.label_output.setText("42")

    mainWindow.func_click_but_sum()
    assert mainWindow.label_output.text() == "42+"


def test_func_click_but_equl():
    mainWindow = MainWindow()

   
    mainWindow.label_output.setText("2+2")
    mainWindow.func_click_but_equl()
    assert mainWindow.label_output.text() == "4"


    mainWindow.label_output.setText("2+*2")
    mainWindow.func_click_but_equl()
    assert mainWindow.label_output.text() == "Введены некоректные данные"

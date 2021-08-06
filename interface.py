import tkinter as tk
import importlib
from tkinter import filedialog, Text
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
hallmark = importlib.import_module('hallmark')


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(513, 306)
        main_window.setStyleSheet("QWidget#centralwidget{\n"
"background-image: url(c:/Users/awilm/Desktop/Workspaces/PyCharm Workspace/HallmarkMovieBingo/icons/background.jpg);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.button_create = QtWidgets.QPushButton(self.centralwidget)
        self.button_create.setGeometry(QtCore.QRect(90, 180, 91, 31))
        self.button_create.setStyleSheet("border-radius: 12px;\n"
"selection-background-color: rgb(0, 170, 255);\n"
"selection-color: rgb(0, 170, 255);\n"
"font: 9pt \"Segoe UI Semibold\";\n"
"background-color: rgb(0, 255, 255)")
        self.button_create.setObjectName("button_create")
        self.button_print = QtWidgets.QPushButton(self.centralwidget)
        self.button_print.setGeometry(QtCore.QRect(200, 180, 91, 31))
        self.button_print.setStyleSheet("border-radius: 12px;\n"
"font: 9pt \"Segoe UI Semibold\";\n"
"background-color: rgb(0, 255, 255)")
        self.button_print.setObjectName("button_print")
        self.button_quit = QtWidgets.QPushButton(self.centralwidget)
        self.button_quit.setGeometry(QtCore.QRect(310, 180, 91, 31))
        self.button_quit.setStyleSheet("border-radius: 12px;\n"
"font: 9pt \"Segoe UI Semibold\";\n"
"background-color: rgb(0, 255, 255)")
        self.button_quit.setObjectName("button_quit")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(70, 20, 391, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 87 25pt \"Segoe UI Black\";\n"
"text-shadow: #000 0px 0px 1px,   #000 0px 0px 1px,   #000 0px 0px 1px,\n"
"             #000 0px 0px 1px,   #000 0px 0px 1px,   #000 0px 0px 1px;")
        self.label_title.setObjectName("label_title")
        self.player_count_input = QtWidgets.QLineEdit(self.centralwidget)
        self.player_count_input.setGeometry(QtCore.QRect(220, 140, 51, 20))
        self.player_count_input.setStyleSheet("font: 9pt \"Segoe UI Semibold\";")
        self.player_count_input.setObjectName("player_count_input")
        self.label_input = QtWidgets.QLabel(self.centralwidget)
        self.label_input.setGeometry(QtCore.QRect(140, 110, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_input.setFont(font)
        self.label_input.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_input.setObjectName("label_input")
        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Bingo Creator"))
        self.button_create.setText(_translate("main_window", "Create Boards"))
        self.button_print.setText(_translate("main_window", "Print Boards"))
        self.button_quit.setText(_translate("main_window", "Quit"))
        self.label_title.setText(_translate("main_window", "Hallmark Movie Bingo!"))
        self.label_input.setText(_translate("main_window", "Enter the number of players"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())

'''TK implementation'''
# root = tk.Tk()
# # def run_board_builder():
# #     hallmark.remove_and_create_boards(5)
# canvas = tk.Canvas(root, height=700, width=900, bg="#263d42")
# canvas.pack()
# frame = tk.Frame(root, bg="white")
# frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
# player_input = tk.Entry(frame)
# player_input.pack()
# ok_button = tk.Button(frame, text="OK", padx=10, pady=5, fg="white", bg="#263d42", command=lambda: hallmark.remove_and_create_boards(player_input.get()))
# ok_button.pack()
# root.mainloop()



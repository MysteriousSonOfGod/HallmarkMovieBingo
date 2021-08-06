import importlib
from PyQt5 import QtWidgets, QtCore, QtGui
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
        self.button_create.setGeometry(QtCore.QRect(120, 180, 91, 31))
        self.button_create.setStyleSheet("")
        self.button_create.setObjectName("button_create")
        self.button_print = QtWidgets.QPushButton(self.centralwidget)
        self.button_print.setGeometry(QtCore.QRect(280, 180, 91, 31))
        self.button_print.setStyleSheet("")
        self.button_print.setObjectName("button_print")
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
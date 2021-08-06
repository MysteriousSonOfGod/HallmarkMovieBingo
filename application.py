import importlib
from PyQt5 import QtWidgets
import sys

interface = importlib.import_module('interface')
hallmark = importlib.import_module('hallmark')


class Application(interface.Ui_main_window):
    def __init__(self, window):
        self.setupUi(window)
        self.button_create.clicked.connect(lambda: hallmark.remove_and_create_boards(int(self.player_count_input.text())))
        self.button_print.clicked.connect(lambda: hallmark.print_boards())


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = Application(MainWindow)
MainWindow.show()
app.exec_()

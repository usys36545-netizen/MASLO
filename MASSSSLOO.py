from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
import sys
import time
class App(QWidget):

    def __init__(self):
        super().__init__()
        self.start()
        self.ComboBox()
    def start(self):
        self.o = uic.loadUi('MASLO.ui')
        self.o.show()
    def ComboBox(self):
        if self.o.comboBox.activated(2):
            print(2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()
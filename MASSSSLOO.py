from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
import sys

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.start()
        self.ComboBox()
    
    def start(self):
        self.o = uic.loadUi('MASLO.ui')
        self.o.show()
    
    def ComboBox(self):
        # Подключаем сигнал activated к обработчику
        self.o.comboBox.activated.connect(self.on_combo_activated)
    
    def on_combo_activated(self, index):
        # Проверяем, если выбран элемент с индексом 2
        if index == 2:
            print(2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
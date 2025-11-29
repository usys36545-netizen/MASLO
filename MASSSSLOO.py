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
        
        # Если выбран 'Рис' (индекс 3), изменяем текст label
        if index == 3:  # 'Рис' находится на 4-й позиции (индекс 3)
            self.o.label.setText('это тестовый текст если вы его видите при конечном (релизом) приложении то сообщите разработчику')
            font = self.o.label.font()
            font.setPointSize(20)
            self.o.label.setFont(font)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
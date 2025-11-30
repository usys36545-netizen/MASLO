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
        # Если выбран 'Начало' (индекс 0), изменяем текст label
        if index == 0:  # 'Начало' находится на 1-й позиции (индекс 0)
            self.o.label.setText('Добро пожаловать!\nЭто приложение создано для тех, кто\nтолько начинает свой путь на кухне — или хочет\nосвежить базовые навыки. Здесь вы найдёте понятные\nинструкции, полезные советы и пошаговые рецепты.\nУдачи и приятного аппетита!')
            font = self.o.label.font()
            font.setPointSize(28)
            self.o.label.setFont(font)

        # Если выбран 'Рис' (индекс 3), изменяем текст label
        if index == 3:  # 'Рис' находится на 4-й позиции (индекс 3)
            self.o.label.setText('Это тестовый текст если вы его видите при конечном (релизом)\nприложении то сообщите разработчику')
            font = self.o.label.font()
            font.setPointSize(20)
            self.o.label.setFont(font)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()

    sys.exit(app.exec_())

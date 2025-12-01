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
            self.o.label.setText(
                '<b>Добро пожаловать!</b><br>'
                'Это приложение создано для тех, кто<br>'
                'только начинает свой путь на кухне — или хочет<br>'
                'освежить базовые навыки. Здесь вы найдёте понятные<br>'
                'инструкции, полезные советы и пошаговые рецепты.<br>'
                'Удачи и приятного аппетита!'
            )
            font = self.o.label.font() # Делаем шрифт 28
            font.setPointSize(28)
            self.o.label.setFont(font)

        # Если выбран 'Инвентарь' (индекс 1), изменяем текст label
        if index == 1: # 'Инвентарь' находится на 2-й позиции (индекс 1)
            self.o.label.setText(f'Это тестовый текст если вы его видите при конечном (релизом)\nприложении то сообщите разработчику "Инвентарь"')
            font = self.o.label.font() # Делаем шрифт 20
            font.setPointSize(20)
            self.o.label.setFont(font)

        # Если выбран 'Пельмени' (индекс 2), изменяем текст label
        if index == 2:  # 'Пельмени' находится на 3-й позиции (индекс 2)
            self.o.label.setText(f'Это тестовый текст если вы его видите при конечном (релизом)\nприложении то сообщите разработчику "Пельмени"')
            font = self.o.label.font() # Делаем шрифт 20
            font.setPointSize(20)
            self.o.label.setFont(font)

        # Если выбран 'Рис' (индекс 3), изменяем текст label
        if index == 3:  # 'Рис' находится на 4-й позиции (индекс 3)
            self.o.label.setText(f'Это тестовый текст если вы его видите при конечном (релизом)\nприложении то сообщите разработчику "РИС"')
            font = self.o.label.font() # Делаем шрифт 20
            font.setPointSize(20)
            self.o.label.setFont(font)

        # Если выбран 'Макароны' (индекс 4), изменяем текст label
        if index == 4:  # 'Рис' находится на 5-й позиции (индекс 4)
            self.o.label.setText(f'Это тестовый текст если вы его видите при конечном (релизом)\nприложении то сообщите разработчику "Макароны"')
            font = self.o.label.font() # Делаем шрифт 20
            font.setPointSize(20)
            self.o.label.setFont(font)

        # Если выбран 'Греча' (индекс 5), изменяем текст label
        if index == 5:  # 'Рис' находится на 6-й позиции (индекс 5)
            self.o.label.setText(f'Это тестовый текст если вы его видите при конечном (релизом)\nприложении то сообщите разработчику "Греча"')
            font = self.o.label.font() # Делаем шрифт 20
            font.setPointSize(20)
            self.o.label.setFont(font)

        # Если выбран 'Яички' (индекс 6), изменяем текст label
        if index == 6:  # 'Рис' находится на 5-й позиции (индекс 6)
            self.o.label.setText(f'Это тестовый текст если вы его видите при конечном (релизом)\nприложении то сообщите разработчику "Яички"')
            font = self.o.label.font() # Делаем шрифт 20
            font.setPointSize(20)
            self.o.label.setFont(font)

        # Если выбран 'Глазунья' (индекс 7), изменяем текст label
        if index == 7:  # 'Рис' находится на 6-й позиции (индекс 7)
            self.o.label.setText(f'Это тестовый текст если вы его видите при конечном (релизом)\nприложении то сообщите разработчику "Глазунья"')
            font = self.o.label.font() # Делаем шрифт 20
            font.setPointSize(20)
            self.o.label.setFont(font)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
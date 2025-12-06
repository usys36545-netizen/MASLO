from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
import sys


class App(QWidget):
    """
    Основной класс приложения
    """
    def __init__(self):
        super().__init__()
        self.start()  # Загружаем UI
        self.ComboBox()  # Настраиваем комбобокс
    
    def start(self):
        """
        Загрузка UI из файла
        """
        self.o = uic.loadUi('MASLO.ui')  # Загружаем интерфейс
        self.o.show()  # Показываем окно
    
    def ComboBox(self):
        """
        Настройка комбобокса
        """
        # Подключаем обработчик событий комбобокса
        self.o.comboBox.activated.connect(self.on_combo_activated)
    
    def on_combo_activated(self, index):
        """
        Обработчик событий комбобокса
        """
        if index == 0:  # 'Начало'
            self.o.label.setText(
                '<html><head/><body><p>'
                '<span style=" font-size:28pt; font-weight:600;">Добро пожаловать!</span>'
                '<span style=" font-size:28pt;"><br/>Это приложение создано для тех, кто'
                '<br/>только начинает свой путь на кухне — или хочет'
                '<br/>освежить базовые навыки. Здесь вы найдёте понятные'
                '<br/>инструкции, полезные советы и пошаговые рецепты. </span></p>'
                '<p><span style=" font-size:28pt;">Удачи и приятного аппетита!</span></p>'
                '</body></html>'
            )
            font = self.o.label.font()
            font.setPointSize(28)
            self.o.label.setFont(font)

        elif index == 3:  # 'Рис'
            self.o.label.setText(
                'Это тестовый текст если вы его видите при конечном (релизом)\n'
                'приложении то сообщите разработчику'
            )
            font = self.o.label.font()
            font.setPointSize(20)
            self.o.label.setFont(font)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
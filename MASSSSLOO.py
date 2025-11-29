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
        # Подключаем сигнал clicked чекбокса к обработчику
        self.o.checkBox.clicked.connect(self.toggle_dark_mode)
        # Устанавливаем начальный светлый режим
        self.set_light_mode()
    
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

    def toggle_dark_mode(self):
        if self.o.checkBox.isChecked():
            # Установка темного режима
            self.set_dark_mode()
        else:
            # Установка светлого режима
            self.set_light_mode()

    def set_dark_mode(self):
        # Установка темного режима
        dark_style = """
        QWidget {
            background-color: #2e2e2e;
            color: #ffffff;
        }
        QComboBox {
            background-color: #3e3e3e;
            color: #ffffff;
            border: 1px solid #5e5e5e;
        }
        QCheckBox {
            color: #ffffff;
        }
        QLabel {
            color: #ffffff;
        }
        """
        self.o.setStyleSheet(dark_style)

    def set_light_mode(self):
        # Установка светлого режима
        light_style = """
        QWidget {
            background-color: #f0f0f0;
            color: #000000;
        }
        QComboBox {
            background-color: #ffffff;
            color: #000000;
            border: 1px solid #c0c0c0;
        }
        QCheckBox {
            color: #000000;
        }
        QLabel {
            color: #000000;
        }
        """
        self.o.setStyleSheet(light_style)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
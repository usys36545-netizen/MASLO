# Импортируем необходимые модули из PyQt5
from PyQt5 import uic  # Для загрузки .ui файлов, созданных в Qt Designer
from PyQt5.QtWidgets import QApplication, QWidget  # Основные классы для создания GUI
import sys  # Для работы с аргументами командной строки и завершения программы


class App(QWidget):
    """Основной класс приложения, наследуемый от QWidget."""

    def __init__(self):
        """Инициализация главного окна приложения."""
        super().__init__()  # Вызываем конструктор родительского класса
        self.start()        # Загружаем и отображаем UI
        self.ComboBox()     # Настраиваем взаимодействие с элементами интерфейса

    def start(self):
        """Загружает интерфейс из файла MASLO.ui и отображает его."""
        self.o = uic.loadUi('MASLO.ui')  # Загружаем UI-файл, созданный в Qt Designer
        self.o.show()                    # Отображаем окно

    def ComboBox(self):
        """Настраивает обработчики сигналов для элементов интерфейса."""
        # Подключаем сигнал активации (выбора элемента) в выпадающем списке к обработчику
        self.o.comboBox.activated.connect(self.on_combo_activated)

        # Подключаем сигнал переключения чекбокса (темный режим) к обработчику
        self.o.checkBox.toggled.connect(self.toggle_dark_mode)

        # Флаг для отслеживания текущего состояния темы (светлая/тёмная)
        self.is_dark_mode = False

    def on_combo_activated(self, index):
        """
        Обработчик выбора элемента в comboBox.
        В зависимости от выбранного индекса обновляет текст и шрифт label.
        """
        # 'Начало' — индекс 0
        if index == 0:
            self.o.label.setText(
                '<b>Добро пожаловать!</b><br>'
                'Это приложение создано для тех, кто<br>'
                'только начинает свой путь на кухне — или хочет<br>'
                'освежить базовые навыки. Здесь вы найдёте понятные<br>'
                'инструкции, полезные советы и пошаговые рецепты.<br>'
                'Удачи и приятного аппетита!'
            )
            font = self.o.label.font()
            font.setPointSize(28)      # Устанавливаем крупный шрифт для приветствия
            self.o.label.setFont(font)

        # 'Инвентарь' — индекс 1
        elif index == 1:
            self.o.label.setText('Это тестовый текст если вы его видите при конечном (релизом)\nприложении то сообщите разработчику "Инвентарь"')
            font = self.o.label.font()
            font.setPointSize(20)
            self.o.label.setFont(font)

        # 'Пельмени' — индекс 2
        elif index == 2:
            self.o.label.setText('Это тестовый текст если вы его видите при конечном (релизом)\nприложении то сообщите разработчику "Пельмени"')
            font = self.o.label.font()
            font.setPointSize(20)
            self.o.label.setFont(font)

        # 'Рис' — индекс 3
        elif index == 3:
            self.o.label.setText('Это тестовый текст если вы его видите при конечном (релизом)\nприложении то сообщите разработчику "РИС"')
            font = self.o.label.font()
            font.setPointSize(20)
            self.o.label.setFont(font)

        # 'Макароны' — индекс 4
        elif index == 4:
            self.o.label.setText('Это тестовый текст если вы его видите при конечном (релизом)\nприложении то сообщите разработчику "Макароны"')
            font = self.o.label.font()
            font.setPointSize(20)
            self.o.label.setFont(font)

        # 'Греча' — индекс 5
        elif index == 5:
            self.o.label.setText('Это тестовый текст если вы его видите при конечном (релизом)\nприложении то сообщите разработчику "Греча"')
            font = self.o.label.font()
            font.setPointSize(20)
            self.o.label.setFont(font)

        # 'Яички' — индекс 6
        elif index == 6:
            self.o.label.setText('Это тестовый текст если вы его видите при конечном (релизом)\nприложении то сообщите разработчику "Яички"')
            font = self.o.label.font()
            font.setPointSize(20)
            self.o.label.setFont(font)

        # 'Глазунья' — индекс 7
        elif index == 7:
            self.o.label.setText('Это тестовый текст если вы его видите при конечном (релизом)\nприложении то сообщите разработчику "Глазунья"')
            font = self.o.label.font()
            font.setPointSize(20)
            self.o.label.setFont(font)

        # Примечание: в будущем можно вынести тексты в словарь или отдельный файл,
        # чтобы упростить расширение и поддержку.

    def toggle_dark_mode(self, checked):
        """
        Обработчик переключения темного режима.
        Применяет пользовательский стиль (stylesheet) в зависимости от состояния чекбокса.
        """
        self.is_dark_mode = checked  # Сохраняем текущее состояние

        if checked:
            # Задаём тёмную тему с помощью CSS-подобного стиля
            dark_stylesheet = """
            QDialog {
                background-color: #2b2b2b;
                color: #ffffff;
            }
            QLabel {
                color: #ffffff;
                background-color: #2b2b2b;
            }
            QComboBox {
                background-color: #3c3c3c;
                color: #ffffff;
                border: 1px solid #555555;
                padding: 5px;
            }
            QComboBox QAbstractItemView {
                background-color: #3c3c3c;
                color: #ffffff;
                selection-background-color: #555555;
            }
            QCheckBox {
                color: #ffffff;
            }
            """
            self.o.setStyleSheet(dark_stylesheet)
        else:
            # Сбрасываем стиль, возвращаясь к системной (светлой) теме
            self.o.setStyleSheet("")


# Точка входа в приложение
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Создаём экземпляр QApplication
    ex = App()                    # Создаём и инициализируем главное окно
    sys.exit(app.exec_())         # Запускаем главный цикл обработки событий
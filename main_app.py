"""
Main application module for the cooking guide application.
"""

from PyQt5.QtWidgets import QApplication
import sys
from ui_handler import UIHandler
from config import RECIPE_TEXTS, DARK_STYLESHEET


class CookingGuideApp:
    """Main application class."""
    
    def __init__(self, ui_file_path='MASLO.ui'):
        """Initialize the main application."""
        self.ui_handler = UIHandler(ui_file_path)
        self.is_dark_mode = False
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the UI and connect signals."""
        self.ui_handler.setup_connections(
            self.on_combo_activated,
            self.toggle_dark_mode
        )
        self.ui_handler.show()
        
    def on_combo_activated(self, index):
        """Handle the combo box activation."""
        if index in RECIPE_TEXTS:
            recipe_data = RECIPE_TEXTS[index]
            self.ui_handler.set_label_text(recipe_data['text'], recipe_data['font_size'])
        
    def toggle_dark_mode(self, checked):
        """Handle the dark mode toggle."""
        self.is_dark_mode = checked
        
        if checked:
            self.ui_handler.set_stylesheet(DARK_STYLESHEET)
        else:
            self.ui_handler.reset_stylesheet()


def main():
    """Main entry point of the application."""
    app = QApplication(sys.argv)
    ex = CookingGuideApp()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
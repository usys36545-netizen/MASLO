"""
UI Handler module for the cooking guide application.
Manages the UI elements and their interactions.
"""

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class UIHandler:
    """Handles UI elements and their interactions."""
    
    def __init__(self, ui_file_path):
        """Initialize the UI handler by loading the UI file."""
        self.ui = uic.loadUi(ui_file_path)
        
    def setup_connections(self, combo_handler, checkbox_handler):
        """Setup signal connections for UI elements."""
        self.ui.comboBox.activated.connect(combo_handler)
        self.ui.checkBox.toggled.connect(checkbox_handler)
        
    def show(self):
        """Show the UI window."""
        self.ui.show()
        
    def set_label_text(self, text, font_size):
        """Set the text and font size for the label."""
        self.ui.label.setText(text)
        font = self.ui.label.font()
        font.setPointSize(font_size)
        self.ui.label.setFont(font)
        
    def set_stylesheet(self, stylesheet):
        """Apply stylesheet to the UI."""
        self.ui.setStyleSheet(stylesheet)
        
    def reset_stylesheet(self):
        """Reset the UI stylesheet to default."""
        self.ui.setStyleSheet("")
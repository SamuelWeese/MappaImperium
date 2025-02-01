from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QScrollArea, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt

class Popup(QWidget):
    def __init__(self, parent=None, text:str=None, title:str=None, blocking:bool=False):
        super().__init__(parent)

        if title:
            self.setWindowTitle(title)
        self.setGeometry(100, 100, 400, 300)

        if blocking:
            self.setWindowModality(Qt.ApplicationModal)

        self.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint)

        layout = QVBoxLayout(self)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget(self.scroll_area)
        self.scroll_area.setWidget(self.scroll_content)

        self.scroll_layout = QVBoxLayout(self.scroll_content)

        layout.addWidget(self.scroll_area)
        if text:
            self.add_text(text)
        # Enable window dragging

        self.drag_position = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_position)

    def add_text(self, new_text):
        label = QLabel(new_text)
        label.setWordWrap(True)

        self.scroll_layout.addWidget(label)

    def clear_scroll(self):
        self.scroll_layout = None
        self.scroll_layout = QVBoxLayout(self.scroll_content)

    def closeEvent(self, event):
        self.close()
import sys
from PyQt5.QtCore import Qt, pyqtSignal, QObject, QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextEdit
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QScrollBar, QDialog, QListWidget, QListWidgetItem
from PyQt5.QtGui import QColor
import re
from . import command_parser as command


def get_xyz(text:str=None):
    matches = re.findall(r"\((.*?)\)", text)
    print(matches)
    if matches:
        text = matches[0].replace("(","").replace(")","").replace(" ","")
        text = text.split(',')
        x = text[0]
        y = text[1]
        return x, y
    else:
        return 0, 0

class ScrollableTextEdit(QTextEdit):
    enterPressed = pyqtSignal()

    def __init__(self):
        super().__init__()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.enterPressed.emit()
        else:
            super().keyPressEvent(event)

    def wheelEvent(self, event):
        modifiers = QApplication.keyboardModifiers()
        if modifiers == Qt.ControlModifier:
            # zoom in/out functionality
            if event.angleDelta().y() > 0:
                self.zoomIn(1)
            else:
                self.zoomOut(1)
        else:
            super().wheelEvent(event)

class HistoryWidget(QListWidget):
    def __init__(self):
        super().__init__()
        self.setWordWrap(True)

    def updateHistory(self, text):
        item = QListWidgetItem(text)
        self.addItem(item)
        self.scrollToBottom()

    def updateResponse(self, text):
        item = QListWidgetItem(text)
        item.setBackground(QColor("darkgray"))
        if text is None or len(text) == 0:
            item.setBackground(QColor("red"))
            item.setText("Response Error!")
        self.addItem(item)
        self.scrollToBottom()

class TextEntryAndHistory(QWidget):
    def __init__(self, fxn_connection=None):
        super().__init__()
        layout = QVBoxLayout()

        self.historyWidget = HistoryWidget()
        item = QListWidgetItem("Text Area")
        item.setBackground(QColor("darkgray"))
        self.historyWidget.addItem(item)
        self.scrollableTextEdit = ScrollableTextEdit()
        self.fxn_connection = fxn_connection
        self.scrollableTextEdit.enterPressed.connect(self.interaction)

        layout.addWidget(self.historyWidget, 9)  # 80 of the content
        layout.addWidget(self.scrollableTextEdit, 1)  # 20 of the content

        self.setLayout(layout)

        self.command_symbol = "/"
        self.command_parser = command.command_parsing

    # this fxn should be as light as possible, as it is called locally for UI on main thread
    # heavier things should go in interaction to be put on a worker
    def updateHistoryClearText(self):
        self.text = self.scrollableTextEdit.toPlainText()
        self.historyWidget.updateHistory(self.text)
        self.scrollableTextEdit.clear()

    def interaction(self):
        self.updateHistoryClearText()

        if command.starts_with(self.text) == self.command_symbol:
            self.worker = Worker(self.command_parser, self.text)
            self.worker.finished.connect(self.handle_response)
            self.worker.start()

    def handle_response(self, text):
        self.historyWidget.updateResponse(text)

class Worker(QThread):
    finished = pyqtSignal(str)

    def __init__(self, command_fxn, text):
        super().__init__()
        self.command_fxn = command_fxn 
        self.text = text

    def run(self):
        response = self.command_fxn(self.text)
        self.finished.emit(str(response))
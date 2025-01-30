from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QLabel, QColorDialog, QPushButton, QSlider
from PyQt5.QtCore import Qt
from . import StyleSheet
#
# Tool options should go here
#
class BaseToolWidget(QWidget):
    def __init__(self, tool):
        super().__init__()
        self.tool = tool
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

class ColorSelector(BaseToolWidget):
    def __init__(self, tool):
        super().__init__(tool)

        self.color_dialog = QColorDialog(self)
        self.color_dialog.setWindowFlags(Qt.Widget)
        self.color_dialog.setOptions(
            QColorDialog.NoButtons
            # Below is a way to make it embedded
            # I need to write my own picker, or find a different way to pick to use native
            # Possibly using a dialog is correct
            # TODO
            #| QColorDialog.DontUseNativeDialog
        )
        self.color_dialog.currentColorChanged.connect(self.update_color)
        self.layout.addWidget(self.color_dialog)

    def update_color(self, color):
        self.tool.setColor(color)

class WidthManager(BaseToolWidget):
    def __init__(self, tool):
        super().__init__(tool)
        self.width_slider = QSlider(Qt.Horizontal)
        label = QLabel("Width")
        label.setStyleSheet(StyleSheet.style_title)
        label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(label)
        self.layout.addWidget(self.width_slider)
        self.width_slider.valueChanged.connect(self.setWidth)

    def setWidth(self, width):
        self.tool.setWidth(width)

class ColorAndWidth(ColorSelector, WidthManager):
    def __init__(self, tool):
        super().__init__(tool)
#
# Below are the interface and display for the content
#
class CanvasToolOptions():
    def __init__(self, tab_name: str, tab_content: QWidget):
        self.tab_name = tab_name
        self.tab_content = tab_content 
        print(tab_name)
        print(tab_content)

class CanvasToolSelector(QWidget):
    def __init__(self, tool_list: list[CanvasToolOptions]):
        super().__init__()
        layout = QVBoxLayout(self)

        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)

        for i in tool_list:
            if i:
                self.tabs.addTab(self.create_tab(f"{i.tab_name}", i.tab_content), f"{i.tab_name}")
            else:
                self.tabs.addTab(self.create_tab("No Tool", QWidget), "No Tool")

    def create_tab(self, option_name: str, tab_content: QWidget):
        label = QLabel(f"You selected: {option_name}")
        label.setStyleSheet(StyleSheet.style_title)
        label.setAlignment(Qt.AlignCenter)
        if tab_content.layout:
            tab_content.layout.addWidget(label)
        else:
            layout = QVBoxLayout(tab_content)
            layout.addWidget(label)
            tab_content.setLayout(layout)
        return tab_content
import json

from PyQt5.QtWidgets import QApplication, QMainWindow, QSplitter, QMenuBar, QMenu, QAction, QFileDialog, QInputDialog, QGraphicsView
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QHBoxLayout, QVBoxLayout, QWidget, QGraphicsSceneWheelEvent, QColorDialog, QDialog

from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot

from . import ImageOnCanvas, ViewWindow, ScrollableTextEdit, CanvasTool, Popup, DirtySave

DEBUGGING=True
if DEBUGGING:
    import pprint
    DEBUG_NAME = "WHY ME"
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Create a QSplitter to manage the resizing of the widgets
        splitter = QSplitter(Qt.Horizontal)

        # Create the image_widget on the left
        self.image_widget = ViewWindow.ViewWindow(self)
        splitter.addWidget(self.image_widget)

        # Load the default text and tool selector
        side_bar_splitter = QSplitter(Qt.Vertical)
        side_bar_splitter.addWidget(ScrollableTextEdit.TextEntryAndHistory(fxn_connection=self.open_latest_image))
        side_bar_splitter.addWidget(self.image_widget.tool_tab)
        self.side_bar = side_bar_splitter
        splitter.addWidget(self.side_bar)

        # Set the size ratio for the widgets (80% - 20%)
        splitter.setSizes([4 * splitter.size().width() // 5, splitter.size().width() // 5])

        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(splitter)

        self.setup_menu_bar()

        self.setWindowTitle('Mappa Imperium')
        if DEBUGGING:
            self.setWindowTitle(f'The Jaran Project - {DEBUG_NAME}')
        self.setGeometry(100, 100, 800, 600)

    def setup_menu_bar(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        open_action = QAction('Open', self)
        open_action.triggered.connect(self.open_image)
        file_menu.addAction(open_action)

        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        list_images_action = QAction('List Images', self)
        list_images_action.triggered.connect(self.list_images)
        file_menu.addAction(list_images_action)

        save_images_action = QAction('Save State', self)
        save_images_action.triggered.connect(self.save_all)
        file_menu.addAction(save_images_action)

        load_images_action = QAction('Load State', self)
        load_images_action.triggered.connect(self.load_all)
        file_menu.addAction(load_images_action)

        # Canvas Menu
        canvas_menu = menubar.addMenu('Canvas')

        list_images_action = QAction('List Images', self)
        list_images_action.triggered.connect(self.list_images)
        canvas_menu.addAction(list_images_action)

        clear_canvas_action = QAction('Clear Canvas', self)
        clear_canvas_action.triggered.connect(self.clear_canvas)
        canvas_menu.addAction(clear_canvas_action)

    def setup_side_bar(self):
        pass

    def open_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp *.gif *.jpeg);;All Files (*)", options=options)

        if file_name:
            self.image_widget.set_image(file_name)

    def open_latest_image(self, x, y, z, rotation = 0.0):
        folder_path = os.path.join(os.path.dirname(__file__), "test_images")
        files = os.listdir(folder_path)
        if not files:
            print("No images found in test_images folder.")
            return

        xy_scale = 1
        # Filter only image files
        image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.bmp', '.gif', '.jpeg'))]

        if not image_files:
            print("No image files found in test_images folder.")
            return

        # Get the latest modified image file
        latest_image = max(image_files, key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))
        latest_image_path = os.path.join(folder_path, latest_image)
        print(latest_image_path)
        # This is a bad patch
        latest_image_path.replace('/', '\\')
        print(f"x:{x}\ny:{y}\nz:{z}\nrot:{rotation}")
        if int(x) > 6500: 
            x=6500
        elif int(x) < -1500:
            x = -1500
        if int(y) > 6500:
            y=6500
        elif int(y) < -1500:
            y = -1500
        # WE NEED COORDS HERE
        if latest_image:
            self.image_widget.addImageOnCanvas(ImageOnCanvas.ImageOnCanvas(int(x)*xy_scale, int(y)*xy_scale*(-1), int(z), rotation, latest_image_path))

    def list_images(self):
        image_list = self.image_widget.list_images_on_canvas()
        for index, image_info in enumerate(image_list):
            print(f"Image {index + 1}:")
            print(f"  Location: ({image_info['x']}, {image_info['y']})")
            # Below broke upon importing images from cont files, don't know why
            #print(f"  Rotation: {image_info['rotation']} degrees")
            print(f"  File Name: {image_info['image_path']}")

    def save_images(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "All Files (*);;Text Files (*.txt)", options=options)
        if file_name:
            self.image_widget.save(folder_path=file_name)
    
    def load_images(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", "", options=options)
        if folder_path:
            self.image_widget.load_images_folder(folder_path=folder_path)

    # # This will eventually consume some other kind of data, ie a text file full of image links
    # # this is proof of concept for now
    # def populate_canvas(self):
    #     options = QFileDialog.Options()
    #     options |= QFileDialog.DontUseNativeDialog
    #     file_name, _ = QFileDialog.getOpenFileName(self, "Open Set", "", "Custom Continuity files (*.cont);;All Files (*)", options=options)

    #     asset_folder = "./assets/"
    #     with open(file_name) as handle:
    #         for line in handle:
    #             image_path, x, y, z, scale =  map(str.strip, line.split(','))
    #             # Rotation is currently unused for our generations
    #             # So is Z, it would require a queing system or something
    #             rotation = 0
    #             # Currently X and Y have a bad offset, as images are positioned to the top left corner not the middle
    #             # We need to calculate this based off of scale, where positioning is x-scale/2, y-scale/2
    #             # Convert numeric values to appropriate types
    #             x = int(float(x)*1024)
    #             y = int(float(y)*1024)
    #             scale = float(scale)

    #             x = x - int(scale*1024/2)
    #             y = y - int(scale*1024/2)
    #             rotation = int(rotation)

    #             # Create ImageOnCanvas instance and append to image_list
    #             image_item = ImageOnCanvas.ImageOnCanvas(x, y, scale, rotation, asset_folder+image_path)
    #             self.image_widget.addImageOnCanvas(image_item)

    def clear_canvas(self):
        self.image_widget.clear_canvas()

    def save_all(self):
        file_options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "All Files (*);;Mappa Files (*.mappa)", options=file_options)
        if file_name:
            with open(file_name, 'w') as file_handle:
                try:
                    value = DirtySave.jsonify_object(self)
                    pprint.pprint(value)
                    file_handle.write(str(value))
                except Exception as e:
                    Popup.Popup(self, f"Work did not save!\n {e}", "Error Saving", blocking=True).show()
        else:
            Popup.Popup(self, "File not found!", "Error Finding File", blocking=True).show()

    def load_all(self):
        new_data = None
        file_options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Load File", "", "All Files (*);;Mappa Files (*.mappa)", options=file_options)
        if file_name:
            new_data = None
            with open(file_name, 'rb') as file_handle:
                try:
                    new_data = json.load(file_handle)
                except Exception as e:
                    Popup.Popup(self, f"File did not load!\n {e}", "Error Loading File", blocking=True).show()
                    return
            new_object = DirtySave.load_object(new_data)
            if type(new_object) is MainWindow:
                self = new_object
                return
            self.__dict__.update(new_data)



if __name__ == '__main__':
    # Remove old chat history
    json_path = os.path.join(pipeline_parent_dir, "chat_history.json")
    if os.path.exists(json_path):
        os.remove(json_path)
    else:
        print("File does not exist.")

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
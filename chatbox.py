import sys
import socket
import threading
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton, QHBoxLayout, QLabel, QInputDialog
)

class ChatBox(QWidget):
    def __init__(self, is_host, host, port):
        super().__init__()

        self.host = host
        self.port = port
        self.is_host = is_host
        self.server_socket = None
        self.client_socket = None

        self.setWindowTitle("ChatBox")
        self.setGeometry(100, 100, 400, 500)

        self.layout = QVBoxLayout()

        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.layout.addWidget(self.chat_display)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type your message here...")
        self.layout.addWidget(self.input_field)

        self.send_button = QPushButton("Send")
        self.layout.addWidget(self.send_button)
        self.send_button.clicked.connect(self.send_message)
        self.input_field.returnPressed.connect(self.send_message)

        self.setLayout(self.layout)
        if self.is_host:
            self.start_server()
        else:
            self.connect_to_server()

    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        self.chat_display.append("Waiting for a connection...")

        threading.Thread(target=self.accept_client, daemon=True).start()

    def accept_client(self):
        self.client_socket, addr = self.server_socket.accept()
        self.chat_display.append(f"Connected to {addr}")

        threading.Thread(target=self.receive_messages, daemon=True).start()

    def connect_to_server(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        self.chat_display.append("Connected to the server.")

        threading.Thread(target=self.receive_messages, daemon=True).start()

    def send_message(self):
        message = self.input_field.text().strip()
        if message:
            try:
                self.client_socket.sendall(message.encode('utf-8'))
                self.chat_display.append(f"You ({user_name}): {message}")
                self.input_field.clear()
            except Exception as e:
                self.chat_display.append(f"Error sending message: {e}")

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    self.chat_display.append(f": {message}")
            except Exception as e:
                self.chat_display.append(f"Error receiving message: {e}")
                break

if __name__ == "__main__":
    app = QApplication(sys.argv)

    choice, ok = QInputDialog.getItem(
        None, "Host or Join", "Choose mode:", ["Host", "Join"], 0, False
    )

    if not ok:
        print("KILL MYSELF")
        sys.exit()

    HOST = "127.0.0.1"
    PORT = 12345

    if choice == "Host":
        is_host = True
    else:
        is_host = False
        HOST, ok = QInputDialog.getText(None, "Server IP", "Enter server IP:")
        if not ok:
            sys.exit()

    chatbox = ChatBox(is_host, HOST, PORT)
    chatbox.show()

    sys.exit(app.exec_())
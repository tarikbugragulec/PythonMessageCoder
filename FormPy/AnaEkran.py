import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox, QWidget, QStackedWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from UI.EncodeUI import Encode
from UI.DecodeUI import Decode

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Ana Pencere")
        self.setGeometry(100, 100, 400, 300)
        icon=QIcon('Icons\laptop.png')
        self.setWindowIcon(icon)


        menubar = self.menuBar()
        options_menu = menubar.addMenu("Options")

        action_encode = QAction("Encode", self)
        action_encode.triggered.connect(self.show_encode_ui)
        options_menu.addAction(action_encode)

        action_decode = QAction("Decode", self)
        action_decode.triggered.connect(self.show_decode)
        options_menu.addAction(action_decode)

        help_menu = menubar.addMenu("Help")
        action_about = QAction("About", self)
        action_about.triggered.connect(self.show_about)
        help_menu.addAction(action_about)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.stacked_widget = QStackedWidget(self.main_widget)
        layout = QVBoxLayout(self.main_widget)
        layout.addWidget(self.stacked_widget)

        self.encode_ui = Encode()
        self.decode_ui = Decode()
        self.stacked_widget.addWidget(self.encode_ui)
        self.stacked_widget.addWidget(self.decode_ui)
        

    def show_encode_ui(self):
        
        self.stacked_widget.setCurrentWidget(self.encode_ui)

    def show_decode(self):
        self.stacked_widget.setCurrentWidget(self.decode_ui)

    def show_about(self):
        try:
            with open("Bilgiler.txt", 'r') as file:
                content = file.read()
        except FileNotFoundError:
            print("Bilgiler.txt dosyası bulunamadı.")
            return None
        except Exception as e:
            print("Bir hata oluştu:", str(e))
            return None

        Message = QMessageBox()
        Message.setIcon(QMessageBox.Question)  # Set the icon as QMessageBox.Question
        Message.setText(content)
        Message.setWindowTitle("Hakkında")
        Message.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

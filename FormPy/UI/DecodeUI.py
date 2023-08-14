from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QPlainTextEdit
from Kodlar import code

class Decode(QWidget):
    def __init__(self):
        super().__init__()
        
        self.text_edit = QTextEdit(self)
        self.plain_text_edit = QPlainTextEdit(self)
        self.button = QPushButton("Decode", self)
        self.button.clicked.connect(self.decode_text)
        self.plain_text_edit.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.button)
        layout.addWidget(self.plain_text_edit)

        self.setLayout(layout)

    def decode_text(self):
        input_text = self.text_edit.toPlainText()
        output_text=code.Codes.Decode(input_text)
        self.plain_text_edit.setPlainText(output_text)

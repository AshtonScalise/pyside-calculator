import sys

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setFixedSize(400, 600)
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignCenter)

        self.label = QLabel("Hello World")



        self.main_layout.addWidget(self.label)
        self.setLayout(self.main_layout)




app = QApplication(sys.argv)

window = MainWindow()
window.show() 

app.exec()
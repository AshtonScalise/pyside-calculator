import sys

from PySide6.QtWidgets import QApplication, QWidget, QLabel, \
QVBoxLayout, QGridLayout, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


math_string = ''

def do_things(txt):
    global math_string
    math_string += txt
    print(math_string)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setFixedSize(400, 600)
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignCenter)

        self.main_ind = Indicator("Hello")
        self.num_grid = NumGrid()

 
        self.main_layout.addWidget(self.main_ind)
        self.main_layout.addWidget(self.num_grid)
        self.setLayout(self.main_layout)


class StdButton(QWidget):
    def __init__(self, text, parent=None):
        super(StdButton, self).__init__(parent)
        self.setMaximumWidth(200)
        self.button = QPushButton()
        self.button.setText(text)
        self.column_layout = QVBoxLayout()
        self.column_layout.addWidget(self.button)
        self.setLayout(self.column_layout)
        self.button.clicked.connect(lambda: do_things(self.button.text()))

class NumGrid(QWidget):
    def __init__(self, parent=None):
        super(NumGrid, self).__init__(parent)

        self.num_grid = QGridLayout()

        count = 9
        for x in range(1, 4, 1):
            for y in range(3, 0, -1):
                button = StdButton(str(count))
                self.num_grid.addWidget(button, x, y)
                count = count - 1

        self.button_neg = StdButton("+/-")
        self.button0 = StdButton("0")
        self.button_dec = StdButton(".")

        self.button_c = StdButton("C")

        self.button_d = StdButton("÷")
        self.button_m = StdButton("x")
        self.button_s = StdButton("-")
        self.button_a = StdButton("+")
        self.button_e = StdButton("=")

        self.num_grid.addWidget(self.button_neg, 4, 1)
        self.num_grid.addWidget(self.button0, 4, 2)
        self.num_grid.addWidget(self.button_dec, 4, 3)

        self.num_grid.addWidget(self.button_c, 0, 1)

        self.num_grid.addWidget(self.button_d, 0, 4)
        self.num_grid.addWidget(self.button_m, 1, 4)
        self.num_grid.addWidget(self.button_s, 2, 4)
        self.num_grid.addWidget(self.button_a, 3, 4)
        self.num_grid.addWidget(self.button_e, 4, 4)

        self.setLayout(self.num_grid)

class Indicator(QWidget):
    def __init__(self, text, parent=None):
        super(Indicator, self).__init__(parent)
        self.label = QLabel()
        self.label.setText(text)
        self.label.setFixedWidth(340)
        self.label.setFont(QFont('Roboto', 20))
        self.label.setAlignment(Qt.AlignRight)
        self.label.setStyleSheet('border: 4px solid grey;')
        self.column_layout = QVBoxLayout()
        self.column_layout.setAlignment(Qt.AlignCenter)
        self.column_layout.addWidget(self.label)
        self.setLayout(self.column_layout)



app = QApplication(sys.argv)

window = MainWindow()
window.show() 

app.exec()
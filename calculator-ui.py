import sys

from PySide6.QtWidgets import QApplication, QWidget, QLabel, \
QVBoxLayout, QGridLayout, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


math_string = ''


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setFixedSize(400, 400)
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignCenter)

        self.num_grid = NumGrid()

 
        self.main_layout.addWidget(main_ind)
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
        self.button.clicked.connect(lambda: handle_click(self.button.text()))

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
main_ind = Indicator("Hello")


def do_math(arg1, arg2, op):
    if(op == '÷'):
        return float(arg1) / float(arg2)
    if(op == 'x'):
        return float(arg1) * float(arg2)
    if(op == '-'):
        return float(arg1) - float(arg2)
    if(op == '+'):
        return float(arg1) + float(arg2)                

def get_op():
    return ''.join([i for i in math_string if not i.isdigit()]).replace('.', '') 

def handle_click(txt):
    global math_string


    if(txt == 'C'):
        math_string = ''
        main_ind.label.setText(math_string)
        return
    if(txt == '='):
        op = get_op()
        args = math_string.split(op)
        math_string = str(do_math(args[0], args[1], op))
        main_ind.label.setText(math_string)
        args = None
        return
    if(txt == '÷' or txt == 'x' or txt == '-' or txt == '+'): 
       op = get_op()

       if op == '':
            math_string += txt                       
            main_ind.label.setText(math_string)
            return
       else:
           args = math_string.split(op)
           math_string = str(do_math(args[0], args[1], op))
           main_ind.label.setText(math_string)
        #    op = None
           return

    math_string += txt
    main_ind.label.setText(math_string)

window = MainWindow()

window.show() 

app.exec()
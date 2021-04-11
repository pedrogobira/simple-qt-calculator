from PySide2 import QtWidgets as qtw


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setFixedSize(310, 200)

        self.central_widget = (qtw.QWidget())
        self.setCentralWidget(self.central_widget)

        self.central_widget.setLayout(qtw.QVBoxLayout())

        self.temp_nums = []
        self.op_nums = []

        self.keypad()

        self.show()

    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())
        container.setFixedSize(300, 190)

        # Campo que apresenta o que é digitado e o result
        self.result_field = qtw.QLineEdit()

        # Botões da calculadora
        btn_enter = qtw.QPushButton('=', clicked=self.func_enter)
        btn_clear = qtw.QPushButton('C', clicked=self.func_clear)

        btn_9 = qtw.QPushButton('9', clicked=lambda: self.num_press('9'))
        btn_8 = qtw.QPushButton('8', clicked=lambda: self.num_press('8'))
        btn_7 = qtw.QPushButton('7', clicked=lambda: self.num_press('7'))
        btn_6 = qtw.QPushButton('6', clicked=lambda: self.num_press('6'))
        btn_5 = qtw.QPushButton('5', clicked=lambda: self.num_press('5'))
        btn_4 = qtw.QPushButton('4', clicked=lambda: self.num_press('4'))
        btn_3 = qtw.QPushButton('3', clicked=lambda: self.num_press('3'))
        btn_2 = qtw.QPushButton('2', clicked=lambda: self.num_press('2'))
        btn_1 = qtw.QPushButton('1', clicked=lambda: self.num_press('1'))
        btn_0 = qtw.QPushButton('0', clicked=lambda: self.num_press('0'))

        btn_plus = qtw.QPushButton('+', clicked=lambda: self.op_press('+'))
        btn_minus = qtw.QPushButton('-', clicked=lambda: self.op_press('-'))
        btn_mult = qtw.QPushButton('*', clicked=lambda: self.op_press('*'))
        btn_div = qtw.QPushButton('/', clicked=lambda: self.op_press('/'))

        # Adicionando botões no layout
        container.layout().addWidget(self.result_field, 0, 0, 1, 4)
        container.layout().addWidget(btn_enter, 1, 0, 1, 2)
        container.layout().addWidget(btn_clear, 1, 2, 1, 2)
        container.layout().addWidget(btn_7, 2, 0)
        container.layout().addWidget(btn_8, 2, 1)
        container.layout().addWidget(btn_9, 2, 2)
        container.layout().addWidget(btn_plus, 2, 3)
        container.layout().addWidget(btn_4, 3, 0)
        container.layout().addWidget(btn_5, 3, 1)
        container.layout().addWidget(btn_6, 3, 2)
        container.layout().addWidget(btn_minus, 3, 3)
        container.layout().addWidget(btn_1, 4, 0)
        container.layout().addWidget(btn_2, 4, 1)
        container.layout().addWidget(btn_3, 4, 2)
        container.layout().addWidget(btn_mult, 4, 3)
        container.layout().addWidget(btn_0, 5, 0, 1, 3)
        container.layout().addWidget(btn_div, 5, 3)

        # Adicionando keypad ao widget principal de MainWindow
        self.layout().addWidget(container)

    def num_press(self, number):
        self.temp_nums.append(number)
        temp_string = ''.join(self.temp_nums)

        if self.op_nums:
            self.result_field.setText(''.join(self.op_nums) + temp_string)
        else:
            self.result_field.setText(temp_string)

    def op_press(self, operation):
        temp_string = ''.join(self.temp_nums)

        self.op_nums.append(temp_string)
        self.op_nums.append(operation)

        self.temp_nums = []

        self.result_field.setText(''.join(self.op_nums))

    def func_enter(self):
        temp_string = ''.join(self.op_nums) + ''.join(self.temp_nums)
        result = eval(temp_string)

        temp_string += '='
        temp_string += str(result)

        self.result_field.setText(temp_string)

    def func_clear(self):
        self.result_field.clear()
        self.temp_nums = []
        self.op_nums = []


if __name__ == "__main__":
    app = qtw.QApplication([])
    main_window = MainWindow()
    app.exec_()

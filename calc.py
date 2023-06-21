from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QGridLayout, QLineEdit

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        layout.setContentsMargins(10, 10, 10, 10)
        self.input_line = QLineEdit()
        self.input_line.setFixedHeight(35)
        layout.addWidget(self.input_line)
        buttons_grid = QGridLayout()
        layout.addLayout(buttons_grid)
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]
        positions = [(i, j) for i in range(4) for j in range(4)]
        for position, button_text in zip(positions, buttons):
            row, column = position
            button = QPushButton(button_text)
            button.setFixedHeight(40)
            buttons_grid.addWidget(button, row, column)
            button.clicked.connect(self.handle_button_click)
    def handle_button_click(self):
        button = self.sender()
        text = button.text()
        if text == "=":
            try:
                result = eval(self.input_line.text())
                self.input_line.setText(str(result))
            except Exception as e:
                self.input_line.setText("Error")
        else:
            self.input_line.setText(self.input_line.text() + text)

if __name__ == "__main__":
    app = QApplication([])
    calculator = Calculator()
    calculator.show()
    app.exec()

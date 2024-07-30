
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel,
)


windowSIZE = 400
displayHEIGHT = 50
buttonSIZE = 60
ERROR_MSG = "ERROR"




class MyCalcWindow (QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MyPythonCalculator")
        self.setFixedSize(340,340)

        self.mainLayout = QVBoxLayout()

        self.display_Label = QLabel("0", self) 
        self.mainLayout.addWidget(self.display_Label)
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(centralWidget)
        
        button_layout = QGridLayout()
        
        for character in range(10):
            buttons = QPushButton(str(character), self)
            buttons.setStyleSheet("QPushButton"
                "{"
                    "height : 40px;"
                    "width : 40px;"
                    "border : 4px white;"
                    "color : black;"
                    "background: #ADD8E6 ;"
                    "border-radius: 5px;" 
                    "}"  )
            buttons.clicked.connect(lambda _, number = character: self.on_digit_clicked(number))
            if character == 0:
                button_layout.addWidget(buttons, 4, 1)
            else:
                button_layout.addWidget(buttons, (12 - character) // 3, (character - 1) % 3)

        operators = ["+", "-", "/", "*"]

        for operator in operators:
            buttons = QPushButton(operator, self)
            buttons.clicked.connect(lambda _, op = operator: self.on_operator_clicked(op))
            buttons.setStyleSheet("QPushButton"
                    "{"
                    "height : 40px;"
                    "width : 40px;"
                    "border : 4px white;"
                    "background: #00008B ;"
                    "border-radius: 5px;" 
                    "}" )
            button_layout.addWidget(buttons, (operators.index(operator) + 1), 3)

        equals_button = QPushButton("=", self)
        equals_button.clicked.connect(self.calculate_result)
        equals_button.setStyleSheet("QPushButton"
                "{"
                    "height : 40px;"
                    "width : 40px;"
                    "border : 4px white;"
                    "background: green;"
                    "border-radius: 5px;" 
                    "}" )
        button_layout.addWidget(equals_button, 4, 2)

        clear_button = QPushButton("C", self)
        clear_button.clicked.connect(self.clear_input)
        clear_button.setStyleSheet("QPushButton"
                "{"
                    "height : 40px;"
                    "width : 40px;"
                    "border : 4px white;"
                    "background: red;"
                    "border-radius: 5px;" 
                    "}" )
        button_layout.addWidget(clear_button, 4 , 0)


        
        self.mainLayout.addLayout(button_layout)

        self.current_input = ""

    def on_digit_clicked(self, digit):

        self.current_input += str(digit)
        self.display_Label.setText(self.current_input)

    def on_operator_clicked(self, operator):

        if self.current_input and self.current_input[-1] not in ["+", "-", "*", "/"]:
            self.current_input += operator
            self.display_Label.setText(self.current_input)

    def clear_input(self):

        self.current_input = ""
        self.display_Label.setText("0")

    def calculate_result(self):
        try:
            result = eval(self.current_input)
            self.display_Label.setText(str(result))
            self.current_input = str(result)
        
        except Exception:
            self.display_Label.setText("ERROR")
            self.current_input = ""




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyCalcWindow()
    window.show()
    sys.exit(app.exec())
    







    

        
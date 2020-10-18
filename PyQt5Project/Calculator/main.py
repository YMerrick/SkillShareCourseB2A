import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Button():
    def __init__(self,text,results):
        self.b = QPushButton(text)
        self.text = text
        self.results = results
        self.b.clicked.connect(lambda: self.handleInput(self.text))

    def handleInput(self,v):

        if v=="=":
            try:
                res = eval(self.results.text())
                self.results.setText(str(res))
            except Exception as e:
                raise print('That is an invalid expression')
                self.results.setText("")
        elif v=="AC":
            self.results.setText("")
        elif v=="^":
            self.results.setText(self.results.text() + "**")
        elif v=="√":
            self.results.setText(str(math.sqrt(float(self.results.text()))))
        else:
            self.results.setText(self.results.text() + str(v))



class Application(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.createApp()


    def createApp(self):
        #Create our grid

        grid = QGridLayout()

        result = QLineEdit()

        buttons = ["AC","√","^","/",
                    7,8,9,"*",
                    4,5,6,"-",
                    1,2,3,"+",
                    0,".","="]

        col,row = 0,4

        grid.addWidget(result,0,0,4,4)

        for button in buttons:
            if col > 3:
                col = 0
                row += 1

            b = Button(str(button), result)
            if button == 0:
                grid.addWidget(b.b,row,col,1,2)
                col += 1
            else:
                    grid.addWidget(b.b,row,col,1,1)
            col += 1



        self.setLayout(grid)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec_())

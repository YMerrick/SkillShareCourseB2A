import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QHBoxLayout,
                             QVBoxLayout, QPushButton, QLabel, QLineEdit)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUi()

    def initUi(self):
        label = QLabel("Name: ")
        nameInput = QLineEdit()

        button = QPushButton("Set Name")

        h = QHBoxLayout()
        h.addStretch()
        h.addWidget(label)
        h.addWidget(nameInput)

        v = QVBoxLayout()
        v.addStretch()
        v.addLayout(h)
        v.addWidget(button)

        self.setLayout(v)


        self.setWindowTitle("horizontal layout")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    sys.exit(app.exec_())

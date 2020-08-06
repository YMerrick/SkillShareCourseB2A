import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QHBoxLayout,
                             QVBoxLayout, QPushButton, QLabel, QLineEdit)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUi()

    def alterName(self):
        self.textLabel.setText(self.nameInput.text())
        self.setWindowTitle(self.nameInput.text() + "'s Window")


    def initUi(self):
        self.textLabel = QLabel("There has been nothing entered so I don't know who I am")
        self.label = QLabel("Name: ")
        self.nameInput = QLineEdit()

        self.button = QPushButton("Set Name")
        self.button.clicked.connect(self.alterName)

        h = QHBoxLayout()
        h.addStretch()
        h.addWidget(self.label)
        h.addWidget(self.nameInput)

        v = QVBoxLayout()
        v.addStretch()

        v.addWidget(self.textLabel)
        v.addLayout(h)
        v.addWidget(self.button)

        self.setLayout(v)


        self.setWindowTitle("Nothing has been clicked")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    sys.exit(app.exec_())

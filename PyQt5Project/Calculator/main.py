import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QHBoxLayout,
                             QVBoxLayout, QPushButton)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUi()

    def initUi(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        horizontal = QHBoxLayout()
        horizontal.addStretch(1)

        horizontal.addWidget(okButton)
        horizontal.addWidget(cancelButton)

        vertical = QVBoxLayout()
        vertical.addStretch(1)
        vertical.addLayout(horizontal)

        self.setLayout(vertical)

        self.setWindowTitle("horizontal layout")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    sys.exit(app.exec_())

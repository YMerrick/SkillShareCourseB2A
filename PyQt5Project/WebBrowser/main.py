import sys
import os
import json

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QLineEdit, QTabBar,
                             QFrame, QStackedLayout)
from PyQt5.QtGui import QIcon, QWindow, QImage
from PyQt5.QtCore import *


class AddressBar(QLineEdit):
    def __init__(self):
        super().__init__()

    def mousePressEvent(self,e):
        print(e)
        self.selectAll()

class App(QFrame):
    """docstring for App."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scuffed Browser")
        self.createApp()
        self.setBaseSize(1300,700)


    def createApp(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)

        #Create Tabs
        self.tabBar = QTabBar(movable=True,tabsClosable=True)
        self.tabBar.tabCloseRequested.connect(self.closeTab)

        self.tabBar.addTab("Tab 1")
        self.tabBar.addTab("Tab 2")

        self.tabBar.setCurrentIndex(0)

        #Create Address bar
        self.toolBar = QWidget()
        self.toolBarLayout = QHBoxLayout()
        self.addressBar = AddressBar()

        self.toolBar.setLayout(self.toolBarLayout)
        self.toolBarLayout.addWidget(self.addressBar)

        self.layout.addWidget(self.tabBar)
        self.layout.addWidget(self.toolBar)
        self.setLayout(self.layout)

        self.show()

    def closeTab(self, i):
        self.tabBar.removeTab(i)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())

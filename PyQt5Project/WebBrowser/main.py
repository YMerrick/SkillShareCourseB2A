import sys
import os
import json

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QLineEdit, QTabBar,
                             QFrame, QStackedLayout)
from PyQt5.QtGui import QIcon, QWindow, QImage
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


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
        self.tabBar.tabBarClicked.connect(self.switchTab)

        self.tabBar.setCurrentIndex(0)

        #Keep track of tabs
        self.tabCount = 0
        self.tabs = []

        #Create Address bar
        self.toolBar = QWidget()
        self.toolBarLayout = QHBoxLayout()
        self.addressBar = AddressBar()

        self.toolBar.setLayout(self.toolBarLayout)
        self.toolBarLayout.addWidget(self.addressBar)

        #New tab button
        self.addTabButton = QPushButton("+")
        self.addTabButton.clicked.connect(self.addTab)

        self.toolBarLayout.addWidget(self.addTabButton)

        #Set main view
        self.container = QWidget()
        self.container.layout = QStackedLayout()
        self.container.setLayout(self.container.layout)


        self.layout.addWidget(self.tabBar)
        self.layout.addWidget(self.toolBar)
        self.layout.addWidget(self.container)
        self.setLayout(self.layout)

        self.addTab()

        self.show()

    def closeTab(self, i):
        self.tabBar.removeTab(i)

    def addTab(self):
        i = self.tabCount

        self.tabs.append(QWidget())
        self.tabs[i].layout = QVBoxLayout()
        self.tabs[i].setObjectName("tab"+str(i))

        self.tabs[i].content = QWebEngineView()
        self.tabs[i].content.load(QUrl.fromUserInput("https://google.com"))

        #Add webview to tabs layout
        self.tabs[i].layout.addWidget(self.tabs[i].content)

        #Set toplevel tab from [] to layout
        self.tabs[i].setLayout(self.tabs[i].layout)

        #Adds the tab to the top level stackedWidget
        self.container.layout.addWidget(self.tabs[i])
        self.container.layout.setCurrentWidget(self.tabs[i])

        #Set tab on top of the screen
        self.tabBar.addTab("New Tab")
        self.tabBar.setTabData(i,"tab"+str(i))
        self.tabBar.setCurrentIndex(i)

        self.tabCount += 1

    def switchTab(self, i):
        tab_Data = self.tabBar.tabData(i)

        tab_Content = self.findChild(QWidget, tab_Data)
        self.container.layout.setCurrentWidget(tab_Content)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())

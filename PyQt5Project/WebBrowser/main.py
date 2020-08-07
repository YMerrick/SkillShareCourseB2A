import sys
import os
import json

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QLineEdit, QTabBar,
                             QFrame, QStackedLayout, QShortcut, QKeySequenceEdit)
from PyQt5.QtGui import QIcon, QWindow, QImage, QKeySequence
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class AddressBar(QLineEdit):
    def __init__(self):
        super().__init__()

    def mousePressEvent(self,e):
        self.selectAll()

class App(QFrame):
    """docstring for App."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scuffed Browser")
        self.createApp()
        self.setMinimumSize(960,540)
        self.setBaseSize(1366,768)


    def createApp(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)

        #Create Tabs
        self.tabBar = QTabBar(movable=True,tabsClosable=True,expanding=False)
        self.tabBar.tabCloseRequested.connect(self.closeTab)
        self.tabBar.tabBarClicked.connect(self.switchTab)

        self.tabBar.setCurrentIndex(0)
        self.tabBar.setDrawBase(False)

        self.shortcutNewTab = QShortcut(self,key=QKeySequence("Crtl+T"))
        self.shortcutNewTab.activated.connect(self.addTab)

        #Keep track of tabs
        self.tabCount = 0
        self.tabs = []

        #Create Address bar
        self.toolBar = QWidget()
        self.toolBar.setObjectName("toolbar")
        self.toolBarLayout = QHBoxLayout()
        self.addressBar = AddressBar()
        self.addTabButton = QPushButton("+")

        self.addressBar.returnPressed.connect(self.browseTo)

        #Build Toolbar buttons
        self.backButton = QPushButton("<")
        self.forwardButton = QPushButton(">")
        self.reloadButton = QPushButton("R")

        self.backButton.clicked.connect(self.go_Back)
        self.forwardButton.clicked.connect(self.go_Forward)
        self.reloadButton.clicked.connect(self.reloadPage)


        #Build Toolbar
        self.toolBar.setLayout(self.toolBarLayout)
        self.toolBarLayout.addWidget(self.backButton)
        self.toolBarLayout.addWidget(self.forwardButton)
        self.toolBarLayout.addWidget(self.reloadButton)
        self.toolBarLayout.addWidget(self.addressBar)

        #New tab button
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
        if self.tabBar.count() == 0:
            sys.exit(-1)

    def addTab(self):
        i = self.tabCount

        self.tabs.append(QWidget())
        self.tabs[i].layout = QVBoxLayout()
        self.tabs[i].setObjectName("tab"+str(i))
        self.tabs[i].layout.setContentsMargins(0,0,0,0)

        self.tabs[i].content = QWebEngineView()
        self.tabs[i].content.load(QUrl.fromUserInput("https://google.com"))

        self.tabs[i].content.titleChanged.connect(lambda: self.tabContentChange(i,"title"))
        self.tabs[i].content.iconChanged.connect(lambda: self.tabContentChange(i,"icon"))
        self.tabs[i].content.urlChanged.connect(lambda: self.tabContentChange(i,"url"))

        #Add webview to tabs layout
        self.tabs[i].layout.addWidget(self.tabs[i].content)

        #Set toplevel tab from [] to layout
        self.tabs[i].setLayout(self.tabs[i].layout)

        #Adds the tab to the top level stackedWidget
        self.container.layout.addWidget(self.tabs[i])
        self.container.layout.setCurrentWidget(self.tabs[i])

        #Set tab on top of the screen
        self.tabBar.addTab("New Tab")
        self.tabBar.setTabData(i,{"object":"tab"+str(i),"initial":i})
        self.tabBar.setCurrentIndex(i)

        self.tabCount += 1

    def switchTab(self, i):
        if self.tabBar.tabData(i):
            tab_Content = self.getPageInfo(i)

            self.container.layout.setCurrentWidget(tab_Content)

            self.changeUrl(tab_Content)

    def changeUrl(self,tabContent):
        newUrl = tabContent.content.url().toString()
        self.addressBar.setText(newUrl)


    def browseTo(self):
        text = self.addressBar.text()

        i = self.tabBar.currentIndex()
        view = self.getPageInfo().content

        if "http" not in text:
            if "." not in text:
                url = "https:google.com/#q=" + text
            else:
                url = "https://" + text
        else:
            url = text

        view.load(QUrl.fromUserInput(url))

    def tabContentChange(self,i,type):
        tabObjectName = self.tabs[i].objectName()

        count = 0
        running = True

        currentTabName = self.tabBar.tabData(self.tabBar.currentIndex())["object"]

        if currentTabName == tabObjectName and type == "url":
            self.changeUrl(self.getPageInfo(i))
            return False

        while running:
            tabDataName = self.tabBar.tabData(count)

            if count >= 99:
                running = False

            if tabObjectName == tabDataName["object"]:
                if type == "title":
                    newTitle = self.findChild(QWidget,tabObjectName).content.title()
                    self.tabBar.setTabText(count, newTitle)
                elif type == "icon":
                    newIcon = self.findChild(QWidget, tabObjectName).content.icon()
                    self.tabBar.setTabIcon(count,newIcon)
                running = False
            else:
                count += 1

    def go_Back(self):
        tabContent = self.getPageInfo().content
        tabContent.back()

    def go_Forward(self):
        tabContent = self.getPageInfo().content
        tabContent.forward()

    def reloadPage(self):
        tabContent = self.getPageInfo().content
        tabContent.reload()

    def getPageInfo(self,i=-1):
        if i == -1:
            activeIndex = self.tabBar.currentIndex()
        else:
            activeIndex = i
        tabName = self.tabBar.tabData(activeIndex)["object"]
        return self.findChild(QWidget, tabName)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()

    with open("style.css", "r") as style:
        app.setStyleSheet(style.read())
    sys.exit(app.exec_())

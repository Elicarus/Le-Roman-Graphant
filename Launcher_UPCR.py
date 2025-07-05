from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QDesktopWidget, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
import os
from pathlib import Path



"""
class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        
    def initUI(self):
        
        path = "D:\Obsidian\Le Roman Graphant"
        path_uri = Path(path).as_uri()
        vbox = QVBoxLayout(self)

        self.browser = QWebEngineView()
        vbox.addWidget(self.browser)
        
        self.setLayout(vbox)
        
        self.browser.setHtml(f"<a href='{path_uri}/aller-retour.md'>hihi</a><br>eh nique")
        self.show()
"""

import sys

app = QApplication(sys.argv)
z = QDesktopWidget().availableGeometry()
#print(z.height(), z.width())
x = QWebEngineView()
x.resize(z.width()//2, z.height()-50)
x.move(z.width()//4, 0)
#x.setFixedWidth(1000)
#x.setFixedHeight(800)
path = os.getcwd()
print(path)
path_uri = Path(path).as_uri()
first = "\\" + open(path+"\\START.txt").read()
url = QUrl.fromLocalFile(path + first)
x.load(url)
x.show()

app.exec_()
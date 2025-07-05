from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QDesktopWidget, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
import os
import sys

from pathlib import Path
#import streamlit as st

def main() :
    app = QApplication(sys.argv)
    z = QDesktopWidget().availableGeometry()
    #print(z.height(), z.width())
    x = QWebEngineView()
    x.resize(z.width()//2, z.height()-50)
    x.move(z.width()//4, 0)
    #x.setFixedWidth(1000)
    #x.setFixedHeight(800)
    print(path)
    name = "UPCR"
    start_file = "/" + open("/files/"+name+"/START.txt").read()
    url = QUrl.fromLocalFile("/files/" + name + "/" + start_file)
    x.load(url)
    x.show()

    app.exec_()

main()

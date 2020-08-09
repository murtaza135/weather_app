from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initMainWindow()
        self.initUI()

    def initMainWindow(self):
        self.setGeometry(200,200,750,750)
        self.setMinimumWidth(250)
        self.setMinimumHeight(250)
        self.setWindowTitle("Weather App")
        # self.setWindowIcon(QtGui.QIcon(""))

    def initUI(self):
        pass
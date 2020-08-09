import sys
from PySide2.QtWidgets import QApplication
from view import MainWindow
from model import Model

if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = Model()
    mainWindow = MainWindow(model=model)
    mainWindow.show()
    sys.exit(app.exec_())
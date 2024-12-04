import os
import sys
import gui # Тут ваш файл
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *


class MainApplication(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.directory = os.getcwd()
        self.data = None
        


def main():
  app = QtWidgets.QApplication(sys.argv)
  window = MainApplication()
  window.show()
  app.exec()


if __name__ == '__main__':
  main()
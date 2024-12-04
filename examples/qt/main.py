import os
import sys
import gui # Тут ваш файл
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


class MainApplication(QtWidgets.QMainWindow, gui.MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.directory = os.getcwd()
        self.data = None
        


def main():
  app = QtWidgets.QApplication(sys.argv)
  window = MainApplication()
  window.show()
  app.exec_()


if __name__ == '__main__':
  main()
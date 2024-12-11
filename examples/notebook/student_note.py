import os
import sys
import design
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *


class MainApplication(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.save_btn.clicked.connect(self.save_file)
        self.ext_btn.clicked.connect(self.exit)
        self.dir = os.getcwd()

    def save_file(self):
       self.my_text = self.edt_text.toPlainText()

       fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, 
            "Save File", "", "All Files(*);;Text Files(*.txt)")
       
       if fileName:
            with open(fileName, 'w') as f:
                f.write(self.edt_text.toPlainText())
            self.fileName = fileName
       
       self.edt_text.clear()

    def exit(self):
       exit()

     
    
def main():
  app = QtWidgets.QApplication(sys.argv)
  window = MainApplication()
  window.show()
  app.exec()

if __name__ == '__main__':
  main()
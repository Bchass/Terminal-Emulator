from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QDialog, QFileDialog
import sys
import os
import subprocess
 
class Terminal(QtWidgets.QMainWindow):

    def __init__(self):
        super(Terminal, self).__init__()
        uic.loadUi('gui.ui', self)
       
    
app = QtWidgets.QApplication([])
gui = Terminal()
gui.show()
sys.exit(app.exec())
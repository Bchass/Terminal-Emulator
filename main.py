from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QDialog, QFileDialog
import sys
import os
import subprocess
 
class Terminal(QtWidgets.QMainWindow):

    def __init__(self):
        super(Terminal, self).__init__()
        uic.loadUi('gui.ui', self)
        self.lineEdit.returnPressed.connect(self.Drake)
        self.working_directory = "."

# Drake is just a placeholder for now, till I figure out a better name
    def commands(self):
        commands = self.lineEdit.text()
        
        if "cd" in commands:
            values = commands.split(" ")
            if values[1][0] == "/":
                self.working_directory = values[1]
            else:
                self.working_directory = self.working_directory + "/" + values[1]
        
        print(self.working_directory)

        subprocess.call(commands, shell=True, cwd=self.working_directory)
        
       


app = QtWidgets.QApplication([])
gui = Terminal()
gui.show()
sys.exit(app.exec())
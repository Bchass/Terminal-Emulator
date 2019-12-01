from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QDialog, QFileDialog
import sys
import os
import subprocess
 
class Terminal(QtWidgets.QMainWindow):

    def __init__(self):
        super(Terminal, self).__init__()
        uic.loadUi('gui.ui', self)
        self.lineEdit.returnPressed.connect(self.commands)
        self.working_directory = "."

    def commands(self):
        commands = self.lineEdit.text()
        
        if "cd" in commands:
            values = commands.split(" ")
            if values[1][0] == "/":
                self.working_directory = values[1]
            else:
                self.working_directory = self.working_directory + "/" + values[1]
        
        print(self.working_directory)
        os.system('clear')

        subprocess.call(commands, shell=True, cwd=self.working_directory)

       


app = QtWidgets.QApplication([])
gui = Terminal()
gui.show()
sys.exit(app.exec())
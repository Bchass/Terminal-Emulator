from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QDialog, QFileDialog
import sys
import os
import subprocess as sp

class Terminal(QtWidgets.QMainWindow):

    def __init__(self):
        super(Terminal, self).__init__()
        uic.loadUi('gui.ui', self)
        self.lineEdit.returnPressed.connect(self.commands)
        self.working_directory = "."

    def commands(self):
        commands = self.lineEdit.text()
        os.system('clear') #clear in shell
    
        if "cd" in commands:
            values = commands.split(" ")
            if values[1][0] == "/":
                self.working_directory = values[1]
            else:
                self.working_directory = self.working_directory + "/" + values[1]
    
        print(self.working_directory)

        sp.call(commands,shell=True, cwd=self.working_directory)

        self.textBrowser.setText(self.textBrowser.toPlainText() + "\n➜" + commands) #show input in GUI

    def error(self):
        try:
            output = sp.check_output(commands,shell=True, cwd=self.working_directory) #show output in GUI
            self.textBrowser.setText(self.textBrowser.toPlainText() + "\n" + output.decode('UTF-8'))
        except Exception:
            output = str(output)
        finished = output.split('\n')
        for line in finished:
            print(line)
        return

app = QtWidgets.QApplication([])
gui = Terminal()
gui.show()
sys.exit(app.exec())

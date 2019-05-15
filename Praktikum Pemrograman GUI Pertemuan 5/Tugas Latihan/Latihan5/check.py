import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
		
    def setupUi(self):
        self.resize(300, 100)
        self.move(350, 350)
        self.setWindowTitle(' ')
        self.judul = QCheckBox()
        self.judul.setText('Show Title')
        self.judul.stateChanged.connect(self.okButtonClick)
        layout = QVBoxLayout()
        layout.addWidget(self.judul)
        self.setLayout(layout)
		
    def okButtonClick(self):
        if self.judul.isChecked():
            self.setWindowTitle('Contoh QCheckBox')
        else:
            self.setWindowTitle(' ')
			
if __name__ =='__main__':
  a =QApplication(sys.argv)
  form =MainForm()
  form.show()
  a.exec_()

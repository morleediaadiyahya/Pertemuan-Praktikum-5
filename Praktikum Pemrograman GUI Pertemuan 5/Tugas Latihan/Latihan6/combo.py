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
        self.move(300, 300)
        self.setWindowTitle('Demo QComboBox')
		
        self.combo =QComboBox()
        for i in range(0,6):
            self.combo.addItem('--Pilih Makanan--')
            self.combo.setItemText(1,('Mendoan'))
            self.combo.setItemText(2,('Cireng'))
            self.combo.setItemText(3,('Gethuk'))
            self.combo.setItemText(4,('Tahu Bulat'))
            self.combo.setItemText(5,('Ketan Susu'))
			
        self.combo1 =QComboBox()
        for l in range (0,6):
            self.combo1.addItem('--Pilih Minuman--')
            self.combo1.setItemText(1,('Es Cincau'))
            self.combo1.setItemText(2,('MilkShake'))
            self.combo1.setItemText(3,('Chatime'))
            self.combo1.setItemText(4,('Thaitea'))
            self.combo1.setItemText(5,('Kopi Hitam'))
        self.getTextButton =QPushButton('Pilihan Anda')

        layout =QVBoxLayout()
        layout.addWidget(self.combo)
        layout.addWidget(self.combo1)
        layout.addWidget(self.getTextButton)
        layout.addStretch()
		
        self.setLayout(layout)
        self.getTextButton.clicked.connect(self.getTextButtonClick)
		
    def getTextButtonClick(self):
        QMessageBox.information(self, 'Informasi',
         'Anda memilih: '+self.combo.currentText()+" & "+self.combo1.currentText())
if __name__ =='__main__':
    a =QApplication(sys.argv)
    form =MainForm()
    form.show()
    a.exec_()

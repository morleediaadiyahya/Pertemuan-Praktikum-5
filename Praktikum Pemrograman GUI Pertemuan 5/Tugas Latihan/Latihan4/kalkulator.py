import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        self.resize(400, 150)
        self.move(300, 300)
        self.setWindowTitle('Demo QRadioButton')
        self.text =QLineEdit()
        self.label1 =QLabel()
        self.label1.setText('Bilangan Pertama')
        self.label2 =QLabel()
        self.label2.setText('Bilangan Kedua')
        self.tls =QLineEdit()
        self.tls.setValidator(QIntValidator())

        self.cektambah =QRadioButton()
        self.cektambah.setText('&Tambah')
        self.cektambah.setChecked(True)

        self.cekkurang =QRadioButton()
        self.cekkurang.setText('&Kurang')

        self.cekkali =QRadioButton()
        self.cekkali.setText('&Kali')

        self.cekbagi =QRadioButton()
        self.cekbagi.setText('&Bagi')

        vbox =QGridLayout()
        vbox.addWidget(self.label1,0,0)
        vbox.addWidget(self.text,0,1,1,4)
        vbox.addWidget(self.label2,1,0)
        vbox.addWidget(self.tls,1,1,1,4)
        vbox.addWidget(self.cektambah,2,0)
        vbox.addWidget(self.cekkurang,2,1,1,1)
        vbox.addWidget(self.cekkali,2,2,2,1)
        vbox.addWidget(self.cekbagi,2,3,3,1)
        self.resultLabel =QLabel('<b>Hasil: </b>')
        self.checkButton =QPushButton('Mari Hitung')
        layout =QVBoxLayout()
        layout.addLayout(vbox)
        layout.addWidget(self.resultLabel)
        layout.addWidget(self.checkButton)
        layout.addStretch()
        self.setLayout(layout)
        self.checkButton.clicked.connect(self.checkButtonClick)
    def checkButtonClick(self):
        one = float(self.text.text())
        two = float(self.tls.text())
        if self.cektambah.isChecked():
            res = one+two
            self.resultLabel.setText('<b>Hasil Pertambahan : </b>'+str(res))
        elif self.cekkurang.isChecked():
            res = one - two
            self.resultLabel.setText('<b>Hasil Pengurangan : </b>'+str(res))
        elif self.cekkali.isChecked():
            res = one * two
            self.resultLabel.setText('<b>Hasil Perkalian : </b>'+str(res))
        else:
            res = one / two
            self.resultLabel.setText('<b>Hasil Pembagian : </b>'+str(res))
if __name__ =='__main__':
    a =QApplication(sys.argv)
    form =MainForm()
    form.show()
    a.exec_()

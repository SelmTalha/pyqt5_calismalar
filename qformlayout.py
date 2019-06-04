#QFormLayout():İki sütun formu oluşturmak için uygun bir yoldur.
#Yöntemler ve Tanım:
#addRow(QLabel,QWidget):Etiket ve giriş alanı içeren bir satır ekler.
#addRow(QLabel,QLayout):İkinci sütuna bir alt düzen ekler.
#AddRow(QWidget):Her iki sütunu kapsayan bir widget ekler.
#///////////////////////////////////////////////////////////////
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

def pencere():
    app=QApplication(sys.argv)
    window=QWidget()
    form=QFormLayout()

    form.addRow(QLabel("Adınız:"),QLineEdit()) #addRow(QLabel,QWidget) -> olayına baktık.

#Alt satırda '/' ile biten yere kadarki kodlar addRow(QLabel,QLayout) olay incelemesidir. 
    lb1 = QLabel("Cinsiyetiniz:")
    rdb1= QRadioButton("Erkek")
    rdb2= QRadioButton("Kadın")

    h_box = QHBoxLayout()
    h_box.addWidget(rdb1)
    h_box.addStretch()
    h_box.addWidget(rdb2)

    form.addRow(lb1,h_box)
#/////////////////////////////////////////////////////////////////////////////////////////

    form.addRow(QPushButton("Gönder"))

    window.setLayout(form)

    window.setWindowTitle("QFormLayout")
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    pencere()
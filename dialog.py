from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys 

def pencere():
    app=QApplication(sys.argv)
    pencere=QDialog()
    button1=QPushButton(pencere)
    button1.setText("Tıklama Alanı 1")
    button1.setGeometry(30,50,100,50)

    button2=QPushButton(pencere)
    button2.setText("Tıklama Alanı 2")
    button2.setGeometry(30,150,100,50)

    pencere.setGeometry(100,100,300,300)
    pencere.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    pencere()
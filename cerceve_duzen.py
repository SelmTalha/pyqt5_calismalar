from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

def pencere():
    app=QApplication(sys.argv)
    pencere=QWidget()

    h_box = QHBoxLayout() #Yatay 

    button1=QPushButton(pencere)
    button1.setText("Ekle")

    button2=QPushButton(pencere)
    button2.setText("Ekle 2")

    h_box.addWidget(button1)
    h_box.addWidget(button2)
    pencere.setLayout(h_box)

    pencere.setGeometry(50,50,300,300)
    pencere.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    pencere()
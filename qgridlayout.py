from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

def pencere():
    app=QApplication(sys.argv)
    window=QWidget()
    window.setWindowTitle("QGridLayout(Izgara)")
    
    izgara=QGridLayout()

#//////////////////////////////////////////////////////////////
#Alt kısmı for döngüsü ile kendisinin ayarlamasını sağlayalım !
    # izgara.addWidget(QPushButton("Button 1"),1,1)
    # izgara.addWidget(QPushButton("Button 2"),1,2)
    # izgara.addWidget(QPushButton("Button 3"),2,1)
    # izgara.addWidget(QPushButton("Button 4"),2,2)
    # izgara.addWidget(QPushButton("Button 5"),3,1)
    # izgara.addWidget(QPushButton("Button 6"),3,2)
#///////////////////////////////////////////////////////////////

    for i in range(1,6):
        for j in range(1,6):
            izgara.addWidget(QPushButton("Str:{} Stn:{}".format(i,j)),i,j)
    window.setLayout(izgara)

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    pencere()
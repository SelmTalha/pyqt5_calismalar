from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


def ilk_pencere():
    app=QApplication(sys.argv)
    window=QWidget()
    window.setWindowTitle("Deneme")
    #Bir buton ekleyelim !
    buton = QPushButton(window)
    buton.setGeometry(50,50,100,30)
    buton.setText("Tıkla")
    window.setGeometry(500,200,300,300)
    window.show()
    sys.exit(app.exec_())

ilk_pencere()
    
#main dosyasından çalıştırıldığının kontrolü için aşağıdaki komut yazılır !
# if __name__ == "__main__":
#     ilk_pencere()
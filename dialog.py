from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys 

def pencere():
    app=QApplication(sys.argv)
    pencere=QDialog() #Widget türü bir dialog değişkeni de pencere olsun.

    #Button 1 Tanımlama:
    button1=QPushButton(pencere) # Oluşturulan button'u pencere içine attık.
    button1.setText("Tıklama Alanı 1")
    button1.setGeometry(30,50,100,50)
    button1.clicked.connect(buton1_tiklandi) #Tıklandığında buton1_tiklandi fonk'a git

    #Button 2 Tanımlama:
    button2=QPushButton(pencere)
    button2.setText("Tıklama Alanı 2")
    button2.setGeometry(30,150,100,50)
    button2.clicked.connect(buton2_tiklandi) #Click Event -> buton2_tiklandi fonk'a git

    pencere.setGeometry(100,100,300,300) #dialog widgetinin boyunu ve konumunu ayarla.
    pencere.show() #göster
    pencere.setWindowTitle("Dialog Deneme")

    sys.exit(app.exec_()) 

def buton1_tiklandi():
    print("Buton 1'e tıklandı")

def buton2_tiklandi():
    print("Buton 2'ye tıklandı")

if __name__ == "__main__": #python dosyası main dosyasından(yazıldığı yerden) çağrıldıysa pencere fonk'unu getir!
    pencere()




















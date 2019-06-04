from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

def pencere():
    app=QApplication(sys.argv)
    window=QWidget()
    v_box = QVBoxLayout() #QHBoxLayot'u yan yana yazımda kullanmıştık . Buda dikey kutuda kullanılıyo .

#/////////////////////////////////////////////////////////////////////////////////////////////////////
#Yorum satırındaki gibi yazıldığında iki buttonda window widgetinda aynı yere ilk konuma koyuluyor
#ve iki buton çakıştığı için sadece Buton1 yazısı görünüyor.
#Bu durumdan kurtarmak için QPushButton(window) -> window yerine "string herhangi bir ifade"
#yazarsak bu button'un setText'i oluyo ve çakışma durumu ortadan kalkıyor..

    # button1=QPushButton(window)
    # button1.setText("Buton1")

    # button2=QPushButton(window)
    # button2.setText("Buton2")

#QHBoxLayout = Horizontal = Yatay
#QVBoxLayout = Vertical   = Dikey
#Üst üste gelme (Çakışma durumu QVBoxLayout kullanımında ortaya çıkıyo!)

#/////////////////////////////////////////////////////////////////////////////////////////////////////

    button1=QPushButton("Buton1")

    button2=QPushButton("Buton2")

    v_box.addWidget(button1)
    v_box.addStretch() #"strech" -> İki button arasına eşit mesafeli boşluk oluşturmak için kullanılır.
    v_box.addWidget(button2)

    window.setLayout(v_box)

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    pencere()
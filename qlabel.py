#QLabel = Bir QLabel nesnesi,düzenlenemez metin , resim veya animasyonlu gif filmini görüntülemek için bir yer tutucu görevi görür.

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys 

def Calismam():
    app=QApplication(sys.argv)
    pencere=QWidget()

    label = QLabel("Selim Talha Çağlar")
    label.setAlignment(Qt.AlignCenter) #Alignment ile hizalama yapıyoruz.AlignCenter label'in merkeze sabitlenmesini                                         sağlar.Center yerine sağa ve sola yaslamada yapılabilir. Right - Left
    label.setFont(QFont("Arial",15,QFont.Bold)) #Font ayarlama ve kalınlaştırma 

#////////////////////////////////////////////////////////////////////////////
#Python'da istersek setText içine html kodları ile hrefte verebiliriz.Örnek:
    label2=QLabel()
    label2.setText("<a href=\"www.github.com/SelmTalha\">Github/SelmTalha</a><br><i>Programmer Selim")
    label2.setAlignment(Qt.AlignCenter)
    label2.setFont(QFont("Arial",10,QFont.Bold))
#Uygulamamız en başta linklere kapalı olarak çalışır.O yüzden "Google'a git" linkine tıklasak bile google açılmayacaktır.
#Bunun için setOpenExternalLinks(True) hale getirilmelidir.
    label2.setOpenExternalLinks(True)
#////////////////////////////////////////////////////////////////////////////
    label3=QLabel()
    label3.setPixmap(QPixmap("resim1.jpg"))

    v_box=QVBoxLayout()
    v_box.addWidget(label)
    v_box.addWidget(label3)
    v_box.addWidget(label2)
    
    pencere.setGeometry(530,50,100,200)
    pencere.setLayout(v_box)
    pencere.setWindowTitle("QLabel Çalışması")
    pencere.show()
    sys.exit((app.exec()))

if __name__ == "__main__":
    Calismam()
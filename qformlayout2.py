from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

def pencere():
    app=QApplication(sys.argv)
    window=QWidget()
    form=QFormLayout()

    form.addRow(QLabel("Kullanıcı Adı:"),QLineEdit())
    sifre=QLineEdit()
    sifre.setEchoMode(QLineEdit.Password)
    form.addRow(QLabel("Şifre:"),sifre)
    form.addRow(QLabel("Adres:"),QTextEdit())

    h_box = QHBoxLayout()
    rdb1= QRadioButton("Erkek")
    rdb2= QRadioButton("Kadın")
    h_box.addWidget(rdb1)
    h_box.addWidget(rdb2)

    form.addRow(QLabel("Cinsiyet"),h_box)

    h_box2 = QHBoxLayout()
    btn1 = QPushButton("Gönder")
    btn2 = QPushButton("İptal")
    h_box2.addWidget(btn1)
    h_box2.addWidget(btn2)

    form.addRow(h_box2)

    window.setLayout(form)
    window.setWindowTitle("QFormLayout-2")
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    pencere()
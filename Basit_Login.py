# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arayuz.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(237, 151)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(100, 40, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 40, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Buxton Sketch")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 70, 113, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Buxton Sketch")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.giris)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def giris(self):
        kullanicilar = ["Selim","Murat","Mahmut","Sude","Buse"]
        sifre = ["123","432","333","912","321"]
        kullanici=self.lineEdit.text()
        parola=self.lineEdit_2.text()
        if((kullanici==kullanicilar[0]and parola==sifre[0]) or (kullanici==kullanicilar[1]and parola==sifre[1])
        or(kullanici==kullanicilar[2]and parola==sifre[2]) or (kullanici==kullanicilar[3]and parola==sifre[3])
        or (kullanici==kullanicilar[4]and parola==sifre[4])):
            print("Giriş Başarılı !")
        else:
            print("Hatalı giriş yaptınız!")
            
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Kullanıcı Girişi"))
        self.label.setText(_translate("Form", "Kullanıcı Adı:"))
        self.label_2.setText(_translate("Form", "Şifre:"))
        self.pushButton.setText(_translate("Form", "Giriş"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


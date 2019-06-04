from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

def pencere():
    app=QApplication(sys.argv)
    window=QWidget()

    b1=QPushButton("Buton1")
    b2=QPushButton("Buton2")
    b3=QPushButton("Buton3")
    b4=QPushButton("Buton4")

    v_box=QVBoxLayout()
    h_box=QHBoxLayout()

    v_box.addWidget(b1)
    v_box.addStretch()
    v_box.addWidget(b2)

    h_box.addWidget(b3)
    h_box.addStretch()
    h_box.addWidget(b4)

    v_box.addLayout(h_box)
    window.setLayout(v_box)

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    pencere()
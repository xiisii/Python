import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication,QComboBox, QLabel
import add_rc
class form_coffee(QMainWindow):
    def __init__(self):
        super(form_coffee, self).__init__()
        uic.loadUi('load1.ui',self)
        



app= QApplication(sys.argv)
f12 = form_coffee()
f12.show()
app.exec()

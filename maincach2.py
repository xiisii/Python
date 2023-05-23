import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication,QComboBox, QLabel
import anh1_rc
import anh2_rc
import anhem1_rc
import anhem_rc
import moi1_rc
class cl_Form_10(QMainWindow):
    def __init__(self):
        super(cl_Form_10, self).__init__()
        uic.loadUi('WIDGET1.ui',self)
        

        self.pushButton_2.clicked.connect(self.load_staff)


    def load_staff(self):
        import cach2load1
        f22 = cach2load1.cl_Form_10()
        f22.show() 
        



app= QApplication(sys.argv)
f10 = cl_Form_10()
f10.show()
app.exec()

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication,QComboBox, QLabel
import anh1_rc
import anh2_rc
import anhem1_rc
import anhem_rc
import moi1_rc

class form_main(QMainWindow):
    def __init__(self):
        super(form_main, self).__init__()
        uic.loadUi('WIDGET1.ui',self)
        self.pushButton.clicked.connect(self.load_we)
        self.pushButton_2.clicked.connect(self.load_staff1)

    def load_staff1(self):
        import manhinh1_menu
        load = manhinh1_menu.form_menu()
        load.show()
    def load_we(self):
        import manhinh1_we
        load_1 = manhinh1_we.form_coffee()
        load_1.show()
        

    
        



app= QApplication(sys.argv)
f10 = form_main()
f10.show()
app.exec()

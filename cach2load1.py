import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication,QComboBox, QLabel
class cl_Form_10(QMainWindow):
    def __init__(self):
        self.cout = 0
        self.count_capu = 0
        self.cout_ame = 0
        self.cout_white = 0
        self.cout_black = 0
        self.cout_peach = 0
        self.cout_blue = 0
        self.cout_Mtea = 0
        self.cout_lipton = 0
        self.cout_ora = 0
        self.cout_water = 0
        self.cout_dau = 0
        self.cout_nho = 0

        super(cl_Form_10, self).__init__()
        uic.loadUi('load2_coffee.ui',self)
        self.btn_tea.clicked.connect(lambda: self.tabWidget.setCurrentWidget(self.tab_tea))
        self.btn_coffee.clicked.connect(lambda: self.tabWidget.setCurrentWidget(self.tab_coffee))
        self.btn_juice.clicked.connect(lambda: self.tabWidget.setCurrentWidget(self.tab_juice))
        


    def capuchino(self):
            self.cout +=1
            self.plain_capu.setPlainText(str(self.cout))



        

        

        
            





app= QApplication(sys.argv)
f10 = cl_Form_10()
f10.show()
app.exec()

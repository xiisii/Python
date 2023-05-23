import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication,QComboBox, QLabel
import resource_rc
class form_menu(QMainWindow):
    def __init__(self):
        super(form_menu, self).__init__()
        uic.loadUi('load2_coffee.ui',self)
        self.tong = 0
        self.count_capu =0
        self.count_ame = 0
        self.count_black = 0
        self.count_white = 0
        self.count_peach = 0
        self.count_blue = 0
        self.count_Mtea = 0
        self.count_lipton = 0
        self.count_ora = 0
        self.count_water = 0
        self.count_dau = 0
        self.count_nho = 0

        

        self.btn_add_capu.clicked.connect(self.cong_capu)
        self.btn_add_capu.clicked.connect(self.tongtien)

        self.btn_tru_capu.clicked.connect(self.tru_capu)
        self.btn_tru_capu.clicked.connect(self.tongtien)

        self.btn_add_ame.clicked.connect(self.cong_ame)
        self.btn_add_ame.clicked.connect(self.tongtien)

        self.btn_tru_ame.clicked.connect(self.tru_ame)
        self.btn_tru_ame.clicked.connect(self.tongtien)

        self.btn_add_black.clicked.connect(self.cong_black)
        self.btn_add_black.clicked.connect(self.tongtien)

        self.btn_tru_black.clicked.connect(self.tru_black)
        self.btn_tru_black.clicked.connect(self.tongtien)

        self.btn_add_white.clicked.connect(self.cong_white)
        self.btn_add_white.clicked.connect(self.tongtien)

        self.btn_tru_white.clicked.connect(self.tru_white)
        self.btn_tru_white.clicked.connect(self.tongtien)

        self.btn_add_peach.clicked.connect(self.cong_peach)
        self.btn_add_peach.clicked.connect(self.tongtien)
        self.btn_tru_peach.clicked.connect(self.tru_peach)
        self.btn_tru_peach.clicked.connect(self.tongtien)

        self.btn_add_blue.clicked.connect(self.cong_blue)
        self.btn_add_blue.clicked.connect(self.tongtien)
        self.btn_tru_blue.clicked.connect(self.tru_blue)
        self.btn_tru_blue.clicked.connect(self.tongtien)

        self.btn_add_Mtea.clicked.connect(self.cong_Mtea)
        self.btn_add_Mtea.clicked.connect(self.tongtien)
        self.btn_tru_Mtea.clicked.connect(self.tru_Mtea)
        self.btn_tru_Mtea.clicked.connect(self.tongtien)

        self.btn_add_lipton.clicked.connect(self.cong_lipton)
        self.btn_add_lipton.clicked.connect(self.tongtien)
        self.btn_tru_lipton.clicked.connect(self.tru_lipton)
        self.btn_tru_lipton.clicked.connect(self.tongtien)

        self.btn_add_ora.clicked.connect(self.cong_ora)
        self.btn_add_ora.clicked.connect(self.tongtien)
        self.btn_tru_ora.clicked.connect(self.tru_ora)
        self.btn_tru_ora.clicked.connect(self.tongtien)

        self.btn_add_water.clicked.connect(self.cong_water)
        self.btn_add_water.clicked.connect(self.tongtien)
        self.btn_tru_water.clicked.connect(self.tru_water)
        self.btn_tru_water.clicked.connect(self.tongtien)

        self.btn_add_dau.clicked.connect(self.cong_dau)
        self.btn_add_dau.clicked.connect(self.tongtien)
        self.btn_tru_dau.clicked.connect(self.tru_dau)
        self.btn_tru_dau.clicked.connect(self.tongtien)

        self.btn_add_nho.clicked.connect(self.cong_nho)
        self.btn_add_nho.clicked.connect(self.tongtien)
        self.btn_tru_nho.clicked.connect(self.tru_nho)
        self.btn_tru_nho.clicked.connect(self.tongtien)


        
        self.btn_tea.clicked.connect(lambda: self.tabWidget.setCurrentWidget(self.tab_tea))
        self.btn_coffee.clicked.connect(lambda: self.tabWidget.setCurrentWidget(self.tab_coffee))
        self.btn_juice.clicked.connect(lambda: self.tabWidget.setCurrentWidget(self.tab_juice))
    def cong_capu(self):
        self.count_capu +=1
        self.lb_capu.setText(str(self.count_capu))
    def tru_capu(self):
        self.count_capu -=1
        self.lb_capu.setText(str(self.count_capu))


    def cong_ame(self):
        self.count_ame +=1
        self.label_38.setText(str(self.count_ame))
    def tru_ame(self):
        self.count_ame -=1
        self.label_38.setText(str(self.count_ame))


    def cong_black(self):
        self.count_black +=1
        self.lb_black.setText(str(self.count_black))
    def tru_black(self):
        self.count_black -=1
        self.lb_black.setText(str(self.count_black))


    def cong_white(self):
        self.count_white +=1
        self.label_41.setText(str(self.count_white))
    def tru_white(self):
        self.count_white -=1
        self.label_41.setText(str(self.count_white))


    def cong_peach(self):
        self.count_peach +=1
        self.label_39.setText(str(self.count_peach))
    def tru_peach(self):
        self.count_peach -=1
        self.label_39.setText(str(self.count_peach))

    def cong_blue(self):
        self.count_blue +=1
        self.label_44.setText(str(self.count_blue))
    def tru_blue(self):
        self.count_blue -=1
        self.label_44.setText(str(self.count_blue))

    def cong_Mtea(self):
        self.count_Mtea +=1
        self.label_42.setText(str(self.count_Mtea))
    def tru_Mtea(self):
        self.count_Mtea -=1
        self.label_42.setText(str(self.count_Mtea))

    def cong_lipton(self):
        self.count_lipton +=1
        self.label_43.setText(str(self.count_lipton))
    def tru_lipton(self):
        self.count_lipton -=1
        self.label_43.setText(str(self.count_lipton))


    def cong_ora(self):
        self.count_ora +=1
        self.label_45.setText(str(self.count_ora))
    def tru_ora(self):
        self.count_ora -=1
        self.label_45.setText(str(self.count_ora))


    def cong_water(self):
        self.count_water +=1
        self.label_47.setText(str(self.count_water))
    def tru_water(self):
        self.count_water -=1
        self.label_47.setText(str(self.count_water))


    def cong_dau(self):
        self.count_dau +=1
        self.label_46.setText(str(self.count_dau))
    def tru_dau(self):
        self.count_dau -=1
        self.label_46.setText(str(self.count_dau))


    def cong_nho(self):
        self.count_nho +=1
        self.label_48.setText(str(self.count_nho))
    def tru_nho(self):
        self.count_nho -=1
        self.label_48.setText(str(self.count_nho))


    def tongtien(self):
        self.tong = (12 * self.count_capu)+(10 * self.count_ame) +(6*self.count_black)+(8 * self.count_white) +(10*self.count_peach)+(10*self.count_blue)+(10*self.count_Mtea)+(10*self.count_lipton)+(15*self.count_ora)+(15* self.count_water)+(15*self.count_dau)+(15*self.count_nho)
        self.plain_tong.setPlainText(str(self.tong))
        



app= QApplication(sys.argv)
f11 = form_menu()
f11.show()
app.exec()

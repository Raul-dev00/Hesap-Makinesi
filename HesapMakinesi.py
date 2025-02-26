from PyQt5 import QtCore, QtGui, QtWidgets

sayilar = []
class Ui_HesapMakinesi(object):
    def setupUi(self, HesapMakinesi):
        HesapMakinesi.setObjectName("HesapMakinesi")
        HesapMakinesi.resize(411, 489)
        self.centralwidget = QtWidgets.QWidget(HesapMakinesi)
        self.centralwidget.setObjectName("centralwidget")
        self.Button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_1.setGeometry(QtCore.QRect(10, 150, 93, 70))
        self.Button_1.setIconSize(QtCore.QSize(20, 20))
        self.Button_1.setObjectName("Button_1")
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_2.setGeometry(QtCore.QRect(110, 150, 93, 70))
        self.Button_2.setObjectName("Button_2")
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_3.setGeometry(QtCore.QRect(210, 150, 93, 70))
        self.Button_3.setObjectName("Button_3")
        self.Button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_4.setGeometry(QtCore.QRect(10, 230, 93, 70))
        self.Button_4.setObjectName("Button_4")
        self.Button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_5.setGeometry(QtCore.QRect(110, 230, 93, 70))
        self.Button_5.setObjectName("Button_5")
        self.Button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_6.setGeometry(QtCore.QRect(210, 230, 93, 70))
        self.Button_6.setObjectName("Button_6")
        self.Button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_7.setGeometry(QtCore.QRect(10, 310, 93, 70))
        self.Button_7.setObjectName("Button_7")
        self.Button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_8.setGeometry(QtCore.QRect(110, 310, 93, 70))
        self.Button_8.setObjectName("Button_8")
        self.Button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_9.setGeometry(QtCore.QRect(210, 310, 93, 70))
        self.Button_9.setObjectName("Button_9")
        self.Button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_0.setGeometry(QtCore.QRect(10, 390, 93, 70))
        self.Button_0.setObjectName("Button_0")
        self.Button_equal = QtWidgets.QPushButton(self.centralwidget)
        self.Button_equal.setGeometry(QtCore.QRect(110, 390, 191, 70))
        self.Button_equal.setObjectName("Button_equal")
        self.Button_sum = QtWidgets.QPushButton(self.centralwidget)
        self.Button_sum.setGeometry(QtCore.QRect(310, 150, 93, 70))
        self.Button_sum.setObjectName("Button_sum")
        self.Button_minus = QtWidgets.QPushButton(self.centralwidget)
        self.Button_minus.setGeometry(QtCore.QRect(310, 230, 93, 70))
        self.Button_minus.setObjectName("Button_minus")
        self.Button_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.Button_multiply.setGeometry(QtCore.QRect(310, 310, 93, 70))
        self.Button_multiply.setObjectName("Button_multiply")
        self.Button_divide = QtWidgets.QPushButton(self.centralwidget)
        self.Button_divide.setGeometry(QtCore.QRect(310, 390, 93, 70))
        self.Button_divide.setObjectName("Button_divide")
        self.hesapMakinesiEkran = QtWidgets.QLineEdit(self.centralwidget)
        self.hesapMakinesiEkran.setGeometry(QtCore.QRect(22, 60, 371, 51))
        self.hesapMakinesiEkran.setObjectName("hesapMakinesiEkran")
        self.hesapMakinesiEkran.setStyleSheet("font-size: 35px;")
        HesapMakinesi.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(HesapMakinesi)
        self.statusbar.setObjectName("statusbar")
        HesapMakinesi.setStatusBar(self.statusbar)

        self.retranslateUi(HesapMakinesi)
        QtCore.QMetaObject.connectSlotsByName(HesapMakinesi)
        self.Button_1.clicked.connect(self.Button_1_clicked)
        self.Button_2.clicked.connect(self.Button_2_clicked)
        self.Button_3.clicked.connect(self.Button_3_clicked)
        self.Button_4.clicked.connect(self.Button_4_clicked)
        self.Button_5.clicked.connect(self.Button_5_clicked)
        self.Button_6.clicked.connect(self.Button_6_clicked)
        self.Button_7.clicked.connect(self.Button_7_clicked)
        self.Button_8.clicked.connect(self.Button_8_clicked)
        self.Button_9.clicked.connect(self.Button_9_clicked)
        self.Button_0.clicked.connect(self.Button_0_clicked)
        self.Button_sum.clicked.connect(self.Button_sum_clicked)
        self.Button_minus.clicked.connect(self.Button_minus_clicked)
        self.Button_multiply.clicked.connect(self.Button_multiply_clicked)
        self.Button_divide.clicked.connect(self.Button_divide_clicked)
        self.Button_equal.clicked.connect(self.Button_equal_clicked)
        self.Button_equal.mouseDoubleClickEvent = self.on_double_click

    def retranslateUi(self, HesapMakinesi):
        _translate = QtCore.QCoreApplication.translate
        HesapMakinesi.setWindowTitle(_translate("HesapMakinesi", "Hesap Makinesi"))
        self.Button_1.setText(_translate("HesapMakinesi", "1"))
        self.Button_2.setText(_translate("HesapMakinesi", "2"))
        self.Button_3.setText(_translate("HesapMakinesi", "3"))
        self.Button_4.setText(_translate("HesapMakinesi", "4"))
        self.Button_5.setText(_translate("HesapMakinesi", "5"))
        self.Button_6.setText(_translate("HesapMakinesi", "6"))
        self.Button_7.setText(_translate("HesapMakinesi", "7"))
        self.Button_8.setText(_translate("HesapMakinesi", "8"))
        self.Button_9.setText(_translate("HesapMakinesi", "9"))
        self.Button_0.setText(_translate("HesapMakinesi", "0"))
        self.Button_equal.setText(_translate("HesapMakinesi", "="))
        self.Button_sum.setText(_translate("HesapMakinesi", "+"))
        self.Button_minus.setText(_translate("HesapMakinesi", "-"))
        self.Button_multiply.setText(_translate("HesapMakinesi", "*"))
        self.Button_divide.setText(_translate("HesapMakinesi", "/"))

    def Button_1_clicked(self):
        self.hesapMakinesiEkran.insert("1")
        sayilar.append(1)
    def Button_2_clicked(self):
        self.hesapMakinesiEkran.insert("2")
        sayilar.append(2)
    def Button_3_clicked(self):
        self.hesapMakinesiEkran.insert("3")
        sayilar.append(3)
    def Button_4_clicked(self):
        self.hesapMakinesiEkran.insert("4")
        sayilar.append(4)
    def Button_5_clicked(self):
        self.hesapMakinesiEkran.insert("5")
        sayilar.append(5)
    def Button_6_clicked(self):
        self.hesapMakinesiEkran.insert("6")
        sayilar.append(6)
    def Button_7_clicked(self):
        self.hesapMakinesiEkran.insert("7")
        sayilar.append(7)
    def Button_8_clicked(self):
        self.hesapMakinesiEkran.insert("8")
        sayilar.append(8)
    def Button_9_clicked(self):
        self.hesapMakinesiEkran.insert("9")
        sayilar.append(9)
    def Button_0_clicked(self):
        self.hesapMakinesiEkran.insert("0")
        sayilar.append(0)
    def Button_sum_clicked(self):
        self.hesapMakinesiEkran.insert("+")
        sayilar.append("+")
    def Button_minus_clicked(self):
        self.hesapMakinesiEkran.insert("-")
        sayilar.append("-")
    def Button_multiply_clicked(self):
        self.hesapMakinesiEkran.insert("*")
        sayilar.append("*")
    def Button_divide_clicked(self):
        self.hesapMakinesiEkran.insert("/")
        sayilar.append("/")
    def Button_equal_clicked(self):
        sayilar_ters = list(reversed(sayilar))
        sayi1 = 0
        sayi2 = 0
        control = 1
        y = None
        bool = True
        for x in sayilar_ters:
            if x == "+" or x == "-" or x == "*" or x == "/":
                y = x
                bool = False
                control = 1
                continue
            if bool == True:
                sayi2 += x*control
                control *= 10
            if bool == False:
                sayi1 += x*control
                control *= 10
        if y == "+":
            answer_sum = sayi1 + sayi2
            self.hesapMakinesiEkran.setText(str(answer_sum))
        if y == "-":
            answer_minus = sayi1 - sayi2
            self.hesapMakinesiEkran.setText(str(answer_minus))
        if y == "*":
            answer_multiply = sayi1 * sayi2
            self.hesapMakinesiEkran.setText(str(answer_multiply))
        if y == "/":
            if sayi2 == 0:
                self.hesapMakinesiEkran.setText("HATA!")
            else:
                answer_divide = sayi1 / sayi2
                self.hesapMakinesiEkran.setText(str(answer_divide))

    def on_double_click(self, event):
        self.hesapMakinesiEkran.setText("")
        sayilar.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HesapMakinesi = QtWidgets.QMainWindow()
    ui = Ui_HesapMakinesi()
    ui.setupUi(HesapMakinesi)
    HesapMakinesi.show()
    sys.exit(app.exec_())

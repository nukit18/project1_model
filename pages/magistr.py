from PyQt5 import QtCore, QtGui, QtWidgets
from pages import start_win, specialist, bakalavr, final_win


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 1024)
        MainWindow.setMinimumSize(QtCore.QSize(1440, 1024))
        MainWindow.setMaximumSize(QtCore.QSize(1440, 1024))
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255)")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(426, 0, 621, 186))
        self.label.setStyleSheet("position: absolute;\n"
"width: 588px;\n"
"height: 186px;\n"
"left: 426px;\n"
"top: 0px;\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 96px;\n"
"line-height: 112px;\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"color: #000000;\n"
"")
        self.label.setObjectName("label")
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(470, 750, 500, 140))
        self.back_btn.setStyleSheet("background: #ff0000;\n"
"border-radius: 70px;\n"
"position: absolute;\n"
"width: 58px;\n"
"height: 18px;\n"
"left: 10px;\n"
"top: 10px;\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 76px;\n"
"line-height: 112px;\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"color: #FFFFFF;")
        self.back_btn.setObjectName("back_btn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(245, 400, 950, 186))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("position: absolute;\n"
"width: 588px;\n"
"height: 186px;\n"
"left: 426px;\n"
"top: 0px;\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 96px;\n"
"line-height: 112px;\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"color: #000000;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # обработчик нажатий
        self.add_functions(MainWindow)

    def add_functions(self, MainWindow):
        self.back_btn.clicked.connect(lambda: self.back_click(MainWindow))

    def back_click(self, MainWindow):
        ui = start_win.Ui_MainWindow()
        ui.setupUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Win1"))
        self.label.setText(_translate("MainWindow", "Магистратура"))
        self.back_btn.setText(_translate("MainWindow", "Назад"))
        self.label_2.setText(_translate("MainWindow", "Вам в кабинет №228"))

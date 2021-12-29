from PyQt5 import QtCore, QtGui, QtWidgets
from pages import start_win, bakalavr, magistr, final_win


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
        self.debts_btn = QtWidgets.QPushButton(self.centralwidget)
        self.debts_btn.setGeometry(QtCore.QRect(34, 207, 519, 148))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.debts_btn.setFont(font)
        self.debts_btn.setStyleSheet("background: #4052EF;\n"
"border-radius: 70px;\n"
"position: absolute;\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 72px;\n"
"line-height: 84px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.debts_btn.setIconSize(QtCore.QSize(676, 186))
        self.debts_btn.setDefault(False)
        self.debts_btn.setFlat(False)
        self.debts_btn.setObjectName("debts_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(426, 0, 588, 186))
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
        self.back_btn.setGeometry(QtCore.QRect(20, 30, 131, 51))
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
"font-size: 36px;\n"
"line-height: 112px;\n"
"display: flex;\n"
"align-items: center;\n"
"\n"
"color: #FFFFFF;")
        self.back_btn.setObjectName("back_btn")
        self.locate_btn = QtWidgets.QPushButton(self.centralwidget)
        self.locate_btn.setGeometry(QtCore.QRect(34, 395, 519, 148))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.locate_btn.setFont(font)
        self.locate_btn.setStyleSheet("background: #4052EF;\n"
"border-radius: 70px;\n"
"position: absolute;\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 72px;\n"
"line-height: 84px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.locate_btn.setIconSize(QtCore.QSize(676, 186))
        self.locate_btn.setDefault(False)
        self.locate_btn.setFlat(False)
        self.locate_btn.setObjectName("locate_btn")
        self.schedule_btn = QtWidgets.QPushButton(self.centralwidget)
        self.schedule_btn.setGeometry(QtCore.QRect(34, 583, 519, 148))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.schedule_btn.setFont(font)
        self.schedule_btn.setStyleSheet("background: #4052EF;\n"
"border-radius: 70px;\n"
"position: absolute;\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 72px;\n"
"line-height: 84px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.schedule_btn.setIconSize(QtCore.QSize(676, 186))
        self.schedule_btn.setDefault(False)
        self.schedule_btn.setFlat(False)
        self.schedule_btn.setObjectName("schedule_btn")
        self.recovery_btn = QtWidgets.QPushButton(self.centralwidget)
        self.recovery_btn.setGeometry(QtCore.QRect(34, 771, 519, 148))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.recovery_btn.setFont(font)
        self.recovery_btn.setStyleSheet("background: #4052EF;\n"
"border-radius: 70px;\n"
"position: absolute;\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 64px;\n"
"line-height: 84px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.recovery_btn.setIconSize(QtCore.QSize(676, 186))
        self.recovery_btn.setDefault(False)
        self.recovery_btn.setFlat(False)
        self.recovery_btn.setObjectName("recovery_btn")
        self.transfer_btn = QtWidgets.QPushButton(self.centralwidget)
        self.transfer_btn.setGeometry(QtCore.QRect(860, 207, 519, 148))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.transfer_btn.setFont(font)
        self.transfer_btn.setStyleSheet("background: #4052EF;\n"
"border-radius: 70px;\n"
"position: absolute;\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 72px;\n"
"line-height: 84px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.transfer_btn.setIconSize(QtCore.QSize(676, 186))
        self.transfer_btn.setDefault(False)
        self.transfer_btn.setFlat(False)
        self.transfer_btn.setObjectName("transfer_btn")
        self.akadem_btn = QtWidgets.QPushButton(self.centralwidget)
        self.akadem_btn.setGeometry(QtCore.QRect(860, 395, 519, 148))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.akadem_btn.setFont(font)
        self.akadem_btn.setStyleSheet("background: #4052EF;\n"
"border-radius: 70px;\n"
"position: absolute;\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 64px;\n"
"line-height: 84px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.akadem_btn.setIconSize(QtCore.QSize(676, 186))
        self.akadem_btn.setDefault(False)
        self.akadem_btn.setFlat(False)
        self.akadem_btn.setObjectName("akadem_btn")
        self.doc_btn = QtWidgets.QPushButton(self.centralwidget)
        self.doc_btn.setGeometry(QtCore.QRect(860, 583, 519, 148))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.doc_btn.setFont(font)
        self.doc_btn.setStyleSheet("background: #4052EF;\n"
"border-radius: 70px;\n"
"position: absolute;\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 64px;\n"
"line-height: 84px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.doc_btn.setIconSize(QtCore.QSize(676, 186))
        self.doc_btn.setDefault(False)
        self.doc_btn.setFlat(False)
        self.doc_btn.setObjectName("doc_btn")
        self.general_btn = QtWidgets.QPushButton(self.centralwidget)
        self.general_btn.setGeometry(QtCore.QRect(860, 771, 519, 148))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.general_btn.setFont(font)
        self.general_btn.setStyleSheet("background: #4052EF;\n"
"border-radius: 70px;\n"
"position: absolute;\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 72px;\n"
"line-height: 84px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.general_btn.setIconSize(QtCore.QSize(676, 186))
        self.general_btn.setDefault(False)
        self.general_btn.setFlat(False)
        self.general_btn.setObjectName("general_btn")
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
        self.debts_btn.clicked.connect(lambda: self.next_click(MainWindow, self.debts_btn.text()))
        self.locate_btn.clicked.connect(lambda: self.next_click(MainWindow, self.locate_btn.text()))
        self.schedule_btn.clicked.connect(lambda: self.next_click(MainWindow, self.schedule_btn.text()))
        self.recovery_btn.clicked.connect(lambda: self.next_click(MainWindow, self.recovery_btn.text()))
        self.transfer_btn.clicked.connect(lambda: self.next_click(MainWindow, self.transfer_btn.text()))
        self.akadem_btn.clicked.connect(lambda: self.next_click(MainWindow, self.akadem_btn.text().replace("\n", " ")))
        self.doc_btn.clicked.connect(lambda: self.next_click(MainWindow, self.doc_btn.text().replace("\n", " ")))
        self.general_btn.clicked.connect(lambda: self.next_click(MainWindow, self.general_btn.text()))

    def back_click(self, MainWindow):
        ui = start_win.Ui_MainWindow()
        ui.setupUi(MainWindow)

    def next_click(self, MainWindow, text_btn):
        ui = final_win.Ui_MainWindow()
        ui.setupUi(MainWindow, text_btn)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Win1"))
        self.debts_btn.setText(_translate("MainWindow", "Долги"))
        self.label.setText(_translate("MainWindow", "Специалитет"))
        self.back_btn.setText(_translate("MainWindow", "Назад"))
        self.locate_btn.setText(_translate("MainWindow", "Поселение"))
        self.schedule_btn.setText(_translate("MainWindow", "Расписание"))
        self.recovery_btn.setText(_translate("MainWindow", "Восстановление"))
        self.transfer_btn.setText(_translate("MainWindow", "Перевод"))
        self.akadem_btn.setText(_translate("MainWindow", "Академический\n"
"отпуск"))
        self.doc_btn.setText(_translate("MainWindow", "Документы и\n"
"финансы"))
        self.general_btn.setText(_translate("MainWindow", "Общие"))

from pages import start_win, specialist, magistr, final_win
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 1024)
        MainWindow.setMinimumSize(QtCore.QSize(1440, 1024))
        MainWindow.setMaximumSize(QtCore.QSize(1440, 1024))
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
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
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 150, 1440, 874))
        self.scrollArea.setMinimumSize(QtCore.QSize(1440, 874))
        self.scrollArea.setMaximumSize(QtCore.QSize(1440, 874))
        self.scrollArea.setStyleSheet("QScrollBar:vertical {\n"
"            border: 0px solid #c6c6c6;\n"
"            background: transparent;\n"
"            width: 25px;    \n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"QScrollBar:horizontal {\n"
"            border: 0px solid #c6c6c6;\n"
"            background: transparent;\n"
"            height: 13px;    \n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::handle {\n"
"            background: #c6c6c6;\n"
"            border: 0px solid 1;\n"
"            border-radius: 6px;\n"
"        }\n"
"        QScrollBar::add-line:vertical {\n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::add-line:horizontal {\n"
"            width: 0px;\n"
"            subcontrol-position: right;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:horizontal {\n"
"            width: 0 px;\n"
"            subcontrol-position: left;\n"
"            subcontrol-origin: margin;\n"
"        }")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1413, 2918))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(0, 2900))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_OIS = QtWidgets.QPushButton(self.frame)
        self.btn_OIS.setGeometry(QtCore.QRect(150, 50, 1100, 250))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_OIS.setFont(font)
        self.btn_OIS.setStyleSheet("background: #4052EF;\n"
"border-radius: 70px;\n"
"position: absolute;\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 50px;\n"
"line-height: 84px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.btn_OIS.setIconSize(QtCore.QSize(676, 186))
        self.btn_OIS.setDefault(False)
        self.btn_OIS.setFlat(False)
        self.btn_OIS.setObjectName("btn_OIS")
        self.btn_DAA = QtWidgets.QPushButton(self.frame)
        self.btn_DAA.setGeometry(QtCore.QRect(150, 350, 1100, 300))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_DAA.setFont(font)
        self.btn_DAA.setStyleSheet("background: #4052EF;\n"
"border-radius: 70px;\n"
"position: absolute;\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 50px;\n"
"line-height: 84px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.btn_DAA.setIconSize(QtCore.QSize(676, 186))
        self.btn_DAA.setDefault(False)
        self.btn_DAA.setFlat(False)
        self.btn_DAA.setObjectName("btn_DAA")
        self.btn_KMS = QtWidgets.QPushButton(self.frame)
        self.btn_KMS.setGeometry(QtCore.QRect(150, 700, 1100, 250))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_KMS.setFont(font)
        self.btn_KMS.setStyleSheet("background: #4052EF;\n"
"border-radius: 70px;\n"
"position: absolute;\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 50px;\n"
"line-height: 84px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.btn_KMS.setIconSize(QtCore.QSize(676, 186))
        self.btn_KMS.setDefault(False)
        self.btn_KMS.setFlat(False)
        self.btn_KMS.setObjectName("btn_KMS")
        self.btn_HEA = QtWidgets.QPushButton(self.frame)
        self.btn_HEA.setGeometry(QtCore.QRect(150, 1000, 1100, 250))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_HEA.setFont(font)
        self.btn_HEA.setStyleSheet("background: #4052EF;\n"
"border-radius: 70px;\n"
"position: absolute;\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 50px;\n"
"line-height: 84px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.btn_HEA.setIconSize(QtCore.QSize(676, 186))
        self.btn_HEA.setDefault(False)
        self.btn_HEA.setFlat(False)
        self.btn_HEA.setObjectName("btn_HEA")
        self.btn_AIV = QtWidgets.QPushButton(self.frame)
        self.btn_AIV.setGeometry(QtCore.QRect(150, 1300, 1100, 250))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_AIV.setFont(font)
        self.btn_AIV.setStyleSheet("background: #4052EF;\n"
"border-radius: 70px;\n"
"position: absolute;\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 50px;\n"
"line-height: 84px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.btn_AIV.setIconSize(QtCore.QSize(676, 186))
        self.btn_AIV.setDefault(False)
        self.btn_AIV.setFlat(False)
        self.btn_AIV.setObjectName("btn_AIV")
        self.btn_VAV = QtWidgets.QPushButton(self.frame)
        self.btn_VAV.setGeometry(QtCore.QRect(150, 1600, 1100, 250))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_VAV.setFont(font)
        self.btn_VAV.setStyleSheet("background: #4052EF;\n"
"border-radius: 70px;\n"
"position: absolute;\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 50px;\n"
"line-height: 84px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.btn_VAV.setIconSize(QtCore.QSize(676, 186))
        self.btn_VAV.setDefault(False)
        self.btn_VAV.setFlat(False)
        self.btn_VAV.setObjectName("btn_VAV")
        self.btn_KNG = QtWidgets.QPushButton(self.frame)
        self.btn_KNG.setGeometry(QtCore.QRect(150, 1900, 1100, 250))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_KNG.setFont(font)
        self.btn_KNG.setStyleSheet("background: #4052EF;\n"
"border-radius: 70px;\n"
"position: absolute;\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 50px;\n"
"line-height: 84px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.btn_KNG.setIconSize(QtCore.QSize(676, 186))
        self.btn_KNG.setDefault(False)
        self.btn_KNG.setFlat(False)
        self.btn_KNG.setObjectName("btn_KNG")
        self.btn_TLN = QtWidgets.QPushButton(self.frame)
        self.btn_TLN.setGeometry(QtCore.QRect(150, 2200, 1100, 250))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_TLN.setFont(font)
        self.btn_TLN.setStyleSheet("background: #4052EF;\n"
"border-radius: 70px;\n"
"position: absolute;\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 50px;\n"
"line-height: 84px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.btn_TLN.setIconSize(QtCore.QSize(676, 186))
        self.btn_TLN.setDefault(False)
        self.btn_TLN.setFlat(False)
        self.btn_TLN.setObjectName("btn_TLN")
        self.btn_KNA = QtWidgets.QPushButton(self.frame)
        self.btn_KNA.setGeometry(QtCore.QRect(150, 2500, 1100, 250))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_KNA.setFont(font)
        self.btn_KNA.setStyleSheet("background: #4052EF;\n"
"border-radius: 70px;\n"
"position: absolute;\n"
"\n"
"font-family: Roboto;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 50px;\n"
"line-height: 84px;\n"
"display: flex;\n"
"align-items: center;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.btn_KNA.setIconSize(QtCore.QSize(676, 186))
        self.btn_KNA.setDefault(False)
        self.btn_KNA.setFlat(False)
        self.btn_KNA.setObjectName("btn_KNA")
        self.verticalLayout.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.add_functions(MainWindow)

    def add_functions(self, MainWindow):
        self.back_btn.clicked.connect(lambda: self.back_click(MainWindow))
        self.btn_OIS.clicked.connect(lambda: self.next_click(MainWindow, "Орехова И.С."))
        self.btn_DAA.clicked.connect(lambda: self.next_click(MainWindow, "Данилова А.А."))
        self.btn_KMS.clicked.connect(lambda: self.next_click(MainWindow, "Курочкина М.С."))
        self.btn_HEA.clicked.connect(lambda: self.next_click(MainWindow, "Худякова Е.А."))
        self.btn_AIV.clicked.connect(lambda: self.next_click(MainWindow, "Антропова И.В."))
        self.btn_VAV.clicked.connect(lambda: self.next_click(MainWindow, "Волкова А.В."))
        self.btn_KNG.clicked.connect(lambda: self.next_click(MainWindow, "Кийко Н.Г."))
        self.btn_TLN.clicked.connect(lambda: self.next_click(MainWindow, "Тараненко Л.Н."))
        self.btn_KNA.clicked.connect(lambda: self.next_click(MainWindow, "Козырева Н.А."))

    def back_click(self, MainWindow):
        ui = start_win.Ui_MainWindow()
        ui.setupUi(MainWindow)

    def next_click(self, MainWindow, text_btn):
        ui = final_win.Ui_MainWindow()
        ui.setupUi(MainWindow, text_btn)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Win1"))
        self.label.setText(_translate("MainWindow", "Бакалавриат"))
        self.back_btn.setText(_translate("MainWindow", "Назад"))
        self.btn_OIS.setText(_translate("MainWindow", 'Орехова Ирина Сергеевна\n'
"Подписание док-ов,\n"
"создание списков на стипендии,\n"
"общие вопросы"))
        self.btn_DAA.setText(_translate("MainWindow", "Данилова Анна Андреевна\n"
"Обеспечение движения контингента,\n"
"подготовка справок о согласии на перевод,\n"
"подготовка справок об обучении,\n"
"проставление оценок в БРС"))
        self.btn_KMS.setText(_translate("MainWindow", "Курочкина Марина Сергеевна\n"
"Вопросы по экзаменам, поселение студентов,\n"
"выдача студика и пропуска,\n"
"вопросы по учебе"))
        self.btn_HEA.setText(_translate("MainWindow", "Худякова Елена Алексеевна\n"
"Вопросы по экзаменам, вопросы по учебе"))
        self.btn_AIV.setText(_translate("MainWindow", "Антропова Ирина Викторовна\n"
"Выдача справок, работа с заболевшими Covid,\n"
"работа с иностранными студентами, заочники"))
        self.btn_VAV.setText(_translate("MainWindow", "Волкова Анна Владимировна\n"
"Успеваемость на онлайн-курсах и майнорах,\n"
"выгрузка НТК"))
        self.btn_KNG.setText(_translate("MainWindow", "Кийко Наталья Григорьевна\n"
"Формирование расписания и\n"
"графика пересдач"))
        self.btn_TLN.setText(_translate("MainWindow", "Тараненко Лидия Николаевна\n"
"Формирование расписания ИОТ и\n"
"графика пересдач"))
        self.btn_KNA.setText(_translate("MainWindow", "Козырева Наталья Андреевна\n"
"Льготники, назначение стипендий,\n"
"назначение мат. помощи"))
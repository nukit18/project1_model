import asyncio
import random

from PyQt5 import QtCore, QtGui, QtWidgets

from db_api.quick_cmd import get_id_by_name, get_last_queue, get_start_talon, get_name_and_num_win, add_to_queue, \
    update_new_queue, get_len_queue, read_new_queue, on_reception_get, on_reception_add
from pages import start_win, specialist, bakalavr, magistr
from server import send_response


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, text_btn):
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
        self.label.setGeometry(QtCore.QRect(-11, -22, 1509, 315))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.MarkdownText)
        self.label.setPixmap(QtGui.QPixmap("../фон.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.ok_btn = QtWidgets.QPushButton(self.centralwidget)
        self.ok_btn.setGeometry(QtCore.QRect(71, 795, 507, 152))
        self.ok_btn.setStyleSheet("background: #0C9700;\n"
                                  "border-radius: 40px;\n"
                                  "\n"
                                  "font-family: Roboto;\n"
                                  "font-style: normal;\n"
                                  "font-weight: normal;\n"
                                  "font-size: 90px;\n"
                                  "line-height: 112px;\n"
                                  "display: flex;\n"
                                  "align-items: center;\n"
                                  "text-align: center;\n"
                                  "\n"
                                  "color: #FFFFFF;")
        self.ok_btn.setObjectName("ok_btn")
        self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_btn.setGeometry(QtCore.QRect(856, 795, 507, 152))
        self.cancel_btn.setStyleSheet("background: #A90D0D;\n"
                                      "border-radius: 40px;\n"
                                      "\n"
                                      "font-family: Roboto;\n"
                                      "font-style: normal;\n"
                                      "font-weight: normal;\n"
                                      "font-size: 90px;\n"
                                      "line-height: 112px;\n"
                                      "display: flex;\n"
                                      "align-items: center;\n"
                                      "text-align: center;\n"
                                      "\n"
                                      "color: #FFFFFF;")
        self.cancel_btn.setObjectName("cancel_btn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 300, 1440, 131))
        self.label_2.setStyleSheet("font-family: Roboto;\n"
                                   "font-style: normal;\n"
                                   "font-weight: normal;\n"
                                   "font-size: 90px;\n"
                                   "line-height: 112px;\n"
                                   "display: flex;\n"
                                   "align-items: center;\n"
                                   "text-align: center;\n"
                                   "\n"
                                   "color: #000000;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 440, 1440, 131))
        self.label_3.setStyleSheet("font-family: Roboto;\n"
                                   "font-style: normal;\n"
                                   "font-weight: normal;\n"
                                   "font-size: 90px;\n"
                                   "line-height: 112px;\n"
                                   "display: flex;\n"
                                   "align-items: center;\n"
                                   "text-align: center;\n"
                                   "\n"
                                   "color: #000000;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 560, 1440, 131))
        self.label_5.setStyleSheet("font-family: Roboto;\n"
                                   "font-style: normal;\n"
                                   "font-weight: normal;\n"
                                   "font-size: 90px;\n"
                                   "line-height: 112px;\n"
                                   "display: flex;\n"
                                   "align-items: center;\n"
                                   "text-align: center;\n"
                                   "\n"
                                   "color: #000000;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.cancel_btn.raise_()
        self.ok_btn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        loop = asyncio.get_event_loop()
        id_spec = loop.run_until_complete(get_id_by_name(text_btn))
        talon_num = loop.run_until_complete(get_last_queue(id_spec))
        start_talon = loop.run_until_complete(get_start_talon(id_spec))
        name_and_numwin = loop.run_until_complete(get_name_and_num_win(id_spec))
        talon = start_talon + str(talon_num)
        self.label_2.setText("Ваш талон №" + talon)
        self.label_5.setText("Окно: " + str(name_and_numwin[1]))
        self.label_3.setText("Специалист: " + str(name_and_numwin[0]))
        # обработчик нажатий
        self.add_functions(MainWindow, id_spec, talon)

    def add_functions(self, MainWindow, id_spec, talon):
        self.ok_btn.clicked.connect(lambda: self.ok_click(MainWindow, id_spec, talon))
        self.cancel_btn.clicked.connect(lambda: self.cancel_click(MainWindow))

    def cancel_click(self, MainWindow):
        ui = start_win.Ui_MainWindow()
        ui.setupUi(MainWindow)

    def ok_click(self, MainWindow, id_spec, talon):
        global new_queue
        loop = asyncio.get_event_loop()
        if loop.run_until_complete(on_reception_get(id_spec)) == "0":
            loop.run_until_complete(add_to_queue(id_spec))
            loop.run_until_complete(update_new_queue(id_spec))
            loop.run_until_complete(on_reception_add(id_spec, talon))
        else:
            loop.run_until_complete(add_to_queue(id_spec))
        ui = start_win.Ui_MainWindow()
        ui.setupUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Win1"))
        self.ok_btn.setText(_translate("MainWindow", "Ок"))
        self.cancel_btn.setText(_translate("MainWindow", "Отмена"))
        # self.label_2.setText(_translate("MainWindow", "Ваш талон №А1"))
        # self.label_3.setText(_translate("MainWindow", "Категория: Долги"))
        # self.label_4.setText(_translate("MainWindow", "Специалист: Орехова И.С."))
        # self.label_5.setText(_translate("MainWindow", "Окно: 7"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'queue.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import asyncio
import time
from _thread import start_new_thread
from threading import Thread

from PyQt5 import QtCore, QtGui, QtWidgets

from db_api.quick_cmd import on_reception_get, get_name_and_num_win


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
        self.label.setGeometry(QtCore.QRect(-11, -22, 1509, 315))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.MarkdownText)
        self.label.setPixmap(QtGui.QPixmap("../фон.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(515, 304, 409, 105))
        self.label_2.setStyleSheet("font-family: Roboto;\n"
                                   "font-style: normal;\n"
                                   "font-weight: 300;\n"
                                   "font-size: 96px;\n"
                                   "line-height: 112px;\n"
                                   "display: flex;\n"
                                   "align-items: center;\n"
                                   "\n"
                                   "color: #000000;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 450, 700, 531))
        self.label_3.setStyleSheet("font-family: Roboto;\n"
                                   "font-style: normal;\n"
                                   "font-weight: normal;\n"
                                   "font-size: 80px;\n"
                                   "line-height: 112px;\n"
                                   "display: flex;\n"
                                   "align-items: center;\n"
                                   "\n"
                                   "color: #000000;")
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(740, 450, 700, 531))
        self.label_4.setStyleSheet("font-family: Roboto;\n"
                                   "font-style: normal;\n"
                                   "font-weight: normal;\n"
                                   "font-size: 80px;\n"
                                   "line-height: 112px;\n"
                                   "display: flex;\n"
                                   "align-items: center;\n"
                                   "\n"
                                   "color: #000000;")
        self.label_4.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        loop = asyncio.get_event_loop()
        # loop = asyncio.new_event_loop()
        # asyncio.set_event_loop(loop)
        #loop = 1
        th_action = Thread(target=self.action_queue, args=(loop,))
        th_action.start()
        #asyncio.get_event_loop().create_task(self.action_queue(loop))
        #start_new_thread(self.action_queue, (loop, ))

    def action_queue(self, loop):
        # loop = asyncio.new_event_loop()
        # asyncio.set_event_loop(loop)
        #loop = asyncio.get_event_loop()
        while True:
            #  очередь (кол-во спецов)
            time.sleep(2)
            #await asyncio.sleep(2)
            text_1 = ""
            text_2 = ""
            for id in range(1, 11):
                on_reception = loop.run_until_complete(on_reception_get(id))
                num_win = loop.run_until_complete(get_name_and_num_win(id))[1]
                # on_reception = await on_reception_get(id)
                # num_win = await (get_name_and_num_win(id))
                if id <= 5:
                    text_1 += str(on_reception) + " - Окно " + str(num_win) + "\n"
                else:
                    text_2 += str(on_reception) + " - Окно " + str(num_win) + "\n"
            self.label_3.setText(text_1)
            self.label_4.setText(text_2)

    def change_label_add(self, label):
        text_1 = self.label_3.text()
        text_2 = self.label_4.text()
        if 5 == len([i for i in text_1 if "\n"]):
            text_2 += label + "\n"
            self.label_4.setText(text_2)
        else:
            text_1 += label + "\n"
            self.label_3.setText(text_1)

    def change_label_del(self, label):
        text_1 = self.label_3.text()
        text_2 = self.label_4.text()
        if label in text_1:
            text_1.replace(label + "\n", "")
            self.label_3.setText(text_1)
        elif label in text_2:
            text_2.replace(label + "\n", "")
            self.label_4.setText(text_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Win1"))
        self.label_2.setText(_translate("MainWindow", "Очередь"))
        # self.label_3.setText(_translate("MainWindow", "ОИС-22 - Окно 10\n"
        #                                               "ОИС-22 - Окно 10\n"
        #                                               "ОИС-22 - Окно 10\n"
        #                                               "ОИС-22 - Окно 10\n"
        #                                               "ОИС-22 - Окно 10\n"
        #                                               ""))
        # self.label_4.setText(_translate("MainWindow", "ОИС-22 - Окно 10\n"
        #                                               "ОИС-22 - Окно 10\n"
        #                                               "ОИС-22 - Окно 10\n"
        #                                               "ОИС-22 - Окно 10\n"
        #                                               "ОИС-22 - Окно 10\n"
        #                                               ""))

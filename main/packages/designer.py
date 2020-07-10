# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1280, 679))
        self.verticalLayoutWidget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.listOfWidgets = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.listOfWidgets.setContentsMargins(0, 0, 0, 0)
        self.listOfWidgets.setObjectName("listOfWidgets")
        self.widgetLogin = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widgetLogin.setEnabled(True)
        self.widgetLogin.setObjectName("widgetLogin")
        self.layoutWidget = QtWidgets.QWidget(self.widgetLogin)
        self.layoutWidget.setObjectName("layoutWidget")
        self.loginGridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.loginGridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.loginGridLayout.setContentsMargins(0, 0, 0, 0)
        self.loginGridLayout.setObjectName("loginGridLayout")
        self.loginBtnLogin = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.loginBtnLogin.setFont(font)
        self.loginBtnLogin.setObjectName("loginBtnLogin")
        self.loginGridLayout.addWidget(self.loginBtnLogin, 0, 0, 1, 1)
        self.loginBtnRegister = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.loginBtnRegister.setFont(font)
        self.loginBtnRegister.setObjectName("loginBtnRegister")
        self.loginGridLayout.addWidget(self.loginBtnRegister, 1, 0, 1, 1)
        self.listOfWidgets.addWidget(self.widgetLogin)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuAccount = QtWidgets.QMenu(self.menubar)
        self.menuAccount.setObjectName("menuAccount")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLogin = QtWidgets.QAction(MainWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.actionNot_signined = QtWidgets.QAction(MainWindow)
        self.actionNot_signined.setObjectName("actionNot_signined")
        self.menuAccount.addAction(self.actionLogin)
        self.menuAccount.addSeparator()
        self.menuAccount.addAction(self.actionNot_signined)
        self.menubar.addAction(self.menuAccount.menuAction())
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginBtnLogin.setText(_translate("MainWindow", "Login"))
        self.loginBtnRegister.setText(_translate("MainWindow", "Register"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuAccount.setTitle(_translate("MainWindow", "Account"))
        self.actionLogin.setText(_translate("MainWindow", "Login"))
        self.actionNot_signined.setText(_translate("MainWindow", "Not signined"))


def startGUI():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

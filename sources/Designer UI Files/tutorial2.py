# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 791, 441))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../bg.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButtonCatalina = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCatalina.setGeometry(QtCore.QRect(210, 490, 75, 23))
        self.pushButtonCatalina.setObjectName("pushButtonCatalina")
        self.pushButtonWindows = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonWindows.setGeometry(QtCore.QRect(540, 490, 75, 23))
        self.pushButtonWindows.setObjectName("pushButtonWindows")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButtonCatalina.clicked.connect(self.show_catalina)
        self.pushButtonWindows.clicked.connect(self.show_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonCatalina.setText(_translate("MainWindow", "Catalina"))
        self.pushButtonWindows.setText(_translate("MainWindow", "Windows"))

    def show_catalina(self):
        self.label.setPixmap(QtGui.QPixmap("../bg.jpg"))

    def show_window(self):
        self.label.setPixmap(QtGui.QPixmap("../bg2.jpg"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1001, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.boton1 = QtWidgets.QPushButton(self.centralwidget)
        self.boton1.setGeometry(QtCore.QRect(20, 20, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(14)
        self.boton1.setFont(font)
        self.boton1.setObjectName("boton1")
        self.boton2 = QtWidgets.QPushButton(self.centralwidget)
        self.boton2.setGeometry(QtCore.QRect(200, 20, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(14)
        self.boton2.setFont(font)
        self.boton2.setObjectName("boton2")
        self.boton3 = QtWidgets.QPushButton(self.centralwidget)
        self.boton3.setGeometry(QtCore.QRect(380, 20, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(14)
        self.boton3.setFont(font)
        self.boton3.setObjectName("boton3")
        self.boton4 = QtWidgets.QPushButton(self.centralwidget)
        self.boton4.setGeometry(QtCore.QRect(560, 20, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(14)
        self.boton4.setFont(font)
        self.boton4.setObjectName("boton4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 100, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.combo = QtWidgets.QComboBox(self.centralwidget)
        self.combo.setGeometry(QtCore.QRect(290, 110, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(14)
        self.combo.setFont(font)
        self.combo.setObjectName("combo")
        self.informacion = QtWidgets.QWidget(self.centralwidget)
        self.informacion.setGeometry(QtCore.QRect(20, 160, 961, 591))
        self.informacion.setObjectName("informacion")
        self.boton5 = QtWidgets.QPushButton(self.informacion)
        self.boton5.setGeometry(QtCore.QRect(760, 490, 191, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(16)
        self.boton5.setFont(font)
        self.boton5.setObjectName("boton5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.boton1.setText(_translate("MainWindow", "Configurar Máquina"))
        self.boton2.setText(_translate("MainWindow", "Simulaciones"))
        self.boton3.setText(_translate("MainWindow", "Reportes"))
        self.boton4.setText(_translate("MainWindow", "Ayuda"))
        self.label.setText(_translate("MainWindow", "Elegir producto a ensamblar:"))
        self.boton5.setText(_translate("MainWindow", "Exportar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
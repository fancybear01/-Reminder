from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(57, 57, 57);")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(25, 100, 350, 130))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(18)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(60, 223, 115);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 35;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(75, 305, 250, 50))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(72, 72, 72);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(37, 37, 37);\n"
"border-radius: 25;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 420, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {background-color:  rgb(60, 223, 115);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 60;}\n"
"QPushButton:pressed {\n"
"background-color: rgb(72, 72, 72)\n"
"}")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CHOOSE A REMINDER TIME"))
        self.pushButton.setText(_translate("MainWindow", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

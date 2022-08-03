import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from alarm import Ui_MainWindow
import schedule
from PyQt5.QtWidgets import QMessageBox
import time
from datetime import datetime

class MainAlarm(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainAlarm, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Alarm")
        self.setWindowIcon(QIcon(r'D:\photoshop\for photoshop\python_icon_black.png'))
        self.ui.lineEdit.setPlaceholderText('Example: 17:30')
        self.ui.pushButton.clicked.connect(self.wait)
    
    def wait(self):
        required_time = self.ui.lineEdit.text()
        self.ui.lineEdit.setText('WAIT')
        def window():
            win = QMessageBox()
            win.setWindowTitle('Already')
            win.setText('!!!THE TIME HAS COME!!!')
            win.setIcon(QMessageBox.Information)
            win.setStandardButtons(QMessageBox.Close)
            win.exec_()
        cur = '%d:%d' % (datetime.now().time().hour, datetime.now().time().minute)
        schedule.every().day.at(required_time).do(window)
        while required_time != cur:
            schedule.run_pending()
            print(datetime.now().time())
            cur = '%d:%d' % (datetime.now().time().hour, datetime.now().time().minute)
            time.sleep(1)
        


app = QtWidgets.QApplication([])
application = MainAlarm()
application.show()

sys.exit(app.exec())
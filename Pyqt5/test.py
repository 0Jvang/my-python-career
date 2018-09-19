import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_mainwindow import Ui_MainWindow as uim


class sub_uim(uim):
    def get_sum(self):
        num_1 = self.lineEdit.text()
        num_2 = self.lineEdit_2.text()
        sum = eval(num_1) + eval(num_2)
        self.textBrowser.setText(str(sum))

    def bc(self):
        self.pushButton.clicked.connect(self.get_sum)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    ui = sub_uim()
    ui.setupUi(mainwindow)
    ui.bc()
    mainwindow.show()
    sys.exit(app.exec_())

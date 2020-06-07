import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MYSQL_MAINWINDOW import Ui_MYSQL_MAINWINDOW
from MYSQL_UPDATE import Ui_MYSQL_UPDATE
from MYSQL_UPDATE import Ui_MYSQL_UPDATE


class MainWindow(QtWidgets.QMainWindow, Ui_MYSQL_MAINWINDOW):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)


class update(QtWidgets.QMainWindow, Ui_MYSQL_UPDATE):
    
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)





def changeWindow(w1, w2):
    w1.hide()
    w2.show()
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    updatetbl=update()

    main.btnUpdateTbl.clicked.connect(lambda: changeWindow(main,updatetbl))

    main.show()
    sys.exit(app.exec_())


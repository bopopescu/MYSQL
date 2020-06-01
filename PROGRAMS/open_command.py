

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MYSQL_CREATEDB import Ui_MYSQL_CREATEDB
from subprocess import call
from MYSQL_CREATEDB import Ui_MYSQL_CREATEDB
from MYSQL_CREATETBL import Ui_MYSQL_CREATETBL
from MYSQL_ALTER import Ui_MYSQL_ALTER
from MYSQL_MAINWINDOW import Ui_MYSQL_MAINWINDOW

class MainWindow(QtWidgets.QMainWindow, Ui_MYSQL_MAINWINDOW):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        

class createdb(QtWidgets.QMainWindow, Ui_MYSQL_CREATEDB):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

class createtbl(QtWidgets.QMainWindow, Ui_MYSQL_CREATETBL):
    
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
    



def changeWindow(w1, w2):
    w1.hide()
    w2.show()
    ui=Ui_MYSQL_CREATETBL
    ui.error_value(self)
    print(ui.error_value)
    
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    createdb = createdb()
    createtbl=createtbl()

    main.btnCreateDB.clicked.connect(lambda:changeWindow(main,createdb))
    main.btnCreateTbl.clicked.connect(lambda: changeWindow(main,createtbl))
    createdb.btncancel.clicked.connect(lambda: changeWindow(createdb,main))
    createtbl.btnCreate.clicked.connect(lambda: changeWindow(createtbl,main))
    createdb.btncreate.clicked.connect(lambda: changeWindow(createdb,main))

    main.show()
    sys.exit(app.exec_())
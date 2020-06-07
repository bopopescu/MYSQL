

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MYSQL_MAINWINDOW import Ui_MYSQL_MAINWINDOW
from MYSQL_CREATEDB import Ui_MYSQL_CREATEDB
from MYSQL_CREATETBL import Ui_MYSQL_CREATETBL
from MYSQL_ALTER import Ui_MYSQL_ALTER
from MYSQL_INSERT import Ui_MYSQL_INSERT
from MYSQL_UPDATE import Ui_MYSQL_UPDATE
from MYSQL_DELETEDB import Ui_MYSQL_DELETEDB
from MYSQL_DELETETABLE import Ui_MYSQL_DELETEtable

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

class inserttbl(QtWidgets.QMainWindow, Ui_MYSQL_INSERT):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

class updatetbl(QtWidgets.QMainWindow, Ui_MYSQL_UPDATE):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)
        self.setupUi(self)

class altertbl(QtWidgets.QMainWindow, Ui_MYSQL_ALTER):
    
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

class deldb(QtWidgets.QMainWindow, Ui_MYSQL_DELETEDB):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)
        self.setupUi(self)

class deltbl(QtWidgets.QMainWindow, Ui_MYSQL_DELETEtable):
    
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)








    



def changeWindow(w1, w2):
    w1.hide()
    w2.show()
    

    
    
    

    
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    createdb = createdb()
    createtbl=createtbl()
    inserttbl=inserttbl()
    updatetbl=updatetbl()
    altertbl=altertbl()
    deldb=deldb()
    deltbl=deltbl()
    


    #mainwindow button actions
    main.btnCreateDB.clicked.connect(lambda:changeWindow(main,createdb))
    main.btnCreateTbl.clicked.connect(lambda: changeWindow(main,createtbl))
    main.btnInsertValues.clicked.connect(lambda: changeWindow(main,inserttbl))
    main.btnUpdateTbl.clicked.connect(lambda: changeWindow(main,updatetbl))
    main.btnAlterTbl.clicked.connect(lambda: changeWindow(main,altertbl))
    main.btnDelDB.clicked.connect(lambda: changeWindow(main,deldb))
    main.btnDelTbl.clicked.connect(lambda: changeWindow(main,deltbl))
    


    #createbd window button actions
    createdb.btncreate.clicked.connect(lambda: changeWindow(createdb,main))
    createdb.btncancel.clicked.connect(lambda: changeWindow(createdb,main))
    

    #createtbl window btn actions
    createtbl.btnCreate.clicked.connect(lambda: changeWindow(createtbl,main))
    createtbl.btncancel.clicked.connect(lambda: changeWindow(createtbl,main))

    #inserttbl window btn actions
    inserttbl.btninsert.clicked.connect(lambda: changeWindow(inserttbl,main))
    inserttbl.btncancel.clicked.connect(lambda: changeWindow(inserttbl,main))

    #updatetbl window btn actions
    updatetbl.btncancel.clicked.connect(lambda: changeWindow(updatetbl,main))
    updatetbl.btnupdate.clicked.connect(lambda: changeWindow(updatetbl,main))
    


    #altertbl window btn actions
    altertbl.btnadd.clicked.connect(lambda: changeWindow(altertbl,main))
    altertbl.btnmod.clicked.connect(lambda: changeWindow(altertbl,main))
    altertbl.btndel.clicked.connect(lambda: changeWindow(altertbl,main))
    altertbl.btncancel.clicked.connect(lambda: changeWindow(altertbl,main))

    #deldb window btn actions

    deldb.btndel.clicked.connect(lambda: changeWindow(deldb,main))
    deldb.btncancel.clicked.connect(lambda: changeWindow(deldb,main))

    #deltbl window btn actions

    deltbl.btndel.clicked.connect(lambda: changeWindow(deltbl,main))
    deltbl.btncancel.clicked.connect(lambda: changeWindow(deltbl,main))





    main.show()
    sys.exit(app.exec_())
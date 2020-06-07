# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MYSQL_CREATEDB.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets 

from tkinter import messagebox
import sys
class Ui_MYSQL_CREATEDB(object):
    def ShowMessageBox(self,title,message):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setIcon(QtWidgets.QMessageBox.Information)
        msgbox.setWindowTitle(title)
        msgbox.setText(message)
        msgbox.exec_()
    def ShowMessageBox_(self,title,message):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setIcon(QtWidgets.QMessageBox.Warning)
        msgbox.setWindowTitle(title)
        msgbox.setText(message)
        msgbox.exec_()
        self.MYSQL_CREATEDB = QtWidgets.QWidget()
        self.ui = Ui_MYSQL_CREATEDB()
        self.ui.setupUi(self.MYSQL_CREATEDB)
        self.MYSQL_CREATEDB.show()


    def createdb(self):
        import mysql.connector
        mydb=mysql.connector.connect(host='localhost', user='root',passwd='logon@123')
        mycursor=mydb.cursor() 
        db_name=self.txtDBname.text()
        query='show databases'
        mycursor.execute(query)
        response=mycursor.fetchall()
        tbllist=[]
        query='create database {}'.format(db_name)
        for i in response:
            for j in i:
                tbllist.append(j.lower())
        if db_name!='' and db_name.lower() in dblist:
            try:
                mycursor.execute(query)
                self.ShowMessageBox('SUCCESSFULL','DB HAS BEEN CREATED SUCESSFULLY')
                mydb.commit()
                self.txtDBname.clear()

            except Exception:
                self.ShowMessageBox_('FAILED','FAILED TO CREATE  DB. RECHECK VALUES!!')
                self.txtDBname.clear()
        else:
            if db_name=='':
                self.ShowMessageBox_('FAILED','ENTER TABLE NAME')
            else:
                self.ShowMessageBox_('FAILED',"ENTERED TABLE NAME DOESN'T EXIST IN DB")
    def cancel(self):
        pass




    def setupUi(self, MYSQL_CREATEDB):
        MYSQL_CREATEDB.setObjectName("MYSQL_CREATEDB")
        MYSQL_CREATEDB.resize(406, 239)
        self.label = QtWidgets.QLabel(MYSQL_CREATEDB)
        self.label.setGeometry(QtCore.QRect(50, 10, 281, 81))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MYSQL_CREATEDB)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btncreate = QtWidgets.QPushButton(MYSQL_CREATEDB)
        self.btncreate.setGeometry(QtCore.QRect(110, 160, 112, 32))
        self.btncreate.setObjectName("btncreate")
        self.btncreate.clicked.connect(self.createdb)
        self.btncancel = QtWidgets.QPushButton(MYSQL_CREATEDB)
        self.btncancel.setGeometry(QtCore.QRect(240, 160, 112, 32))
        self.btncancel.setObjectName("btncancel")
        self.btncancel.clicked.connect(self.cancel)
        self.txtDBname = QtWidgets.QLineEdit(MYSQL_CREATEDB)
        self.txtDBname.setGeometry(QtCore.QRect(182, 110, 211, 31))
        self.txtDBname.setObjectName("txtDBname")
        self.txtDBname.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.btncreate.raise_()
        self.btncancel.raise_()

        self.retranslateUi(MYSQL_CREATEDB)
        QtCore.QMetaObject.connectSlotsByName(MYSQL_CREATEDB)

    def retranslateUi(self, MYSQL_CREATEDB):
        _translate = QtCore.QCoreApplication.translate
        MYSQL_CREATEDB.setWindowTitle(_translate("MYSQL_CREATEDB", "Form"))
        self.label.setText(_translate("MYSQL_CREATEDB", "CREATING DATABASE"))
        self.label_2.setText(_translate("MYSQL_CREATEDB", "DATABASE NAME: "))
        self.btncreate.setText(_translate("MYSQL_CREATEDB", "CREATE"))
        self.btncancel.setText(_translate("MYSQL_CREATEDB", "CANCEL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MYSQL_CREATEDB = QtWidgets.QWidget()
    ui = Ui_MYSQL_CREATEDB()
    ui.setupUi(MYSQL_CREATEDB)
    MYSQL_CREATEDB.show()
    sys.exit(app.exec_())


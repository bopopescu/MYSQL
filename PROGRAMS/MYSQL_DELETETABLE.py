# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MYSQL_DELETETABLE.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MYSQL_DELETEtable(object):
    def ShowMessageBox(self,title,message):
        value=2
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
        self.MYSQL_deltbl = QtWidgets.QWidget()
        self.ui = Ui_MYSQL_DELETEtable()
        self.ui.setupUi(self.MYSQL_deltbl)
        self.MYSQL_deltbl.show()

    def deltbl(self):
        self.tblname=self.txtTblname.text()
        import mysql.connector
        mydb=mysql.connector.connect(host='localhost', user='root',passwd='logon@123',database='python')
        mycursor=mydb.cursor()
        query='show tables'
        mycursor.execute(query)
        res=mycursor.fetchall()
        tbllist=[]
        for i in res:
            for j in i:
                tbllist.append(j.lower())


        if self.tblname=='' or self.tblname.lower() not in tbllist:
            if self.tblname=='':
                self.ShowMessageBox_('FAILED','ENTER TABLE NAME')
                self.txtTblname.clear()
                return
            else:
                self.ShowMessageBox_('FAILED',"ENTERED TABLE NAME DOESN'T EXIST IN DB ")
                return

        else:
            query='drop table {}'.format(self.tblname)
            try:
                mycursor.execute(query)
                mydb.commit()
                self.ShowMessageBox('SUCCESSFULL','SUCCESSFULLY DELETED TABLE FROM DB')
                self.txtTblname.clear()
            except Exception:
                self.ShowMessageBox('FAILED','ERROR WHILE DELETING TABLE')
                







    def setupUi(self, MYSQL_DELETEtable):
        MYSQL_DELETEtable.setObjectName("MYSQL_DELETEtable")
        MYSQL_DELETEtable.resize(406, 239)
        self.label = QtWidgets.QLabel(MYSQL_DELETEtable)
        self.label.setGeometry(QtCore.QRect(50, 10, 281, 81))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MYSQL_DELETEtable)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btndel = QtWidgets.QPushButton(MYSQL_DELETEtable)
        self.btndel.setGeometry(QtCore.QRect(110, 160, 112, 32))
        self.btndel.setObjectName("btndel")
        self.btndel.clicked.connect(self.deltbl)
        self.btncancel = QtWidgets.QPushButton(MYSQL_DELETEtable)
        self.btncancel.setGeometry(QtCore.QRect(240, 160, 112, 32))
        self.btncancel.setObjectName("btncancel")
        self.txtTblname = QtWidgets.QLineEdit(MYSQL_DELETEtable)
        self.txtTblname.setGeometry(QtCore.QRect(182, 110, 211, 31))
        self.txtTblname.setObjectName("txtTblname")
        self.txtTblname.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.btndel.raise_()
        self.btncancel.raise_()

        self.retranslateUi(MYSQL_DELETEtable)
        QtCore.QMetaObject.connectSlotsByName(MYSQL_DELETEtable)

    def retranslateUi(self, MYSQL_DELETEtable):
        _translate = QtCore.QCoreApplication.translate
        MYSQL_DELETEtable.setWindowTitle(_translate("MYSQL_DELETEtable", "Form"))
        self.label.setText(_translate("MYSQL_DELETEtable", "DELETE TABLE"))
        self.label_2.setText(_translate("MYSQL_DELETEtable", "TABLE NAME: "))
        self.btndel.setText(_translate("MYSQL_DELETEtable", "DELETE"))
        self.btncancel.setText(_translate("MYSQL_DELETEtable", "CANCEL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MYSQL_DELETEtable = QtWidgets.QWidget()
    ui = Ui_MYSQL_DELETEtable()
    ui.setupUi(MYSQL_DELETEtable)
    MYSQL_DELETEtable.show()
    sys.exit(app.exec_())

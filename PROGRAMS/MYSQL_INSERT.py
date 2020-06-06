# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MYSQL_INSERT.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MYSQL_INSERT(object):
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
        self.MYSQL_INSERT = QtWidgets.QWidget()
        self.ui = Ui_MYSQL_INSERT()
        self.ui.setupUi(self.MYSQL_INSERT)
        self.MYSQL_INSERT.show()
    
    def insert(self):
        import mysql.connector
        mydb=mysql.connector.connect(host='localhost', user='root',passwd='logon@123',database='python')
        mycursor=mydb.cursor()
        tblname=self.txttblname.text()
        val1=self.txtvalue1.text()
        val2=self.txtvalue2.text()
        val3=self.txtvalue3.text()
        val4=self.txtvalue4.text()
        query='show tables'
        mycursor.execute(query)
        res=mycursor.fetchall()
        list=[]
        for i in res:
            for j in i:
                list.append(j)

        if tblname not in list:
            if tblname=='':
                self.ShowMessageBox_('FAILED',"ENTER TABLE NAME")
            else:
                self.ShowMessageBox_('FAILED',"ENTERED TABLE NAME DOESN'T EXIST IN DB")
        else:
            if (val1=='') or (val2=='') or (val3=='') or (val4==''):
                self.ShowMessageBox_('FAILED','ENTER VALUES OF ALL 4 COLUMNS')
            elif val1==val2==val3==val4:
                self.ShowMessageBox_('FAILED',('ALL VALUES ARE EQUAL. PLEASE ENTER ACCORDING TO TABLE CONSTRAINTS'))
            else:
                query='insert into {} values("{}","{}","{}","{}")'.format(tblname,val1,val2,val3,val4)
                try:
                    print(query)
                    mycursor.execute(query)
                    mydb.commit()
                    self.ShowMessageBox('SUCCESSFULL','SUCCESSFULLY INSERTED VALUES INTO TABLE')
                except Exception:
                    self.ShowMessageBox('FAILED','ERROR WHILE INSERTING VALUES INTO TABLE')


    def setupUi(self, MYSQL_INSERT):
        MYSQL_INSERT.setObjectName("MYSQL_INSERT")
        MYSQL_INSERT.resize(579, 445)
        self.label = QtWidgets.QLabel(MYSQL_INSERT)
        self.label.setGeometry(QtCore.QRect(100, 10, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(MYSQL_INSERT)
        self.label_4.setGeometry(QtCore.QRect(40, 180, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(MYSQL_INSERT)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txttblname = QtWidgets.QLineEdit(MYSQL_INSERT)
        self.txttblname.setGeometry(QtCore.QRect(210, 180, 221, 31))
        self.txttblname.setObjectName("txttblname")
        self.label_3 = QtWidgets.QLabel(MYSQL_INSERT)
        self.label_3.setGeometry(QtCore.QRect(210, 130, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(MYSQL_INSERT)
        self.label_5.setGeometry(QtCore.QRect(40, 230, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txtvalue1 = QtWidgets.QLineEdit(MYSQL_INSERT)
        self.txtvalue1.setGeometry(QtCore.QRect(210, 230, 221, 31))
        self.txtvalue1.setObjectName("txtvalue1")
        self.label_6 = QtWidgets.QLabel(MYSQL_INSERT)
        self.label_6.setGeometry(QtCore.QRect(40, 330, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.txtvalue3 = QtWidgets.QLineEdit(MYSQL_INSERT)
        self.txtvalue3.setGeometry(QtCore.QRect(210, 330, 221, 31))
        self.txtvalue3.setObjectName("txtvalue3")
        self.label_7 = QtWidgets.QLabel(MYSQL_INSERT)
        self.label_7.setGeometry(QtCore.QRect(40, 280, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.txtvalue2 = QtWidgets.QLineEdit(MYSQL_INSERT)
        self.txtvalue2.setGeometry(QtCore.QRect(210, 280, 221, 31))
        self.txtvalue2.setObjectName("txtvalue2")
        self.label_9 = QtWidgets.QLabel(MYSQL_INSERT)
        self.label_9.setGeometry(QtCore.QRect(40, 380, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.txtvalue4 = QtWidgets.QLineEdit(MYSQL_INSERT)
        self.txtvalue4.setGeometry(QtCore.QRect(210, 380, 221, 31))
        self.txtvalue4.setObjectName("txtvalue4")
        self.frame = QtWidgets.QFrame(MYSQL_INSERT)
        self.frame.setGeometry(QtCore.QRect(20, 110, 431, 321))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btncancel = QtWidgets.QPushButton(MYSQL_INSERT)
        self.btncancel.setGeometry(QtCore.QRect(460, 160, 112, 32))
        self.btncancel.setObjectName("btncancel")
        self.btninsert = QtWidgets.QPushButton(MYSQL_INSERT)
        self.btninsert.setGeometry(QtCore.QRect(460, 120, 112, 32))
        self.btninsert.setObjectName("btninsert")
        self.btninsert.clicked.connect(self.insert)
        self.frame.raise_()
        self.label.raise_()
        self.btncancel.raise_()
        self.btninsert.raise_()
        self.label_2.raise_()
        self.txtvalue3.raise_()
        self.label_6.raise_()
        self.txttblname.raise_()
        self.label_9.raise_()
        self.txtvalue1.raise_()
        self.label_7.raise_()
        self.txtvalue4.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.txtvalue2.raise_()
        self.label_5.raise_()

        self.retranslateUi(MYSQL_INSERT)
        QtCore.QMetaObject.connectSlotsByName(MYSQL_INSERT)

    def retranslateUi(self, MYSQL_INSERT):
        _translate = QtCore.QCoreApplication.translate
        MYSQL_INSERT.setWindowTitle(_translate("MYSQL_INSERT", "Form"))
        self.label.setText(_translate("MYSQL_INSERT", "<html><head/><body><p align=\"center\">INSERTING VALUES </p><p align=\"center\">INTO TABLE</p></body></html>"))
        self.label_4.setText(_translate("MYSQL_INSERT", "TABLE NAME: "))
        self.label_2.setText(_translate("MYSQL_INSERT", "DATABASE NAME: "))
        self.label_3.setText(_translate("MYSQL_INSERT", "<html><head/><body><p align=\"center\">PYTHON</p></body></html>"))
        self.label_5.setText(_translate("MYSQL_INSERT", "VALUE 1: "))
        self.label_6.setText(_translate("MYSQL_INSERT", "VALUE 3:"))
        self.label_7.setText(_translate("MYSQL_INSERT", "VALUE 2: "))
        self.label_9.setText(_translate("MYSQL_INSERT", "VALUE 4:"))
        self.btncancel.setText(_translate("MYSQL_INSERT", "CANCEL"))
        self.btninsert.setText(_translate("MYSQL_INSERT", "INSERT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MYSQL_INSERT = QtWidgets.QWidget()
    ui = Ui_MYSQL_INSERT()
    ui.setupUi(MYSQL_INSERT)
    MYSQL_INSERT.show()
    sys.exit(app.exec_())

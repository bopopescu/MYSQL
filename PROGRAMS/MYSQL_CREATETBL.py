# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MYSQL_CREATETBL.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MYSQL_CREATETBL(object):
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
        self.MYSQL_CREATETBL = QtWidgets.QWidget()
        self.ui = Ui_MYSQL_CREATETBL()
        self.ui.setupUi(self.MYSQL_CREATETBL)
        self.MYSQL_CREATETBL.show()
        
    
    
    

    
        
        
        
        

    


    def createtbl(self):
        import mysql.connector
        mydb=mysql.connector.connect(host='localhost', user='root',passwd='logon@123',database='python',auth_plugin='mysql_native_password')
        mycursor=mydb.cursor()
        tablename=self.txttblname.text()
        col1name=self.txtcolumn1name.text()
        col1type=self.txtcolumn1type.text()
        col2name=self.txtcolumn2name.text()
        col2type=self.txtcolumn2type.text()
        col3name=self.txtcolumn3name.text()
        col3type=self.txtcolumn3type.text()
        col4name=self.txtcolumn4name.text()
        col4type=self.txtcolumn4type.text()
        query='show tables'
        mycursor.execute(query)
        res=mycursor.fetchall()
        list=[]
        for i in res:
            for j in i:
                list.append(j)
        if tablename in list:
            self.ShowMessageBox_('FAILED','TABLE WITH THE GIVEN ALDREADY EXIST')
            self.txttblname.clear()

        elif col1name=='' and col1type=='' and col2name=='' and col2type== '' and  col3name=='' and col3type=='' and col4name=='' and col4type=='':
            self.ShowMessageBox_('FAILED','PLEASE ENTER VALUES')
        elif col1name==col2name==col3name==col4name:
            self.ShowMessageBox_('FAILED','ALL COLUMN NAMES ARE EQUAL')
            self.txtcolumn1name.clear()
            self.txtcolumn2name.clear()
            self.txtcolumn2type.clear()
            self.txtcolumn3name.clear()
            self.txtcolumn4name.clear()
            self.txtcolumn4type.clear()    
            
        else:
            query='create table {}({} {},{} {},{} {},{} {}'.format(tablename,col1name,col1type,col2name,col2type,col3name,col3type,col4name,col4type)
            query=query.rstrip(' ,')
            temp=query+')'
            query=query+')'
            list=[]
            start=0
            for i in range(len(temp)):
                if temp[i]==',' and temp[i-1]==' ' and temp[i-2]==',':
                    list.append(i)
                
            if len(list)!=0:
                query=''
                for j in range(len(list)):
                
                    stop=list[j]-1
                    query=query+temp[start:stop]
                    start=stop+2
                    query=query+temp[start::]    
            
            try:
                mycursor.execute(query)
                mydb.commit()
                self.ShowMessageBox('successfull','successfully created table')
                self.txttblname.clear()
                self.txtcolumn1name.clear()
                self.txtcolumn2name.clear()
                self.txtcolumn2type.clear()
                self.txtcolumn3name.clear()
                self.txtcolumn4name.clear()
                self.txtcolumn4type.clear()    
            except Exception:
                self.ShowMessageBox_('error','error while creating table')
                self.txttblname.clear()
                self.txtcolumn1name.clear()
                self.txtcolumn2name.clear()
                self.txtcolumn2type.clear()
                self.txtcolumn3name.clear()
                self.txtcolumn4name.clear()
                self.txtcolumn4type.clear()    
    def cancel(self):
        pass
        
            







    def setupUi(self, MYSQL_CREATETBL):
        MYSQL_CREATETBL.setObjectName("MYSQL_CREATETBL")
        MYSQL_CREATETBL.resize(619, 633)
        self.label = QtWidgets.QLabel(MYSQL_CREATETBL)
        self.label.setGeometry(QtCore.QRect(160, 0, 281, 81))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MYSQL_CREATETBL)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btnCreate = QtWidgets.QPushButton(MYSQL_CREATETBL)
        self.btnCreate.setGeometry(QtCore.QRect(490, 90, 112, 32))
        self.btnCreate.setObjectName("btnCreate")
        self.btnCreate.clicked.connect(self.createtbl)
        self.btncancel = QtWidgets.QPushButton(MYSQL_CREATETBL)
        self.btncancel.setGeometry(QtCore.QRect(490, 130, 112, 32))
        self.btncancel.setObjectName("btncancel")
        self.btncancel.clicked.connect(self.cancel)
        self.label_3 = QtWidgets.QLabel(MYSQL_CREATETBL)
        self.label_3.setGeometry(QtCore.QRect(200, 110, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(MYSQL_CREATETBL)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(MYSQL_CREATETBL)
        self.label_5.setGeometry(QtCore.QRect(30, 200, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(MYSQL_CREATETBL)
        self.label_6.setGeometry(QtCore.QRect(30, 250, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.frame = QtWidgets.QFrame(MYSQL_CREATETBL)
        self.frame.setGeometry(QtCore.QRect(20, 80, 441, 521))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(10, 270, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(10, 220, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(10, 370, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(10, 420, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(10, 320, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(10, 470, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.txttblname = QtWidgets.QLineEdit(self.frame)
        self.txttblname.setGeometry(QtCore.QRect(180, 70, 221, 31))
        self.txttblname.setObjectName("txttblname")
        self.txtcolumn1name = QtWidgets.QLineEdit(self.frame)
        self.txtcolumn1name.setGeometry(QtCore.QRect(180, 120, 221, 31))
        self.txtcolumn1name.setObjectName("txtcolumn1name")
        self.txtcolumn2name = QtWidgets.QLineEdit(self.frame)
        self.txtcolumn2name.setGeometry(QtCore.QRect(180, 220, 221, 31))
        self.txtcolumn2name.setObjectName("txtcolumn2name")
        self.txtcolumn1type = QtWidgets.QLineEdit(self.frame)
        self.txtcolumn1type.setGeometry(QtCore.QRect(180, 170, 221, 31))
        self.txtcolumn1type.setObjectName("txtcolumn1type")
        self.txtcolumn3type = QtWidgets.QLineEdit(self.frame)
        self.txtcolumn3type.setGeometry(QtCore.QRect(180, 370, 221, 31))
        self.txtcolumn3type.setObjectName("txtcolumn3type")
        self.txtcolumn4name = QtWidgets.QLineEdit(self.frame)
        self.txtcolumn4name.setGeometry(QtCore.QRect(180, 420, 221, 31))
        self.txtcolumn4name.setObjectName("txtcolumn4name")
        self.txtcolumn3name = QtWidgets.QLineEdit(self.frame)
        self.txtcolumn3name.setGeometry(QtCore.QRect(180, 320, 221, 31))
        self.txtcolumn3name.setObjectName("txtcolumn3name")
        self.txtcolumn2type = QtWidgets.QLineEdit(self.frame)
        self.txtcolumn2type.setGeometry(QtCore.QRect(180, 270, 221, 31))
        self.txtcolumn2type.setObjectName("txtcolumn2type")
        self.txtcolumn4type = QtWidgets.QLineEdit(self.frame)
        self.txtcolumn4type.setGeometry(QtCore.QRect(180, 470, 221, 31))
        self.txtcolumn4type.setObjectName("txtcolumn4type")
        self.label_9.raise_()
        self.label_13.raise_()
        self.label_7.raise_()
        self.label_11.raise_()
        self.label_8.raise_()
        self.label_12.raise_()
        self.txttblname.raise_()
        self.txtcolumn1name.raise_()
        self.txtcolumn2name.raise_()
        self.txtcolumn1type.raise_()
        self.txtcolumn3type.raise_()
        self.txtcolumn4name.raise_()
        self.txtcolumn3name.raise_()
        self.txtcolumn2type.raise_()
        self.txtcolumn4type.raise_()
        self.frame.raise_()
        self.label.raise_()
        self.btnCreate.raise_()
        self.btncancel.raise_()
        self.label_6.raise_()
        self.label_4.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_5.raise_()

        self.retranslateUi(MYSQL_CREATETBL)
        QtCore.QMetaObject.connectSlotsByName(MYSQL_CREATETBL)

    def retranslateUi(self, MYSQL_CREATETBL):
        _translate = QtCore.QCoreApplication.translate
        MYSQL_CREATETBL.setWindowTitle(_translate("MYSQL_CREATETBL", "Form"))
        self.label.setText(_translate("MYSQL_CREATETBL", "CREATING TABLE"))
        self.label_2.setText(_translate("MYSQL_CREATETBL", "DATABASE NAME: "))
        self.btnCreate.setText(_translate("MYSQL_CREATETBL", "CREATE"))
        self.btncancel.setText(_translate("MYSQL_CREATETBL", "CANCEL"))
        self.label_3.setText(_translate("MYSQL_CREATETBL", "<html><head/><body><p align=\"center\">PYTHON</p></body></html>"))
        self.label_4.setText(_translate("MYSQL_CREATETBL", "TABLE NAME: "))
        self.label_5.setText(_translate("MYSQL_CREATETBL", "COLUMN 1 NAME:"))
        self.label_6.setText(_translate("MYSQL_CREATETBL", "COLUMN 1 TYPE:"))
        self.label_7.setText(_translate("MYSQL_CREATETBL", "COLUMN 2 TYPE:"))
        self.label_8.setText(_translate("MYSQL_CREATETBL", "COLUMN 2 NAME:"))
        self.label_12.setText(_translate("MYSQL_CREATETBL", "COLUMN 3 TYPE:"))
        self.label_9.setText(_translate("MYSQL_CREATETBL", "COLUMN 4 NAME:"))
        self.label_11.setText(_translate("MYSQL_CREATETBL", "COLUMN 3 NAME:"))
        self.label_13.setText(_translate("MYSQL_CREATETBL", "COLUMN 4 TYPE:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MYSQL_CREATETBL = QtWidgets.QWidget()
    ui = Ui_MYSQL_CREATETBL()
    ui.setupUi(MYSQL_CREATETBL)
    MYSQL_CREATETBL.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MYSQL_UPDATE.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MYSQL_UPDATE(object):
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
        self.MYSQL_UPDATE = QtWidgets.QWidget()
        self.ui = Ui_MYSQL_UPDATE()
        self.ui.setupUi(self.MYSQL_UPDATE)
        self.MYSQL_UPDATE.show()
    
    def prival(self):
        print('1')
        self.privall=1

    def prival2(self):
        self.privall=2

    def prival3(self):
        self.privall=3

    def prival4(self):
        self.privall=4
    
    def val(self):
        self.tblname=self.txttblname.text()
        self.val1=self.txtvalue1.text()
        self.val2=self.txtvalue2.text()
        self.val3=self.txtvalue3.text()
        self.val4=self.txtvalue4.text()
        self.vallist=[self.val1,self.val2,self.val3,self.val4]
    
    def tblcheck(self):
        try:
            import mysql.connector
            mydb=mysql.connector.connect(host='localhost', user='root',passwd='logon@123',database='python',auth_plugin='mysql_native_password')
            mycursor=mydb.cursor()
            query='show tables'
            mycursor.execute(query)
            res=mycursor.fetchall()
            tbllist=[]
            for i in res:
                for j in i:
                    tbllist.append(j.lower())
            
            a=self.tblname
            if self.txttblname.text()=='':
                self.ShowMessageBox_('FAILED','ENTER TABLE NAME')
                return
            elif a.lower() in tbllist:
                self.fetchingcolumns()
            
            else:
                self.ShowMessageBox_('ERROR','ENTERED TABLE DOESNT EXIST IN DB')
                self.txttblname.clear()
                return
        except Exception:
            return
        
        

    def fetchingcolumns(self):
        
        import mysql.connector
        mydb=mysql.connector.connect(host='localhost', user='root',passwd='logon@123',database='python',auth_plugin='mysql_native_password')
        mycursor=mydb.cursor()
        try:
            self.query='show columns from {}'.format(self.txttblname.text())
            mycursor.execute(self.query)
            self.response=mycursor.fetchall()
            self.list=[]
            for i in self.response:
                self.list.append(i[0])
            if self.privall==1:
                self.prikey1()
            if self.privall==2:
                self.prikey2()
            if self.privall==3:
                self.prikey3()
            if self.privall==4:
                self.prikey4()

        except Exception:
            return    

    def prikey1(self):
    
        self.primcolname=self.list[0]
        self.primval=self.txtvalue1.text()
    def prikey2(self):
        self.primcolname=self.list[1]
        self.primval=self.txtvalue2.text()
    def prikey3(self):
        self.primcolname=self.list[2]
        self.primval=self.txtvalue3.text()
    def prikey4(self):
        self.primcolname=self.list[3]
        self.primval=self.txtvalue4.text()
    
    def finalval(self):
        try:
            self.tblname=self.txttblname.text()
            self.val1=self.txtvalue1.text()
            self.val2=self.txtvalue2.text()
            self.val3=self.txtvalue3.text()
            self.val4=self.txtvalue4.text()
            self.col1=self.list[0]
            self.col2=self.list[1]
            self.col3=self.list[2]
            self.col4=self.list[3]
            query=''
            list1=[]
            for i in self.vallist:
                if i!='':
                    query=query+','+ i
                    list1.append(i)

                else:
                    continue
            self.query=query.lstrip(',')
            self.list1=list1
            
            set_command=''
            
            for i in range(len(self.vallist)):
                for j in self.list1:
                    if self.vallist[i]==j:
                        for a in range(len(self.list)):

                            if i==a and j!=self.primval:
                                set_command=set_command+'{}="{}",'.format(self.list[a],j)
            
            self.set_command=set_command.rstrip(',')
        except Exception:
            return


            
        
        
    def updatetbl(self):
        import mysql.connector
        mydb=mysql.connector.connect(host='localhost', user='root',passwd='logon@123',database='python',auth_plugin='mysql_native_password')
        mycursor=mydb.cursor()
        try:
            self.val()
            self.tblcheck()
    
            if self.primval!='':
                try:
                    self.finalval()
                    query='update {} set '.format(self.txttblname.text())
                    query=query+"{} where ".format(self.set_command)
                    query=query+"{}={}".format(self.primcolname,self.primval)
                    mycursor.execute(query)
                    mydb.commit()
                    self.ShowMessageBox('SUCCESSFULL','SUCCESSFULLY UPDATED TABLE')
                    self.txttblname.clear()
                    self.txtvalue1.clear()
                    self.txtvalue2.clear()
                    self.txtvalue3.clear()
                    self.txtvalue4.clear()
                except Exception:
                    self.ShowMessageBox_('FAILED','ERROR WHILE UPDATING TABLE.PLEASE RE-CHECK VALUE')
                    self.txttblname.clear()
                    self.txtvalue1.clear()
                    self.txtvalue2.clear()
                    self.txtvalue3.clear()
                    self.txtvalue4.clear()

            else:
                self.ShowMessageBox_('FAILED','SELECT PRIMARY KEY')
            
        except Exception:
            return

        
    
    def setupUi(self, MYSQL_UPDATE):
        MYSQL_UPDATE.setObjectName("MYSQL_UPDATE")
        MYSQL_UPDATE.resize(754, 488)
        self.label_4 = QtWidgets.QLabel(MYSQL_UPDATE)
        self.label_4.setGeometry(QtCore.QRect(40, 190, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btnupdate = QtWidgets.QPushButton(MYSQL_UPDATE)
        self.btnupdate.setGeometry(QtCore.QRect(620, 130, 112, 32))
        self.btnupdate.setObjectName("btnupdate")
        self.btnupdate.clicked.connect(self.updatetbl)
        self.label_7 = QtWidgets.QLabel(MYSQL_UPDATE)
        self.label_7.setGeometry(QtCore.QRect(40, 290, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.txtvalue3 = QtWidgets.QLineEdit(MYSQL_UPDATE)
        self.txtvalue3.setGeometry(QtCore.QRect(210, 340, 221, 31))
        self.txtvalue3.setObjectName("txtvalue3")
        self.txttblname = QtWidgets.QLineEdit(MYSQL_UPDATE)
        self.txttblname.setGeometry(QtCore.QRect(210, 190, 221, 31))
        self.txttblname.setObjectName("txttblname")
        self.label_3 = QtWidgets.QLabel(MYSQL_UPDATE)
        self.label_3.setGeometry(QtCore.QRect(210, 140, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(MYSQL_UPDATE)
        self.label.setGeometry(QtCore.QRect(120, 20, 421, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txtvalue2 = QtWidgets.QLineEdit(MYSQL_UPDATE)
        self.txtvalue2.setGeometry(QtCore.QRect(210, 290, 221, 31))
        self.txtvalue2.setObjectName("txtvalue2")
        self.label_2 = QtWidgets.QLabel(MYSQL_UPDATE)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_9 = QtWidgets.QLabel(MYSQL_UPDATE)
        self.label_9.setGeometry(QtCore.QRect(40, 390, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_5 = QtWidgets.QLabel(MYSQL_UPDATE)
        self.label_5.setGeometry(QtCore.QRect(40, 240, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txtvalue1 = QtWidgets.QLineEdit(MYSQL_UPDATE)
        self.txtvalue1.setGeometry(QtCore.QRect(210, 240, 221, 31))
        self.txtvalue1.setObjectName("txtvalue1")
        self.frame = QtWidgets.QFrame(MYSQL_UPDATE)
        self.frame.setGeometry(QtCore.QRect(20, 120, 591, 341))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.primkey1 = QtWidgets.QCheckBox(self.frame)
        self.primkey1.setGeometry(QtCore.QRect(440, 120, 101, 31))
        self.primkey1.setObjectName("primkey1")
        self.primkey1.toggled.connect(self.prival)
        self.primkey3 = QtWidgets.QCheckBox(self.frame)
        self.primkey3.setGeometry(QtCore.QRect(440, 220, 101, 31))
        self.primkey3.setObjectName("primkey3")
        self.primkey3.toggled.connect(self.prival3)
        self.primkey2 = QtWidgets.QCheckBox(self.frame)
        self.primkey2.setGeometry(QtCore.QRect(440, 170, 101, 31))
        self.primkey2.setObjectName("primkey2")
        self.primkey2.toggled.connect(self.prival2)
        self.primkey4 = QtWidgets.QCheckBox(self.frame)
        self.primkey4.setGeometry(QtCore.QRect(440, 270, 101, 31))
        self.primkey4.setObjectName("primkey4")
        self.primkey4.toggled.connect(self.prival4)
        self.primkey3.raise_()
        self.primkey2.raise_()
        self.primkey1.raise_()
        self.primkey4.raise_()
        self.btncancel = QtWidgets.QPushButton(MYSQL_UPDATE)
        self.btncancel.setGeometry(QtCore.QRect(620, 160, 112, 32))
        self.btncancel.setObjectName("btncancel")
        self.label_6 = QtWidgets.QLabel(MYSQL_UPDATE)
        self.label_6.setGeometry(QtCore.QRect(40, 340, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.txtvalue4 = QtWidgets.QLineEdit(MYSQL_UPDATE)
        self.txtvalue4.setGeometry(QtCore.QRect(210, 390, 221, 31))
        self.txtvalue4.setObjectName("txtvalue4")
        self.frame.raise_()
        self.btnupdate.raise_()
        self.label.raise_()
        self.btncancel.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.txtvalue2.raise_()
        self.txtvalue3.raise_()
        self.txtvalue1.raise_()
        self.txtvalue4.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.txttblname.raise_()
        self.label_9.raise_()
        self.label_2.raise_()
        self.label_7.raise_()

        self.retranslateUi(MYSQL_UPDATE)
        QtCore.QMetaObject.connectSlotsByName(MYSQL_UPDATE)

    def retranslateUi(self, MYSQL_UPDATE):
        _translate = QtCore.QCoreApplication.translate
        MYSQL_UPDATE.setWindowTitle(_translate("MYSQL_UPDATE", "Form"))
        self.label_4.setText(_translate("MYSQL_UPDATE", "TABLE NAME: "))
        self.btnupdate.setText(_translate("MYSQL_UPDATE", "UPDATE"))
        self.label_7.setText(_translate("MYSQL_UPDATE", "NEW VALUE 2:"))
        self.label_3.setText(_translate("MYSQL_UPDATE", "<html><head/><body><p align=\"center\">PYTHON</p></body></html>"))
        self.label.setText(_translate("MYSQL_UPDATE", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">UPDATING VALUES IN TABLE</span></p></body></html>"))
        self.label_2.setText(_translate("MYSQL_UPDATE", "DATABASE NAME: "))
        self.label_9.setText(_translate("MYSQL_UPDATE", "NEW VALUE 4:"))
        self.label_5.setText(_translate("MYSQL_UPDATE", "NEW VALUE 1: "))
        self.primkey1.setText(_translate("MYSQL_UPDATE", "primary key"))
        self.primkey3.setText(_translate("MYSQL_UPDATE", "primary key"))
        self.primkey2.setText(_translate("MYSQL_UPDATE", "primary key"))
        self.primkey4.setText(_translate("MYSQL_UPDATE", "primary key"))
        self.btncancel.setText(_translate("MYSQL_UPDATE", "CANCEL"))
        self.label_6.setText(_translate("MYSQL_UPDATE", "NEW VALUE 3: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MYSQL_UPDATE = QtWidgets.QWidget()
    ui = Ui_MYSQL_UPDATE()
    ui.setupUi(MYSQL_UPDATE)
    MYSQL_UPDATE.show()
    sys.exit(app.exec_())

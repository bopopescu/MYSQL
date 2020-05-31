# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MYSQL_ALTER.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MYSQL_ALTER(object):
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
    def tblname(self):
        self.tablname=self.txttablname.text()


    def add(self):
        import mysql.connector
        mydb=mysql.connector.connect(host='localhost', user='root',passwd='logon@123',database='python')
        mycursor=mydb.cursor()
        col1name=self.txtcolumn1name.text()
        col1type=self.txtcolumn1type.text()
        col2name=self.txtcolumn2name.text()
        col2type=self.txtcolumn2type.text()
        col3name=self.txtcolumn3name.text()
        col3type=self.txtcolumn3type.text()
        col4name=self.txtcolumn4name.text()
        col4type=self.txtcolumn4type.text()
        if self.tablname=='':
            self.ShowMessageBox_('error','enter table name')
        elif col1name=='' and col1type=='' and col2name=='' and col2type== '' and  col3name=='' and col3type=='' and col4name=='' and col4type=='':
            self.ShowMessageBox_('FAILED','PLEASE ENTER VALUES')

        elif col1name==col2name==col3name==col4name:
            self.ShowMessageBox_('FAILED','ALL COLUMN NAMES ARE EQUAL')
        else:
            query= 'alter table {} add ({} {},{} {},{} {},{} {}'.format(self.tablname,col1name,col1type,col2name,col2type,col3name,col3type,col4name,col4type)
            query=query.rstrip(' ,')
            temp=query+')'
            query=''
            list=[]
            start=0
            for i in range(len(temp)):
                if temp[i]==',' and temp[i-1]==' ' and temp[i-2]==',':
                    list.append(i)
                
            for j in range(len(list)):
                stop=list[j]-1
                query=query+temp[start:stop]
                start=stop+2
            query=query+temp[start::] 
            if query=='':
                self.ShowMessageBox_('error','error while stripping query')
            else:
                try:
                    mycursor.execute(query)
                    self.ShowMessageBox('successfull','successfully altered table')
                    mydb.commit()
                    sys.exit()
        

                except Exception:
                    self.ShowMessageBox_('error','error while altering table')
    def mod(self):
        import mysql.connector
        mydb=mysql.connector.connect(host='localhost', user='root',passwd='logon@123',database='python')
        mycursor=mydb.cursor()
        if self.tablname=='':
            self.ShowMessageBox_('error','enter table name')
        else:
            query='show columns from {}'.format(self.tablname)
            mycursor.execute(query)
            response=mycursor.fetchall()
            list=[]
            for i in response:
                list.append(i[0])
            if len(list)<4:
                self.ShowMessageBox_('error','the entered table has columns<4 or 4<columns')
            else:
                col1=list[0]
                col2=list[1]
                col3=list[2]
                col4=list[3]
                modcol1name=self.txtmodcol1name.text()
                modcol1type=self.txtmodcol1type.text()
                modcol2name=self.txtmodcol2name.text()
                modcol2type=self.txtmodcol2type.text()
                modcol3name=self.txtmodcol3name.text()
                modcol3type=self.txtmodcol3type.text()
                modcol4name=self.txtmodcol4name.text()
                modcol4type=self.txtmodcol4type.text()
               
                if modcol1name=='' and modcol1type=='' and modcol2name=='' and modcol2type=='' and modcol3name=='' and modcol3type=='' and modcol4name=='' and modcol4type=='':
                    self.ShowMessageBox_('ERROR','PLEASE ENTER VALUSE')
                elif modcol1name==modcol2name==modcol3name==modcol4name:
                    self.ShowMessageBox_('ERROR','COLUMN NAMES ARE EQUAL!!')
                elif modcol1name=='':
                    self.ShowMessageBox_('ERROR','COLUMN 1 CANNOT BE EMPTY')
                else:
                    query='alter table {} change {} {} {},change {} {} {},change {} {} {},change {} {} {}'.format(self.tablname,col1,modcol1name,modcol1type,col2,modcol2name,modcol2type,col3,modcol3name,modcol3type,col4,modcol4name,modcol4type)
                    temp=query
                    query=''
                    list=[]
                    list1=[]
                    for i in range(len(temp)):
                        if temp[i]==','and temp[i-1]==' ':
                            list.append(i)

                        if ',' in temp[i]:
                            list1.append(i)
                    list3=[]
                    for i in range(len(list)):
                        for j in range(len(list1)):
                            if list[i]== list1[j]:
                                list3.append(list1[j-1])

                    start=0
                    stop=list3[0]+1
                    for i in range(len(list3)):
                        stop=list3[i]
                        query=query+temp[start:stop]
                        start=list[i]
                   
                
                    try:
                        mycursor.execute(query)
                       
                        self.ShowMessageBox('successfull','successfully modified table')
                        mydb.commit()
                        self.close()
                    except Exception:
                        self.ShowMessageBox_('error','error while modifying')


    def dele(self):
        import mysql.connector
        mydb=mysql.connector.connect(host='localhost', user='root',passwd='logon@123',database='python')
        mycursor=mydb.cursor()
        col1name=self.txtdelcol1name.text()
        col2name=self.txtdelcol2name.text()
        col3name=self.txtdelcol3name.text()
        col4name=self.txtdelcol4name.text()
        list1=[col1name,col2name,col3name,col4name]
        todrop=''
        for i in range(4):
            if list1[i]!='':
                todrop= todrop + ',drop ' + list1[i]
        todrop=todrop.lstrip(',')
        todrop=todrop.rstrip(',')
    
        query= 'alter table {} {}'.format(self.tablname,todrop)
        if self.tablname=='':
            self.ShowMessageBox_('error','enter table name')
        elif todrop=='':
            self.ShowMessageBox_('error','enter column name to delete')      
        elif col1name==col2name==col3name==col4name:
            self.ShowMessageBox_('error','all column names are same')        
        else:
            try:
                mycursor.execute(query)
                self.ShowMessageBox('successfull','successfully deleted column')
                mydb.commit()
                sys.exit()
            except Exception:
                self.ShowMessageBox_('error','error while deleting column')


    def cancel(self):
         sys.exit()



    def setupUi(self, MYSQL_ALTER):
        MYSQL_ALTER.setObjectName("MYSQL_ALTER")
        MYSQL_ALTER.resize(970, 634)
        self.label = QtWidgets.QLabel(MYSQL_ALTER)
        self.label.setGeometry(QtCore.QRect(310, 10, 341, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.addframe = QtWidgets.QFrame(MYSQL_ALTER)
        self.addframe.setGeometry(QtCore.QRect(20, 159, 271, 421))
        self.addframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.addframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.addframe.setObjectName("addframe")
        self.label_6 = QtWidgets.QLabel(self.addframe)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_13 = QtWidgets.QLabel(self.addframe)
        self.label_13.setGeometry(QtCore.QRect(10, 310, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_11 = QtWidgets.QLabel(self.addframe)
        self.label_11.setGeometry(QtCore.QRect(10, 230, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_14 = QtWidgets.QLabel(self.addframe)
        self.label_14.setGeometry(QtCore.QRect(10, 150, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.txtcolumn1type = QtWidgets.QLineEdit(self.addframe)
        self.txtcolumn1type.setGeometry(QtCore.QRect(130, 110, 121, 21))
        self.txtcolumn1type.setText("")
        self.txtcolumn1type.setObjectName("txtcolumn1type")
        self.txtcolumn2name = QtWidgets.QLineEdit(self.addframe)
        self.txtcolumn2name.setGeometry(QtCore.QRect(130, 150, 121, 21))
        self.txtcolumn2name.setObjectName("txtcolumn2name")
        self.txtcolumn2type = QtWidgets.QLineEdit(self.addframe)
        self.txtcolumn2type.setGeometry(QtCore.QRect(130, 190, 121, 21))
        self.txtcolumn2type.setObjectName("txtcolumn2type")
        self.label_9 = QtWidgets.QLabel(self.addframe)
        self.label_9.setGeometry(QtCore.QRect(10, 270, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.txtcolumn3type = QtWidgets.QLineEdit(self.addframe)
        self.txtcolumn3type.setGeometry(QtCore.QRect(130, 270, 121, 21))
        self.txtcolumn3type.setObjectName("txtcolumn3type")
        self.label_12 = QtWidgets.QLabel(self.addframe)
        self.label_12.setGeometry(QtCore.QRect(10, 190, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.txtcolumn1name = QtWidgets.QLineEdit(self.addframe)
        self.txtcolumn1name.setGeometry(QtCore.QRect(130, 70, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtcolumn1name.setFont(font)
        self.txtcolumn1name.setText("")
        self.txtcolumn1name.setObjectName("txtcolumn1name")
        self.label_7 = QtWidgets.QLabel(self.addframe)
        self.label_7.setGeometry(QtCore.QRect(10, 110, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.txtcolumn3name = QtWidgets.QLineEdit(self.addframe)
        self.txtcolumn3name.setGeometry(QtCore.QRect(130, 230, 121, 21))
        self.txtcolumn3name.setObjectName("txtcolumn3name")
        self.label_8 = QtWidgets.QLabel(self.addframe)
        self.label_8.setGeometry(QtCore.QRect(10, 70, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.txtcolumn4name = QtWidgets.QLineEdit(self.addframe)
        self.txtcolumn4name.setGeometry(QtCore.QRect(130, 310, 121, 21))
        self.txtcolumn4name.setObjectName("txtcolumn4name")
        self.txtcolumn4type = QtWidgets.QLineEdit(self.addframe)
        self.txtcolumn4type.setGeometry(QtCore.QRect(130, 350, 121, 21))
        self.txtcolumn4type.setObjectName("txtcolumn4type")
        self.label_16 = QtWidgets.QLabel(self.addframe)
        self.label_16.setGeometry(QtCore.QRect(10, 350, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.btnadd = QtWidgets.QPushButton(self.addframe)
        self.btnadd.setGeometry(QtCore.QRect(70, 380, 112, 32))
        self.btnadd.setObjectName("btnadd")
        self.btnadd.clicked.connect(self.tblname)
        self.btnadd.clicked.connect(self.add)
        self.label_6.raise_()
        self.label_14.raise_()
        self.txtcolumn1type.raise_()
        self.label_8.raise_()
        self.txtcolumn2name.raise_()
        self.txtcolumn3type.raise_()
        self.label_9.raise_()
        self.label_13.raise_()
        self.label_12.raise_()
        self.txtcolumn3name.raise_()
        self.txtcolumn1name.raise_()
        self.txtcolumn2type.raise_()
        self.label_7.raise_()
        self.label_11.raise_()
        self.txtcolumn4name.raise_()
        self.txtcolumn4type.raise_()
        self.label_16.raise_()
        self.btnadd.raise_()
        self.modifyframe = QtWidgets.QFrame(MYSQL_ALTER)
        self.modifyframe.setGeometry(QtCore.QRect(290, 160, 291, 421))
        self.modifyframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.modifyframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.modifyframe.setObjectName("modifyframe")
        self.label_15 = QtWidgets.QLabel(self.modifyframe)
        self.label_15.setGeometry(QtCore.QRect(20, 70, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.modifyframe)
        self.label_17.setGeometry(QtCore.QRect(20, 270, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.modifyframe)
        self.label_18.setGeometry(QtCore.QRect(20, 190, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.txtmodcol3type = QtWidgets.QLineEdit(self.modifyframe)
        self.txtmodcol3type.setGeometry(QtCore.QRect(140, 270, 121, 21))
        self.txtmodcol3type.setObjectName("txtmodcol3type")
        self.txtmodcol1type = QtWidgets.QLineEdit(self.modifyframe)
        self.txtmodcol1type.setGeometry(QtCore.QRect(140, 110, 121, 21))
        self.txtmodcol1type.setText("")
        self.txtmodcol1type.setObjectName("txtmodcol1type")
        self.txtmodcol2type = QtWidgets.QLineEdit(self.modifyframe)
        self.txtmodcol2type.setGeometry(QtCore.QRect(140, 190, 121, 21))
        self.txtmodcol2type.setObjectName("txtmodcol2type")
        self.txtmodcol3name = QtWidgets.QLineEdit(self.modifyframe)
        self.txtmodcol3name.setGeometry(QtCore.QRect(140, 230, 121, 21))
        self.txtmodcol3name.setObjectName("txtmodcol3name")
        self.txtmodcol4type = QtWidgets.QLineEdit(self.modifyframe)
        self.txtmodcol4type.setGeometry(QtCore.QRect(140, 350, 121, 21))
        self.txtmodcol4type.setObjectName("txtmodcol4type")
        self.label_20 = QtWidgets.QLabel(self.modifyframe)
        self.label_20.setGeometry(QtCore.QRect(20, 230, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.txtmodcol1name = QtWidgets.QLineEdit(self.modifyframe)
        self.txtmodcol1name.setGeometry(QtCore.QRect(140, 70, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtmodcol1name.setFont(font)
        self.txtmodcol1name.setText("")
        self.txtmodcol1name.setObjectName("txtmodcol1name")
        self.txtmodcol4name = QtWidgets.QLineEdit(self.modifyframe)
        self.txtmodcol4name.setGeometry(QtCore.QRect(140, 310, 121, 21))
        self.txtmodcol4name.setObjectName("txtmodcol4name")
        self.label_21 = QtWidgets.QLabel(self.modifyframe)
        self.label_21.setGeometry(QtCore.QRect(20, 350, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.modifyframe)
        self.label_22.setGeometry(QtCore.QRect(20, 110, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.modifyframe)
        self.label_23.setGeometry(QtCore.QRect(20, 150, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.modifyframe)
        self.label_24.setGeometry(QtCore.QRect(20, 310, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.txtmodcol2name = QtWidgets.QLineEdit(self.modifyframe)
        self.txtmodcol2name.setGeometry(QtCore.QRect(140, 150, 121, 21))
        self.txtmodcol2name.setObjectName("txtmodcol2name")
        self.btnmod = QtWidgets.QPushButton(self.modifyframe)
        self.btnmod.setGeometry(QtCore.QRect(80, 380, 112, 32))
        self.btnmod.setObjectName("btnmod")
        self.btnmod.clicked.connect(self.tblname)
        self.btnmod.clicked.connect(self.mod)
        self.label_30 = QtWidgets.QLabel(self.modifyframe)
        self.label_30.setGeometry(QtCore.QRect(30, 10, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.txtmodcol1type.raise_()
        self.txtmodcol3type.raise_()
        self.label_18.raise_()
        self.label_20.raise_()
        self.label_23.raise_()
        self.label_21.raise_()
        self.txtmodcol4type.raise_()
        self.txtmodcol1name.raise_()
        self.btnmod.raise_()
        self.label_24.raise_()
        self.label_17.raise_()
        self.txtmodcol3name.raise_()
        self.label_15.raise_()
        self.txtmodcol2name.raise_()
        self.txtmodcol4name.raise_()
        self.txtmodcol2type.raise_()
        self.label_22.raise_()
        self.label_30.raise_()
        self.delframe = QtWidgets.QFrame(MYSQL_ALTER)
        self.delframe.setGeometry(QtCore.QRect(580, 160, 371, 421))
        self.delframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.delframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.delframe.setObjectName("delframe")
        self.label_4 = QtWidgets.QLabel(self.delframe)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_25 = QtWidgets.QLabel(self.delframe)
        self.label_25.setGeometry(QtCore.QRect(20, 200, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.delframe)
        self.label_26.setGeometry(QtCore.QRect(20, 80, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.txtdelcol4name = QtWidgets.QLineEdit(self.delframe)
        self.txtdelcol4name.setGeometry(QtCore.QRect(190, 200, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txtdelcol4name.setFont(font)
        self.txtdelcol4name.setObjectName("txtdelcol4name")
        self.txtdelcol1name = QtWidgets.QLineEdit(self.delframe)
        self.txtdelcol1name.setGeometry(QtCore.QRect(190, 80, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txtdelcol1name.setFont(font)
        self.txtdelcol1name.setText("")
        self.txtdelcol1name.setObjectName("txtdelcol1name")
        self.label_27 = QtWidgets.QLabel(self.delframe)
        self.label_27.setGeometry(QtCore.QRect(20, 160, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.txtdelcol3name = QtWidgets.QLineEdit(self.delframe)
        self.txtdelcol3name.setGeometry(QtCore.QRect(190, 160, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txtdelcol3name.setFont(font)
        self.txtdelcol3name.setObjectName("txtdelcol3name")
        self.label_29 = QtWidgets.QLabel(self.delframe)
        self.label_29.setGeometry(QtCore.QRect(20, 120, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.txtdelcol2name = QtWidgets.QLineEdit(self.delframe)
        self.txtdelcol2name.setGeometry(QtCore.QRect(190, 120, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txtdelcol2name.setFont(font)
        self.txtdelcol2name.setObjectName("txtdelcol2name")
        self.btndel = QtWidgets.QPushButton(self.delframe)
        self.btndel.setGeometry(QtCore.QRect(140, 260, 112, 32))
        self.btndel.setObjectName("btndel")
        self.btndel.clicked.connect(self.tblname)
        self.btndel.clicked.connect(self.dele)
        self.label_31 = QtWidgets.QLabel(MYSQL_ALTER)
        self.label_31.setGeometry(QtCore.QRect(70, 60, 171, 91))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(24)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.txttablname = QtWidgets.QLineEdit(MYSQL_ALTER)
        self.txttablname.setGeometry(QtCore.QRect(250, 90, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.txttablname.setFont(font)
        self.txttablname.setObjectName("txttablname")
        self.btncancel = QtWidgets.QPushButton(MYSQL_ALTER)
        self.btncancel.setGeometry(QtCore.QRect(820, 600, 112, 32))
        self.btncancel.setObjectName("btncancel")
        self.btncancel.clicked.connect(self.cancel)
        self.delframe.raise_()
        self.modifyframe.raise_()
        self.addframe.raise_()
        self.label.raise_()
        self.label_31.raise_()
        self.txttablname.raise_()
        self.btncancel.raise_()

        self.retranslateUi(MYSQL_ALTER)
        QtCore.QMetaObject.connectSlotsByName(MYSQL_ALTER)

    def retranslateUi(self, MYSQL_ALTER):
        _translate = QtCore.QCoreApplication.translate
        MYSQL_ALTER.setWindowTitle(_translate("MYSQL_ALTER", "Form"))
        self.label.setText(_translate("MYSQL_ALTER", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">ALTER TABLE</span></p></body></html>"))
        self.label_6.setText(_translate("MYSQL_ALTER", "<html><head/><body><p align=\"center\">ADD COLUMN</p></body></html>"))
        self.label_13.setText(_translate("MYSQL_ALTER", "NEW COLUMN 4 NAME:"))
        self.label_11.setText(_translate("MYSQL_ALTER", "NEW COLUMN 3 NAME:"))
        self.label_14.setText(_translate("MYSQL_ALTER", "NEW COLUMN 2 NAME:"))
        self.label_9.setText(_translate("MYSQL_ALTER", "NEW COLUMN 3 TYPE:"))
        self.label_12.setText(_translate("MYSQL_ALTER", "NEW COLUMN 2 TYPE:"))
        self.label_7.setText(_translate("MYSQL_ALTER", "NEW COLUMN 1 TYPE:"))
        self.label_8.setText(_translate("MYSQL_ALTER", "NEW COLUMN 1 NAME:"))
        self.label_16.setText(_translate("MYSQL_ALTER", "NEW COLUMN 4 Type:"))
        self.btnadd.setText(_translate("MYSQL_ALTER", "ADD"))
        self.label_15.setText(_translate("MYSQL_ALTER", "MOD COLUMN 1 NAME:"))
        self.label_17.setText(_translate("MYSQL_ALTER", "MOD COLUMN 3 TYPE:"))
        self.label_18.setText(_translate("MYSQL_ALTER", "MOD COLUMN 2 TYPE:"))
        self.label_20.setText(_translate("MYSQL_ALTER", "MOD COLUMN 3 NAME:"))
        self.label_21.setText(_translate("MYSQL_ALTER", "MOD COLUMN 4 Type:"))
        self.label_22.setText(_translate("MYSQL_ALTER", "MOD COLUMN 1 TYPE:"))
        self.label_23.setText(_translate("MYSQL_ALTER", "MOD COLUMN 2 NAME:"))
        self.label_24.setText(_translate("MYSQL_ALTER", "MOD COLUMN 4 NAME:"))
        self.btnmod.setText(_translate("MYSQL_ALTER", "MODIFY"))
        self.label_30.setText(_translate("MYSQL_ALTER", "<html><head/><body><p align=\"center\">MODIFY COLUMN</p></body></html>"))
        self.label_4.setText(_translate("MYSQL_ALTER", "<html><head/><body><p align=\"center\">DELETE COLUMN</p><p align=\"center\"><br/></p></body></html>"))
        self.label_25.setText(_translate("MYSQL_ALTER", "DEL COLUMN 4 NAME:"))
        self.label_26.setText(_translate("MYSQL_ALTER", "DEL COLUMN 1 NAME:"))
        self.label_27.setText(_translate("MYSQL_ALTER", "DEL COLUMN 3 NAME:"))
        self.label_29.setText(_translate("MYSQL_ALTER", "DEL COLUMN 2 NAME:"))
        self.btndel.setText(_translate("MYSQL_ALTER", "DELETE"))
        self.label_31.setText(_translate("MYSQL_ALTER", "TABLE NAME: "))
        self.btncancel.setText(_translate("MYSQL_ALTER", "CANCEL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MYSQL_ALTER = QtWidgets.QWidget()
    ui = Ui_MYSQL_ALTER()
    ui.setupUi(MYSQL_ALTER)
    MYSQL_ALTER.show()
    sys.exit(app.exec_())

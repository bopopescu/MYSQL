# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MYSQL_MAINWINDOW.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from MYSQL_CREATEDB import Ui_MYSQL_CREATEDB
from subprocess import call
from MYSQL_CREATEDB import Ui_MYSQL_CREATEDB
from MYSQL_CREATETBL import Ui_MYSQL_CREATETBL
from MYSQL_ALTER import Ui_MYSQL_ALTER
class Ui_MYSQL_MAINWINDOW(object):
    def createdb(self):
        self.MYSQL_CREATEDB = QtWidgets.QWidget()
        self.ui = Ui_MYSQL_CREATEDB()
        self.ui.setupUi(self.MYSQL_CREATEDB)
        self.MYSQL_CREATEDB.show()

    def createtbl(self):
        self.MYSQL_CREATETBL = QtWidgets.QWidget()
        self.ui = Ui_MYSQL_CREATETBL()
        self.ui.setupUi(self.MYSQL_CREATETBL)
        self.MYSQL_CREATETBL.show()
    def altertbl(self):
        self.MYSQL_ALTER = QtWidgets.QWidget()
        self.ui = Ui_MYSQL_ALTER()
        self.ui.setupUi(self.MYSQL_ALTER)
        self.MYSQL_ALTER.show()


    def setupUi(self, MYSQL_MAINWINDOW):
        MYSQL_MAINWINDOW.setObjectName("MYSQL_MAINWINDOW")
        MYSQL_MAINWINDOW.resize(361, 480)
        MYSQL_MAINWINDOW.setToolTipDuration(-1)
        self.label = QtWidgets.QLabel(MYSQL_MAINWINDOW)
        self.label.setGeometry(QtCore.QRect(60, 20, 221, 81))
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnCreateDB = QtWidgets.QPushButton(MYSQL_MAINWINDOW)
        self.btnCreateDB.setGeometry(QtCore.QRect(20, 140, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(19)
        font.setItalic(False)
        self.btnCreateDB.setFont(font)
        self.btnCreateDB.setObjectName("btnCreateDB")
        self.btnCreateTbl = QtWidgets.QPushButton(MYSQL_MAINWINDOW)
        self.btnCreateTbl.setGeometry(QtCore.QRect(20, 180, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(19)
        font.setItalic(False)
        self.btnCreateTbl.setFont(font)
        self.btnCreateTbl.setObjectName("btnCreateTbl")
        self.btnInsertValues = QtWidgets.QPushButton(MYSQL_MAINWINDOW)
        self.btnInsertValues.setGeometry(QtCore.QRect(20, 220, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(19)
        font.setItalic(False)
        self.btnInsertValues.setFont(font)
        self.btnInsertValues.setObjectName("btnInsertValues")
        self.btnUpdateTbl = QtWidgets.QPushButton(MYSQL_MAINWINDOW)
        self.btnUpdateTbl.setGeometry(QtCore.QRect(20, 260, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(19)
        font.setItalic(False)
        self.btnUpdateTbl.setFont(font)
        self.btnUpdateTbl.setObjectName("btnUpdateTbl")
        self.btnAlterTbl = QtWidgets.QPushButton(MYSQL_MAINWINDOW)
        self.btnAlterTbl.setGeometry(QtCore.QRect(20, 300, 161, 31))
        self.btnAlterTbl.clicked.connect(self.altertbl)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(19)
        font.setItalic(False)
        self.btnAlterTbl.setFont(font)
        self.btnAlterTbl.setToolTipDuration(-1)
        self.btnAlterTbl.setCheckable(False)
        self.btnAlterTbl.setChecked(False)
        self.btnAlterTbl.setAutoDefault(False)
        self.btnAlterTbl.setDefault(False)
        self.btnAlterTbl.setFlat(False)
        self.btnAlterTbl.setObjectName("btnAlterTbl")
        self.btnDelDB = QtWidgets.QPushButton(MYSQL_MAINWINDOW)
        self.btnDelDB.setGeometry(QtCore.QRect(20, 340, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(19)
        font.setItalic(False)
        self.btnDelDB.setFont(font)
        self.btnDelDB.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnDelDB.setObjectName("btnDelDB")
        self.btnDelTbl = QtWidgets.QPushButton(MYSQL_MAINWINDOW)
        self.btnDelTbl.setGeometry(QtCore.QRect(20, 380, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(19)
        font.setItalic(False)
        self.btnDelTbl.setFont(font)
        self.btnDelTbl.setObjectName("btnDelTbl")
        self.label_2 = QtWidgets.QLabel(MYSQL_MAINWINDOW)
        self.label_2.setGeometry(QtCore.QRect(170, 440, 181, 31))
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(MYSQL_MAINWINDOW)
        self.frame.setGeometry(QtCore.QRect(10, 120, 341, 311))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.label.raise_()
        self.btnCreateDB.raise_()
        self.btnCreateTbl.raise_()
        self.btnInsertValues.raise_()
        self.btnUpdateTbl.raise_()
        self.btnAlterTbl.raise_()
        self.btnDelDB.raise_()
        self.btnDelTbl.raise_()
        self.label_2.raise_()

        self.retranslateUi(MYSQL_MAINWINDOW)
        QtCore.QMetaObject.connectSlotsByName(MYSQL_MAINWINDOW)

    def retranslateUi(self, MYSQL_MAINWINDOW):
        _translate = QtCore.QCoreApplication.translate
        MYSQL_MAINWINDOW.setWindowTitle(_translate("MYSQL_MAINWINDOW", "Form"))
        self.label.setText(_translate("MYSQL_MAINWINDOW", "MYSQL "))
        self.btnCreateDB.setText(_translate("MYSQL_MAINWINDOW", "CREATE DATABASE"))
        self.btnCreateTbl.setText(_translate("MYSQL_MAINWINDOW", "CREATE TABLE"))
        self.btnInsertValues.setText(_translate("MYSQL_MAINWINDOW", "INSERT VALUES INTO TABLE"))
        self.btnUpdateTbl.setText(_translate("MYSQL_MAINWINDOW", "UPDATE TABLE"))
        self.btnAlterTbl.setText(_translate("MYSQL_MAINWINDOW", "ALTER TABLE"))
        self.btnDelDB.setText(_translate("MYSQL_MAINWINDOW", "DELETE DATABASE"))
        self.btnDelTbl.setText(_translate("MYSQL_MAINWINDOW", "DELETE TABLE"))
        self.label_2.setText(_translate("MYSQL_MAINWINDOW", "<html><head/><body><p><span style=\" font-size:18pt; font-style:italic;\">~</span><span style=\" font-size:18pt; font-style:italic; text-decoration: underline;\">MOHAMED NAVEED</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MYSQL_MAINWINDOW = QtWidgets.QWidget()
    ui = Ui_MYSQL_MAINWINDOW()
    ui.setupUi(MYSQL_MAINWINDOW)
    MYSQL_MAINWINDOW.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MYSQL_MAINWINDOW.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(550, 441)
        Form.setToolTipDuration(-1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 30, 221, 81))
        font = QtGui.QFont()
        font.setFamily("Phosphate")
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnCreateDB = QtWidgets.QPushButton(Form)
        self.btnCreateDB.setGeometry(QtCore.QRect(20, 140, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(19)
        font.setItalic(False)
        self.btnCreateDB.setFont(font)
        self.btnCreateDB.setObjectName("btnCreateDB")
        self.btnCreateTbl = QtWidgets.QPushButton(Form)
        self.btnCreateTbl.setGeometry(QtCore.QRect(20, 180, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(19)
        font.setItalic(False)
        self.btnCreateTbl.setFont(font)
        self.btnCreateTbl.setObjectName("btnCreateTbl")
        self.btnInsertValues = QtWidgets.QPushButton(Form)
        self.btnInsertValues.setGeometry(QtCore.QRect(20, 220, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(19)
        font.setItalic(False)
        self.btnInsertValues.setFont(font)
        self.btnInsertValues.setObjectName("btnInsertValues")
        self.btnUpdateTbl = QtWidgets.QPushButton(Form)
        self.btnUpdateTbl.setGeometry(QtCore.QRect(20, 260, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(19)
        font.setItalic(False)
        self.btnUpdateTbl.setFont(font)
        self.btnUpdateTbl.setObjectName("btnUpdateTbl")
        self.btnAlterTbl = QtWidgets.QPushButton(Form)
        self.btnAlterTbl.setGeometry(QtCore.QRect(20, 300, 161, 31))
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
        self.btnDelDB = QtWidgets.QPushButton(Form)
        self.btnDelDB.setGeometry(QtCore.QRect(20, 340, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(19)
        font.setItalic(False)
        self.btnDelDB.setFont(font)
        self.btnDelDB.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnDelDB.setObjectName("btnDelDB")
        self.btnDelTbl = QtWidgets.QPushButton(Form)
        self.btnDelTbl.setGeometry(QtCore.QRect(20, 380, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(19)
        font.setItalic(False)
        self.btnDelTbl.setFont(font)
        self.btnDelTbl.setObjectName("btnDelTbl")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(330, 390, 181, 31))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "MYSQL "))
        self.btnCreateDB.setText(_translate("Form", "CREATE DATABASE"))
        self.btnCreateTbl.setText(_translate("Form", "CREATE TABLE"))
        self.btnInsertValues.setText(_translate("Form", "INSERT VALUES INTO TABLE"))
        self.btnUpdateTbl.setText(_translate("Form", "UPDATE TABLE"))
        self.btnAlterTbl.setText(_translate("Form", "ALTER TABLE"))
        self.btnDelDB.setText(_translate("Form", "DELETE DATABASE"))
        self.btnDelTbl.setText(_translate("Form", "DELETE TABLE"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt; font-style:italic;\">~</span><span style=\" font-size:18pt; font-style:italic; text-decoration: underline;\">MOHAMED NAVEED</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

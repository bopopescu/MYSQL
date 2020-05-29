# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MYSQL_DELETEDB.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MYSQL_DELETEDB(object):
    def setupUi(self, MYSQL_DELETEDB):
        MYSQL_DELETEDB.setObjectName("MYSQL_DELETEDB")
        MYSQL_DELETEDB.resize(406, 239)
        self.label = QtWidgets.QLabel(MYSQL_DELETEDB)
        self.label.setGeometry(QtCore.QRect(50, 10, 281, 81))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MYSQL_DELETEDB)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btndel = QtWidgets.QPushButton(MYSQL_DELETEDB)
        self.btndel.setGeometry(QtCore.QRect(110, 160, 112, 32))
        self.btndel.setObjectName("btndel")
        self.btncancel = QtWidgets.QPushButton(MYSQL_DELETEDB)
        self.btncancel.setGeometry(QtCore.QRect(240, 160, 112, 32))
        self.btncancel.setObjectName("btncancel")
        self.txtDBname = QtWidgets.QLineEdit(MYSQL_DELETEDB)
        self.txtDBname.setGeometry(QtCore.QRect(182, 110, 211, 31))
        self.txtDBname.setObjectName("txtDBname")
        self.txtDBname.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.btndel.raise_()
        self.btncancel.raise_()

        self.retranslateUi(MYSQL_DELETEDB)
        QtCore.QMetaObject.connectSlotsByName(MYSQL_DELETEDB)

    def retranslateUi(self, MYSQL_DELETEDB):
        _translate = QtCore.QCoreApplication.translate
        MYSQL_DELETEDB.setWindowTitle(_translate("MYSQL_DELETEDB", "Form"))
        self.label.setText(_translate("MYSQL_DELETEDB", "DELETE DATABASE"))
        self.label_2.setText(_translate("MYSQL_DELETEDB", "DATABASE NAME: "))
        self.btndel.setText(_translate("MYSQL_DELETEDB", "DELETE"))
        self.btncancel.setText(_translate("MYSQL_DELETEDB", "CANCEL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MYSQL_DELETEDB = QtWidgets.QWidget()
    ui = Ui_MYSQL_DELETEDB()
    ui.setupUi(MYSQL_DELETEDB)
    MYSQL_DELETEDB.show()
    sys.exit(app.exec_())

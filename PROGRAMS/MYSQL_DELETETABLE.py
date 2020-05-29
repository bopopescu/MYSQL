# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MYSQL_DELETETABLE.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MYSQL_DELETEtable(object):
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

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'infor.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QDialog
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(260, 400)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(30, 130, 201, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(32, 179, 201, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 180, 31, 31))
        self.label.setObjectName("label")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 240, 201, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 310, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.lineEdit.cursorPositionChanged['int','int'].connect(self.label.clear)
        
        
        #槽信号
        self.pushButton.clicked.connect(self.Get_infor)
        
        
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBox.setItemText(0, _translate("Dialog", "律师"))
        self.comboBox.setItemText(1, _translate("Dialog", "学生"))
        self.comboBox.setItemText(2, _translate("Dialog", "工程师"))
        self.comboBox.setItemText(3, _translate("Dialog", "科学家"))
        self.comboBox.setItemText(4, _translate("Dialog", "演员"))
        self.comboBox.setItemText(5, _translate("Dialog", "画家"))
        self.comboBox.setItemText(6, _translate("Dialog", "IT工程师"))
        self.label.setText(_translate("Dialog", "年龄"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "  M"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "  F"))
        self.label_2.setText(_translate("Dialog", "收集您的一些信息，用于推荐"))
        self.pushButton.setText(_translate("Dialog", "进入"))
    def Get_infor(self):
        self.age=self.lineEdit.text()
        self.job=self.comboBox.currentText()
        self.gender=self.comboBox_2.currentText()
        print(self.age,self.job,self.gender)

class query_interface(QDialog):
        def __init__(self):
          super(query_interface, self).__init__()
          self.ui=Ui_Dialog()
          self.ui.setupUi(self)
 
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myapp=query_interface()
    #myapp.setupUi()
    myapp.exec_()
    sys.exit(app.exec_())
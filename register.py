# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QDialog
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
class Ui_Dialog(QDialog,object):
    def setupUi(self, Dialog,MainWindow):
        QDialog.__init__(self)
        # object.__init__(self)
        Dialog.setObjectName("Dialog")
        Dialog.resize(330, 535)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 390, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(100, 40, 101, 91))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("C:/Users/Administrator/Desktop/MainWindow_1.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(70, 150, 183, 231))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 4, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        #
        self.pushButton.clicked.connect(self.save_newUser_data)
        #
        self.review_data()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "注册"))
        self.label_2.setText(_translate("Dialog", "密码"))
        self.label_4.setText(_translate("Dialog", "性别"))
        self.label.setText(_translate("Dialog", "用户名"))
        self.label_3.setText(_translate("Dialog", "年龄"))
        self.comboBox.setItemText(0, _translate("Dialog", "administrator"))
        self.comboBox.setItemText(1, _translate("Dialog", "artist"))
        self.comboBox.setItemText(2, _translate("Dialog", "doctor"))
        self.comboBox.setItemText(3, _translate("Dialog", "educator"))
        self.comboBox.setItemText(4, _translate("Dialog", "engineer"))
        self.comboBox.setItemText(5, _translate("Dialog", "entertainment"))
        self.comboBox.setItemText(6, _translate("Dialog", "executive"))
        self.comboBox.setItemText(7, _translate("Dialog", "healthcare"))
        self.comboBox.setItemText(8, _translate("Dialog", "homemaker"))
        self.comboBox.setItemText(9, _translate("Dialog", "lawyer"))
        self.comboBox.setItemText(10, _translate("Dialog", "librarian"))
        self.comboBox.setItemText(11, _translate("Dialog", "marketing"))
        self.comboBox.setItemText(12, _translate("Dialog", "none"))
        self.comboBox.setItemText(13, _translate("Dialog", "other"))
        self.comboBox.setItemText(14, _translate("Dialog", "programmer"))
        self.comboBox.setItemText(15, _translate("Dialog", "retired"))
        self.comboBox.setItemText(16, _translate("Dialog", "salesman"))
        self.comboBox.setItemText(17, _translate("Dialog", "scientist"))
        self.comboBox.setItemText(18, _translate("Dialog", "student"))
        self.comboBox.setItemText(19, _translate("Dialog", "technician"))
        self.comboBox.setItemText(20, _translate("Dialog", "writer"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "M"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "F"))
        self.label_5.setText(_translate("Dialog", "职业"))
    def save_newUser_data(self):#将新用户的信息放入数据库
        conn = sqlite3.connect(r'db\user_info.db')
        conn.isolation_level = None #这个就是事务隔离级别，默认是需要自己commit才能修改数据库，置为None则自动每次修改都提交,否则为""
        conn.commit()
        cur = conn.cursor()
        user_name=self.lineEdit.text()
        user_pwd=self.lineEdit_2.text()
        user_age=self.lineEdit_3.text()
        user_gender=self.comboBox_2.currentText()
        user_job=self.comboBox.currentText()
        
        
        
        
        #判断用户名是否已经被占用
        data=cur.execute("select * from user_table")
        #     print("d")
        # print(data)
        tell=True
        for i in data:
            if (i[0]==user_name):

                QtWidgets.QMessageBox.critical(self, '错误', '该用户名已经被使用了')
                tell=False
                break
        if(tell==True):
            sql="INSERT INTO user_table(user_name,user_pwd,user_age,user_gender,\
              user_job) VALUES (:d1,:d2,:d3,:d4,:d5)"
            cur.execute(sql,{'d1':user_name,'d2':user_pwd,'d3':user_age,'d4':user_gender,'d5':user_job})
            QtWidgets.QMessageBox.information(self,"您好","注册成功,关闭当前登入窗口，返回主页面，登录您的账号",QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.No)
            conn.commit()
            cur.close()

    def review_data(self):
        conn = sqlite3.connect(r'db\user_info.db')
        conn.isolation_level = None
        conn.commit()
        cur = conn.cursor()
        cur.execute("select * from user_review" )
        res = cur.fetchall()
        row = len(res)  # 数据库表中总行数
        cown = len(res[0])  # 数据库中每行的列
        for i in range(16):
            for j in range(cown):
                item = QtWidgets.QTableWidgetItem(res[i][j])
                # self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(res[i][j]))  # 设置i行j列的内容为Value
                if i % 2 == 0:
                    # item.setBackground(QtGui.QBrush(QtGui.QColor(55, 106, 85)))  # 背景
                    item.setBackground(QtGui.QBrush(QtGui.QColor(221, 240, 237)))  # 背景
                    # item.setForeground(QtGui.QBrush(QtGui.QColor(255, 255, 255)))#字体
                elif i % 2 == 1:
                    # item.setBackground(QtGui.QBrush(QtGui.QColor(73, 90, 128)))
                    item.setBackground(QtGui.QBrush(QtGui.QColor(195, 190, 212)))
                    # item.setForeground(QtGui.QBrush(QtGui.QColor(255, 255, 0)))
                self.tableWidget.setItem(i, j, item)
                QtWidgets.QTableWidget.setItem(i, j, item)
        # count = 23
        # for m in range(0, row - 23):
        #     count = 23 + m
        #     for n in range(cown):
        #         item = QtWidgets.QTableWidgetItem(res[count][n])
        #         if m % 2 == 0:
        #             item.setBackground(QtGui.QBrush(QtGui.QColor(221, 240, 237)))
        #         elif m % 2 == 1:
        #             item.setBackground(QtGui.QBrush(QtGui.QColor(195, 190, 212)))
        #         self.tableWidget_2.setItem(m, n, item)
        cur.close()
        conn.close()
#         data=cur.execute("select * from user_table")

    
        
class query_interface(QDialog):
#     print("hah")
    def __init__(self):
      super(query_interface, self).__init__()
      self.ui=Ui_Dialog()
      self.ui.setupUi(self,MainWindow)
          
 
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myapp=query_interface()
    #myapp.setupUi()
    myapp.exec_()
    sys.exit(app.exec_())


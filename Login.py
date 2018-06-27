from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QDialog
from movielen import Functions
import os
import sqlite3
class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        self.movie_num=[]
        QDialog.__init__(self)
        Dialog.setObjectName("Dialog")
        Dialog.resize(337, 442)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(120, 80, 91, 81))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C:/Users/Administrator/Desktop/MainWindow_1.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(81, 172, 177, 151))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
        #
        self.pushButton.clicked.connect(self.remenber_psw)
        self.pushButton.clicked.connect(self.return_data)
#         self.pushButton.clicked.connect(self.get_movie)
#         self.pushButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        #
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "登录"))
        self.label.setText(_translate("Dialog", "用户名"))
        self.label_2.setText(_translate("Dialog", "用户名"))
        self.radioButton.setText(_translate("Dialog", "记住密码"))
        self.pushButton.setText(_translate("Dialog", "登录"))
        self.user_init()
    def user_init(self):
        old=open(r"db/old_pwd.txt",'r')
        old_pwd=old.readlines()
        tell=os.path.getsize("db/old_pwd.txt")
        if tell==0:
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
        else:
            self.lineEdit.setText(old_pwd[0].split(" ")[0])
            self.lineEdit_2.setText(old_pwd[0].split(" ")[1])
        old.close()
        
    def remenber_psw(self):
        try:
            old_pwd=open(r"db/old_pwd.txt",'w+')
            if self.radioButton.isChecked():
                term=self.lineEdit.text()
                term_2=self.lineEdit_2.text()
                old_pwd.write(term+' ')
                old_pwd.write(term_2)
                old_pwd.close()
        except Exception as err:
            print(err)
        conn = sqlite3.connect(r'db\user_info.db')
        conn.isolation_level = None #这个就是事务隔离级别，默认是需要自己commit才能修改数据库，置为None则自动每次修改都提交,否则为""
        conn.commit()
        cur = conn.cursor()
        data=cur.execute("select * from user_table")
        user_name=self.lineEdit.text().strip(" ").strip('\n')#获取输入框用户名
        user_pwd=self.lineEdit_2.text().strip(" ").strip('\n')
        tell=True
#         print("==",user_name)
#         print('==',user_pwd)
        for i in data:
#             print(i)
            if user_name==i[0]:
#                 print(i[0],i[1])
                if user_name==i[0] and user_pwd==i[1]:
#                     print("1")
                    tell=False
                    self.get_movie()
                    QtWidgets.QMessageBox.information(self,"您好","登录成功,关闭当前登入窗口，返回主页面，并且刷新",QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.No)
                    break
                elif user_name==i[0] and user_pwd!=i[1]:
#                     print("2")
                    QtWidgets.QMessageBox.critical(self, '错误', '密码错误，请重新输入')
                    tell=False
                    break
        if tell==True:
            QtWidgets.QMessageBox.critical(self, '错误', '没有该用户，请重新输入')
#             print("3")     
    def return_data(self):
#         print(self.lineEdit.text(),self.movie_num)
        return self.lineEdit.text(),self.movie_num
    def get_movie(self):
        spark=Functions.function()
        if (int(self.lineEdit.text())>=944):#新用户
#             print("KNN")
            spark.KNN(int(self.lineEdit.text()))
#             print("KNN")
            self.movie_num=spark.Get_movie_recommend()
  
        else:
            spark.person_like=[int(self.lineEdit.text())]
            self.movie_num=spark.Get_movie_recommend()       
class query_interface(QDialog):
#     print("hah")
    def __init__(self):
      super(query_interface, self).__init__()
      self.ui=Ui_Dialog()
      self.ui.setupUi(self)
    def fun(self):
        return self.ui.lineEdit.text().strip(" ").strip('\n'),self.ui.movie_num
          
 
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myapp=query_interface()
    #myapp.setupUi()
    myapp.exec_()
    myapp.fun()
    sys.exit(app.exec_())


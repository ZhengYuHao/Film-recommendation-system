# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '首页.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QDialog
import sys
from movielen import Login
from movielen import register
from movielen import comment
import random
# from movielen import Functions
# import Icon_rc
class Ui_MainWindow(QDialog):
    def setupUi(self, MainWindow):
        QDialog.__init__(self)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1043, 950)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/MainWindow_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 80, 984, 363))
        self.textBrowser.setStyleSheet("background-image: url(images/2.png);\n"
"border-radius:3px;")
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 350, 556, 40))
        self.lineEdit.setAccessibleDescription("")
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"border-top-left-radius:3px;\n"
"border-bottom-left-radius:3px;\n"
"border:1px solid black;")
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(770, 350, 56, 40))
        self.pushButton.setStyleSheet("background-image: url(images/3.png);\n"
"border-top-right-radius:3px;\n"
"border-bottom-right-radius:3px;\n"
"border:1px solid black;")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 203, 60))
        self.label.setStyleSheet("image: url(images/4.png);\n"
"border-radius:3px;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(710, 20, 191, 40))
        self.lineEdit_2.setStyleSheet("font:9pt \"微软雅黑\";\n"
"border-radius:3px;")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
#         self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(910, 20, 93, 40))
#         self.pushButton_2.setStyleSheet("background-color: rgb(93, 202, 255);\n"
# "font: 10pt \"微软雅黑\";\n"
# "color: rgb(255, 255, 255);\n"
# "border-radius:3px;")
#         self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 455, 160, 35))
        self.label_2.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 490, 150, 180))
        self.label_3.setStyleSheet("")
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 675, 160, 35))
        self.label_4.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 710, 150, 180))
        self.label_5.setText("")
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(550, 455, 160, 35))
        self.label_6.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(550, 490, 150, 180))
        self.label_7.setText("")
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(550, 675, 160, 35))
        self.label_8.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(550, 710, 150, 180))
        self.label_9.setText("")
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(200, 490, 290, 180))
        self.textBrowser_2.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(200, 710, 290, 180))
        self.textBrowser_3.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(700, 490, 290, 180))
        self.textBrowser_4.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(700, 710, 290, 180))
        self.textBrowser_5.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.textBrowser_5.setObjectName("textBrowser_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1043, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.SignIn_action = QtWidgets.QAction(MainWindow)
        self.SignIn_action.setObjectName("SignIn_action")
        self.Login_action = QtWidgets.QAction(MainWindow)
        self.Login_action.setObjectName("Login_action")
        self.modify_action = QtWidgets.QAction(MainWindow)
        self.modify_action.setObjectName("modify_action")
        self.exit_action = QtWidgets.QAction(MainWindow)
        self.exit_action.setObjectName("exit_action")
        self.menu.addAction(self.SignIn_action)
        self.menu.addAction(self.Login_action)
        self.menu.addAction(self.modify_action)
        self.menu.addAction(self.exit_action)
        self.menubar.addAction(self.menu.menuAction())
        
        
        
#         self.menubar.addAction(self.menu.menuAction())
#         self.Login_action.triggered.connect(self.login_fun)
        #之间为自定义槽函数
        self.Menu()
        self.visit()
        self.pushButton.clicked.connect(self.jump_comment)
        #
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "遇见一场电影"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "想找什么"))
        self.lineEdit_2.setText(_translate("MainWindow", "游客，您还没有登录哦~"))
#         self.pushButton_2.setText(_translate("MainWindow", "登录"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.SignIn_action.setText(_translate("MainWindow", "注册"))
        self.SignIn_action.setShortcut(_translate("MainWindow", "F1"))
        self.Login_action.setText(_translate("MainWindow", "登录"))
        self.Login_action.setShortcut(_translate("MainWindow", "F2"))
        self.modify_action.setText(_translate("MainWindow", "修改个人信息"))
        self.modify_action.setShortcut(_translate("MainWindow", "F3"))
        self.exit_action.setText(_translate("MainWindow", "退出"))
#         self.textBrowser_2.append('hhhhhh')
        self.exit_action.setShortcut(_translate("MainWindow", "F5"))
    def Menu(self):#函数实现菜单功能的跳转
        self.menubar.addAction(self.menu.menuAction())
        self.Login_action.triggered.connect(self.login_fun)
        
        self.menubar.addAction(self.menu.menuAction())
        self.SignIn_action.triggered.connect(self.Sign)
        
        self.menubar.addAction(self.menu.menuAction())
        self.exit_action.triggered.connect(self.exit_windows)
        
    def jump_comment(self):
        self.title=self.lineEdit.text()#获取输入框内容
        try:
            line_1=self.title+".jpg"
            line_2=self.title+".txt"
            item=open("image/%s"%line_1,'r')
            item_2=open('books/%s'%line_2,'r')
            comment_fun=comment.query_interface(self.title)
            comment_fun.fun()
        
            comment_fun.exec_()
        except Exception as err:
            
            QtWidgets.QMessageBox.critical(self, '错误', '您没有进行输入，或者数据库中无此文件')
        
        
        
        
    def visit(self):#
        self.list_num=[random.randint(0,934) for i in range(4)]
#         self.list_num=[894, 568, 580, 473]
        self.wiki_display_sum()
    def Sign(self):
        exe=register.query_interface()
        exe.exec()
    def login_fun(self):#跳转到登录界面,登录之后更新主页面
        exe=Login.query_interface()
        exe.exec()
        self.user_name,self.user_movielist=exe.fun()
        if self.user_movielist !=[]:
            print(self.user_name,self.user_movielist)
            self.list_num=self.user_movielist#[1,2,3,4]
            self.lineEdit_2.setText('欢迎您'+self.user_name+"用户")
            self.wiki_display_sum()
        
    def exit_windows(self):
        exe=QtWidgets.QApplication()
        exe.exit()
    def wiki_display_sum(self):
        self.wiki_display_1(self.list_num[0]-1)
        self.wiki_display_2(self.list_num[1]-1)
        self.wiki_display_3(self.list_num[2]-1)
        self.wiki_display_4(self.list_num[3]-1)
#         self.wiki_display_5(list_num[4]-1)
            
        
    def wiki_display_1(self,i):
        
        fname_1=open('ml-100k/电影名.txt','r').readlines()
        line=fname_1[i]
#         print(line)
        line=line.replace(":","")
        line=line.replace("*","")
        line=line.replace("?","")
        line=line.replace("&","")
        line=line.replace("/","")
        line=line.strip("\n").strip(")").split(",")
        
        if len(line)>=2:
            term=line[0]
            line[0]=line[1]
            line[1]=term
        line=''.join(line)
        
        #以上为获取匹配的电影名
        line=line.strip("\n").strip(" ").strip(")")
#         print(line)
        self.label_2.setText(line)
        try:
            line_1=line+".jpg"
            line_2=line+".txt"
#             open('ml-100k/电影名s.txt','r').readlines()
            pixmap = QtGui.QPixmap ("image/%s"%line_1)
            fname_2=open('books/%s'%line_2,'r').readlines()
#             print("".join(fname_2))
            item=open("image/%s"%line_1,'r')
            item_2=open('books/%s'%line_2,'r')
        except Exception as err:
            pixmap = QtGui.QPixmap (r"image/404.jpg")
            fname_2="抱歉，我们的数据库中没有这样的文件"
        finally:
            self.label_3.setPixmap (pixmap)  # 在label上显示图片  
            self.label_3.setScaledContents (True)  # 让图片自适应label大小
            self.textBrowser_2.append("".join(fname_2))
#             print("text_2")
    def wiki_display_2(self,i):
        
        fname_1=open('ml-100k/电影名.txt','r').readlines()
        line=fname_1[i]
#         print(line)
        line=line.replace(":","")
        line=line.replace("*","")
        line=line.replace("?","")
        line=line.replace("&","")
        line=line.replace("/","")
        line=line.strip("\n").strip(")").split(",")
        
        if len(line)>=2:
            term=line[0]
            line[0]=line[1]
            line[1]=term
        line=''.join(line)
        
        #以上为获取匹配的电影名
        line=line.strip("\n").strip(" ").strip(")")
#         print(line)
        self.label_6.setText(line)
        try:
            line_1=line+".jpg"
            line_2=line+".txt"
#             open('ml-100k/电影名s.txt','r').readlines()
            pixmap = QtGui.QPixmap ("image/%s"%line_1)
            fname_2=open('books/%s'%line_2,'r').readlines()
            item=open("image/%s"%line_1,'r')
            item_2=open('books/%s'%line_2,'r')
        except Exception as err:
            pixmap = QtGui.QPixmap (r"image/404.jpg")
            fname_2="抱歉，我们的数据库中没有这样的文件"
        finally:
            self.label_7.setPixmap (pixmap)  # 在label上显示图片  
            self.label_7.setScaledContents (True)  # 让图片自适应label大小
            self.textBrowser_4.append("".join(fname_2))
    def wiki_display_3(self,i):
        
        fname_1=open('ml-100k/电影名.txt','r').readlines()
        line=fname_1[i]
#         print(line)
        line=line.replace(":","")
        line=line.replace("*","")
        line=line.replace("?","")
        line=line.replace("&","")
        line=line.replace("/","")
        line=line.strip("\n").strip(")").split(",")
        
        if len(line)>=2:
            term=line[0]
            line[0]=line[1]
            line[1]=term
        line=''.join(line)
        
        #以上为获取匹配的电影名
        line=line.strip("\n").strip(" ").strip(")")
#         print(line)
        self.label_4.setText(line)
        try:
            line_1=line+".jpg"
            line_2=line+".txt"
#             open('ml-100k/电影名s.txt','r').readlines()
            pixmap = QtGui.QPixmap ("image/%s"%line_1)
            fname_2=open('books/%s'%line_2,'r').readlines()
            item=open("image/%s"%line_1,'r')
            item_2=open('books/%s'%line_2,'r')
        except Exception as err:
            pixmap = QtGui.QPixmap (r"image/404.jpg")
            fname_2="抱歉，我们的数据库中没有这样的文件"
        finally:
            self.label_5.setPixmap (pixmap)  # 在label上显示图片  
            self.label_5.setScaledContents (True)  # 让图片自适应label大小
            self.textBrowser_3.append("".join(fname_2))
    
    
    def wiki_display_4(self,i):
        
        fname_1=open('ml-100k/电影名.txt','r').readlines()
        line=fname_1[i]
#         print(line)
        line=line.replace(":","")
        line=line.replace("*","")
        line=line.replace("?","")
        line=line.replace("&","")
        line=line.replace("/","")
        line=line.strip("\n").strip(")").split(",")
        
        if len(line)>=2:
            term=line[0]
            line[0]=line[1]
            line[1]=term
        line=''.join(line)
        
        #以上为获取匹配的电影名
        line=line.strip("\n").strip(" ").strip(")")
#         print(line)
        self.label_8.setText(line)
        try:
            line_1=line+".jpg"
            line_2=line+".txt"
#             open('ml-100k/电影名s.txt','r').readlines()
            pixmap = QtGui.QPixmap ("image/%s"%line_1)
            fname_2=open('books/%s'%line_2,'r').readlines()
            item=open("image/%s"%line_1,'r')
            item_2=open('books/%s'%line_2,'r')
        except Exception as err:
            pixmap = QtGui.QPixmap (r"image/404.jpg")
            fname_2="抱歉，我们的数据库中没有这样的文件"
        finally:
            self.label_9.setPixmap (pixmap)  # 在label上显示图片  
            self.label_9.setScaledContents (True)  # 让图片自适应label大小
            self.textBrowser_5.append("".join(fname_2))
 
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)   

    win = QtWidgets.QMainWindow()   
    myapp = Ui_MainWindow()
    myapp.setupUi(win)
    win.setWindowIcon(QtGui.QIcon('images/MainWindow_1.png'))
    win.show()
    sys.exit(app.exec_()) 

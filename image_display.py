# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image_display.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QDialog
from _nsis import err
from movielen import Functions

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(447, 583)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(250, 50, 91, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(340, 50, 81, 51))
        self.label.setObjectName("label")
#         
#         hbox = QtWidgets.QHBoxLayout (self) 
        pixmap = QtGui.QPixmap (r"image\404.jpg")  # 按指定路径找到图片  
        self.label.setPixmap (pixmap)  # 在label上显示图片  
        self.label.setScaledContents (True)  # 让图片自适应label大小 
        self.label.setText("laji")
#         self.label.set 
#         lbl.setPixmap(QPixmap(""))#移除label上的图片  
#         hbox.addWidget (self.label)  
        
        
        
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(340, 100, 81, 51))
        self.label_2.setObjectName("label_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(250, 100, 91, 51))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(340, 150, 81, 51))
        self.label_3.setObjectName("label_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(250, 150, 91, 51))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(340, 200, 81, 51))
        self.label_4.setObjectName("label_4")
        self.textBrowser_4 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_4.setGeometry(QtCore.QRect(250, 200, 91, 51))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(340, 250, 81, 51))
        self.label_5.setObjectName("label_5")
        self.textBrowser_5 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_5.setGeometry(QtCore.QRect(250, 250, 91, 51))
        self.textBrowser_5.setObjectName("textBrowser_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "image_1"))
        self.label_2.setText(_translate("Dialog", "image_2"))
        self.label_3.setText(_translate("Dialog", "image_3"))
        self.label_4.setText(_translate("Dialog", "image_4"))
        self.label_5.setText(_translate("Dialog", "image_5"))
        self.wiki_display_sum()
#         pixmap = QtGui.QPixmap (r"")  # 按指定路径找到图片  
#         self.label.setPixmap (pixmap)  # 在label上显示图片  
#         self.label.setScaledContents (True)  # 让图片自适应label大小 
    
#         self.textBrowser.append("射雕英雄传")
    def wiki_display_sum(self):
        fun=Functions.function()
        fun.person_like=[1,2,3,4,5]
        list_num=fun.Get_movie_recommend()
#         list_num=[78,263,45,676,877]
        self.wiki_display_1(list_num[0]-1)
        self.wiki_display_2(list_num[1]-1)
        self.wiki_display_3(list_num[2]-1)
        self.wiki_display_4(list_num[3]-1)
        self.wiki_display_5(list_num[4]-1)
            
        
    def wiki_display_1(self,i):
        
        fname_1=open('ml-100k/电影名.txt','r').readlines()
        line=fname_1[i]
        print(line)
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
        print(line)
        
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
#             fname_2="抱歉，我们的数据库中没有这样的文件"
        finally:
            self.label.setPixmap (pixmap)  # 在label上显示图片  
            self.label.setScaledContents (True)  # 让图片自适应label大小
            self.textBrowser.append("".join(fname_2))
    def wiki_display_2(self,i):
        
        fname_1=open('ml-100k/电影名.txt','r').readlines()
        line=fname_1[i]
        print(line)
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
        print(line)
        
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
#             fname_2="抱歉，我们的数据库中没有这样的文件"
        finally:
            self.label_2.setPixmap (pixmap)  # 在label上显示图片  
            self.label_2.setScaledContents (True)  # 让图片自适应label大小
            self.textBrowser_2.append("".join(fname_2))
    def wiki_display_3(self,i):
        
        fname_1=open('ml-100k/电影名.txt','r').readlines()
        line=fname_1[i]
        print(line)
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
        print(line)
        
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
#             fname_2="抱歉，我们的数据库中没有这样的文件"
        finally:
            self.label_3.setPixmap (pixmap)  # 在label上显示图片  
            self.label_3.setScaledContents (True)  # 让图片自适应label大小
            self.textBrowser_3.append("".join(fname_2))
    
    
    def wiki_display_4(self,i):
        
        fname_1=open('ml-100k/电影名.txt','r').readlines()
        line=fname_1[i]
        print(line)
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
        print(line)
        
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
#             fname_2="抱歉，我们的数据库中没有这样的文件"
        finally:
            self.label_4.setPixmap (pixmap)  # 在label上显示图片  
            self.label_4.setScaledContents (True)  # 让图片自适应label大小
            self.textBrowser_4.append("".join(fname_2))
    
    def wiki_display_5(self,i):
        
        fname_1=open('ml-100k/电影名.txt','r').readlines()
        line=fname_1[i]
        print(line)
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
        print(line)
        
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
#             fname_2="抱歉，我们的数据库中没有这样的文件"
        finally:
            self.label_5.setPixmap (pixmap)  # 在label上显示图片  
            self.label_5.setScaledContents (True)  # 让图片自适应label大小
            self.textBrowser_5.append("".join(fname_2))
            

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

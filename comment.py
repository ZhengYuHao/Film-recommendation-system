# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'comment.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QDialog
import sqlite3
from datetime import datetime

class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
#         self.line='Toy Story'
        #
        Dialog.setObjectName("Dialog")
        QDialog.__init__(self)
        Dialog.resize(967, 767)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 50, 161, 201))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setText("")
#         self.label.setPixmap(QtGui.QPixmap("C:/Users/Administrator/Desktop/1.jpg"))
#         self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(180, 50, 331, 201))
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 19, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 20, 121, 21))
        self.label_4.setObjectName("label_4")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(520, 110, 431, 601))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(19)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(530, 50, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 270, 481, 436))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
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
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
                    
                    
        #
#         self.fun()
        #
                   
        self.pushButton.clicked.connect(self.save_database)           
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    

        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
#         self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
# "<p style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:28px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333; background-color:#ffffff;\">《射雕英雄传》是</span><a href=\"https://baike.baidu.com/item/%E9%87%91%E5%BA%B8\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; text-decoration: underline; color:#136ec2;\">金庸</span></a><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333;\">创作的长篇武侠小说，最初连载于1957～1959年的《香港商报》，后收录在《金庸作品集》中，</span><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; color:#3366cc;\"> [1]</span><a name=\"ref_[1]_5297005\"></a><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#136ec2;\"> </span><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333;\">是金庸“</span><a href=\"https://baike.baidu.com/item/%E5%B0%84%E9%9B%95%E4%B8%89%E9%83%A8%E6%9B%B2\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; text-decoration: underline; color:#136ec2;\">射雕三部曲</span></a><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333;\">”的第一部。</span></p>\n"
# "<p style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:28px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333; background-color:#ffffff;\">《射雕英雄传》以宁宗庆元五年（1199年）至成吉思汗逝世（1227年）这段历史为背景，反映了南宋抵抗金国与蒙古两大强敌的斗争，充满爱国的民族主义情愫。</span><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; color:#3366cc;\"> [2]</span><a name=\"ref_[2]_5297005\"></a><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#136ec2;\"> </span></p>\n"
# "<p style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:28px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#333333; background-color:#ffffff;\">该小说历史背景突出，场景纷繁，气势宏伟，具有鲜明的“英雄史诗”风格；在人物创造与情节安排上，它打破了传统武侠小说一味传奇，将人物作为情节附庸的模式，坚持以创造个性化的人物形象为中心，坚持人物统帅故事，按照人物性格的发展需要及其内在可能性、必然性来设置情节，从而使这部小说达到了事虽奇人却真的妙境。</span><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; color:#3366cc;\"> [1]</span><a name=\"ref_[1]_5297005\"></a><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14px; color:#136ec2;\"> </span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "电影名:"))
#         self.label_4.setText(_translate("Dialog", "射雕英雄传"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "2"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "3"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "4"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "5"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "6"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Dialog", "7"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Dialog", "8"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Dialog", "10"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("Dialog", "11"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("Dialog", "12"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("Dialog", "13"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("Dialog", "14"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("Dialog", "16"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("Dialog", "17"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("Dialog", "18"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("Dialog", "19"))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("Dialog", "20"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "电影名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "评分"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "评论内容"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "时间"))
        self.label_8.setText(_translate("Dialog", "热门评论"))
        self.label_6.setText(_translate("Dialog", "评论时间"))
        self.label_5.setText(_translate("Dialog", "评论内容"))
        self.label_2.setText(_translate("Dialog", "评分"))
        self.comboBox.setItemText(0, _translate("Dialog", "10"))
        self.comboBox.setItemText(1, _translate("Dialog", "9"))
        self.comboBox.setItemText(2, _translate("Dialog", "8"))
        self.comboBox.setItemText(3, _translate("Dialog", "7"))
        self.comboBox.setItemText(4, _translate("Dialog", "6"))
        self.comboBox.setItemText(5, _translate("Dialog", "5"))
        self.comboBox.setItemText(6, _translate("Dialog", "4"))
        self.comboBox.setItemText(7, _translate("Dialog", "3"))
        self.comboBox.setItemText(8, _translate("Dialog", "2"))
        self.comboBox.setItemText(9, _translate("Dialog", "1"))
        self.comboBox.setItemText(10, _translate("Dialog", "0"))
        self.pushButton.setText(_translate("Dialog", "提交"))
    def fun(self,line):#接受来自主窗口的文件。同时更新当前窗口
#         self.line=''
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
            self.label_4.setText(line)
            self.label.setPixmap (pixmap)  # 在label上显示图片  
            self.label.setScaledContents (True)  # 让图片自适应label大小
            self.textBrowser.append("".join(fname_2))
    def save_database(self):#将评论的内容存入数据库
        conn = sqlite3.connect(r'db\user_info.db')
        conn.isolation_level = None #这个就是事务隔离级别，默认是需要自己commit才能修改数据库，置为None则自动每次修改都提交,否则为""
        conn.commit()
        cur = conn.cursor()
        sql_1="create table if not exists user_review(movie_name varchar(128), movie_stars varchar(128),movie_reviews varchar(128),review_time varchar(128))"
        cur.execute(sql_1)
        
        movie_name=self.label_4.text()
        movie_stars=self.comboBox.currentText()
        movie_reviews=self.textEdit.toPlainText()
        reviwe_time=str(datetime.now())
#         print(movie_name+movie_stars+movie_reviews+reviwe_time)
        if movie_reviews.strip(' ')!='':
            self.label_7.setText(reviwe_time)
    #         term_arry=["射雕英雄传","5","好看",str(datetime.now())]
            conn.commit()
            sql ="INSERT INTO user_review (movie_name,movie_stars,movie_reviews,review_time) VALUES (:d1,:d2,:d3,:d4)"#     print("3")
            cur.execute(sql,{'d1':movie_name,'d2':movie_stars,'d3':movie_reviews,'d4':reviwe_time})
            conn.commit()
            cur.close()
            conn.close()
        else:
            QtWidgets.QMessageBox.critical(self, '错误', '您还没用撰写相关评论，无法提交')
        
class query_interface(QDialog):
#     print("hah")
    def __init__(self,tit):
      super(query_interface, self).__init__()
      self.ui=Ui_Dialog()
      self.ui.setupUi(self)
      self.tit=tit
    def fun(self):
        
        self.ui.fun(self.tit)
#       self.ui.line=title
      
 
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
#     t=input("输入电影名:")
    myapp=query_interface('Toy Story')
    myapp.fun()
    #myapp.setupUi()
    myapp.exec_()
#     myapp.fun()
    sys.exit(app.exec_())


'''
Created on 2018年5月30日
@author: Administrator
'''
from sklearn.neighbors import NearestNeighbors  
import numpy as np 
from scipy.stats._stats_mstats_common import linregress\

from pyspark import SparkContext
from pyspark.mllib.recommendation import Rating
from pyspark.mllib.recommendation import ALS
import sqlite3
import re  
import sys  
import urllib  
import os  
import requests 

class function():
    def KNN(self,per):
        print("person",per)
        data=open(r"ml-100k\用户表.txt",'r').readlines()
        # print(data)
        # 
#         person=input("输入你的年龄、性别、和职业").strip().split()
        # print(person)
        conn = sqlite3.connect(r'db\user_info.db')
        conn.isolation_level = None #这个就是事务隔离级别，默认是需要自己commit才能修改数据库，置为None则自动每次修改都提交,否则为""
        conn.commit()
        cur = conn.cursor()
        print("person",per)
        person=cur.execute("select * from user_table where user_name=%s"%per)
        print("person",per)
        for i in person:
            person=i
            break
#         person=[25,'M','scientist']
#         print(list(person))
        person=list(person)
        train=[]#
        for line in data:#获取用户的相关信息，用于k近邻算法的训练集
            person[2]=int(person[2])
            line=line.strip().split('|')
            line[1]=int(line[1])
             
            if line[2]==person[3]:#性别相同时，归一化为0,否则为1
                line[2]=0
            else:
                line[2]=1
                 
            if line[3]==person[4]:#职业相同时，归一化为0，否者为1
                line[3]=0
            else:
                line[3]=1
             
            if abs(line[1]-person[2])==0:
                line[1]=0
            elif abs(line[1]-person[2])>=1 and abs(line[1]-person[2])<=5:
                line[1]=1
            elif abs(line[1]-person[2])>5 and abs(line[1]-person[2])<=10:
                line[1]=2
            elif abs(line[1]-person[2])>10 and abs(line[1]-person[2])<=15:
                line[1]=3
            elif abs(line[1]-person[2])>15 and abs(line[1]-person[2])<=20:
                line[1]=4
            elif abs(line[1]-person[2])>20 and abs(line[1]-person[2])<=25:
                line[1]=5
            else:
                line[1]=6
            
            train.append(line[1:-1])
#         print(self.train)
        X=np.array(train)
        nbrs = NearestNeighbors(n_neighbors=2, algorithm="ball_tree").fit(X)  
        #返回距离每个点k个最近的点和距离指数，indices可以理解为表示点的下标，distances为距离  
        distances, indices = nbrs.kneighbors([[0,0,0]])
        self.person_like=indices.tolist()[0]#person_like为预测的人
        print(self.person_like)
#         return (person_like)
    def Get_movie_recommend(self):#使用spark的ALS算法
#         self.KNN()
        sc=SparkContext()
        sc.master
        rawUserData = sc.textFile(r"ml-100k\u.data")
        rawRatings = rawUserData.map(lambda line: line.split("\t")[:3] ) 
        ratingsRDD = rawRatings.map(lambda x: (x[0],x[1],x[2])) 
        numUsers = ratingsRDD.map(lambda x: x[0] ).distinct().count()
        numMovies = ratingsRDD.map(lambda x: x[1]).distinct().count() 
        ratingsRDD.persist()
        model = ALS.train(ratingsRDD, 10, 10, 0.01)
        itemRDD = sc.textFile(r"ml-100k\u.item") 
        movieTitle= itemRDD.map( lambda line : line.split("|")).map(lambda a: (float(a[0]),a[1])).collectAsMap()          
        recommendP= model.recommendProducts(self.person_like[0],4)#self.person_like[0]为需要进行预测的人，新用户通过kNN进行匹配，
#         老用户则通过登录的账号
        self.term=[]
        for p in recommendP:
            print(p[1])
            a=[1,1,1]#列表保存数据
            a[0]=str(p[0])
            a[1]=str(movieTitle[p[1]])
            a[2]=str(p[2])
            self.term.append(int(p[1]))
            print("对用户"+ str(p[0])+"推荐电影"+ str(movieTitle[p[1]])+"推荐评分"+ str(p[2]))         
#         print(self.term)
        return self.term#返回推荐的电影编号
# a=function()
# b=a.KNN(5555)
# # #
# bb=153
# a.person_like=[bb]
# b=a.Get_movie_recommend()
# print(b)

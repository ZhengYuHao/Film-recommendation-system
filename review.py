'''
Created on 2018年6月10日

@author: Administrator
'''
import sqlite3
from datetime import datetime
#该函数实现对电影的评论(包含评论的电影名，评分，评论，以及时间戳)
conn = sqlite3.connect(r'db\user_info.db')
conn.isolation_level = None #这个就是事务隔离级别，默认是需要自己commit才能修改数据库，置为None则自动每次修改都提交,否则为""
conn.commit()
cur = conn.cursor()
sql_1="create table if not exists user_review(movie_name varchar(128), movie_stars varchar(128),movie_reviews varchar(128),review_time varchar(128))"
cur.execute(sql_1)
term_arry=["射雕英雄传","5","好看",str(datetime.now())]
conn.commit()
sql ="INSERT INTO user_review (movie_name,movie_stars,movie_reviews,review_time) VALUES (:d1,:d2,:d3,:d4)"#     print("3")
cur.execute(sql,{'d1':term_arry[0],'d2':term_arry[1],'d3':term_arry[2],'d4':term_arry[3]})
conn.commit()
cur.close()
conn.close()
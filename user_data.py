'''
Created on 2018年6月10日

@author: Administrator
'''
import sqlite3

conn = sqlite3.connect(r'db\user_info.db')
conn.isolation_level = None #这个就是事务隔离级别，默认是需要自己commit才能修改数据库，置为None则自动每次修改都提交,否则为""
conn.commit()
cur = conn.cursor()
sql_1="create table if not exists user_table(user_name varchar(128), user_pwd varchar(128),user_age varchar(128),user_gender varchar(128),user_job varchar(128))"
cur.execute(sql_1)
conn.commit()
file=open(r"ml-100k/用户表.txt",'r').readlines()
for line in file:
    term_arry=line.split("|")[0:-1]
    sql ="INSERT INTO user_table (user_name,user_pwd,user_age,user_gender,user_job) VALUES (:d1,:d2,:d3,:d4,:d5)"#     print("3")
    cur.execute(sql,{'d1':term_arry[0],'d2':term_arry[0],'d3':term_arry[1],'d4':term_arry[2],'d5':term_arry[3]})
    conn.commit()
cur.close()
conn.close()

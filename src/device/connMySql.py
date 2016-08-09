'''
Created on 2015 year 8  mouth 1 day

@author: Administrator
'''
# coding=utf-8
import MySQLdb


class conn:
    def connDB(self):        
        conn=MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="",db="client_performance")       
        return conn
    def cursor(self,conn):
        cur=conn.cursor()
        return cur
    
    def create(self,cur,tableName):
        sql1="use client_performance"
        cur.execute(sql1)        
        sql="create table "+tableName+"(id int(4) not null primary key auto_increment,url char(200) not null,code char(10) not null,blocked char(10) not null,send char(10) not null,wait char(10) not null,receive char(10) not null,ttfb char(10) not null,network char(10) not null)"
        cur.execute(sql)

           
    def INSERT(self,cur,tableName,url, code, blocked, send, wait, receive, ttfb, network):
        cur.execute("insert into simple0821181238(url, code, blocked, send, wait, receive, ttfb, network)values('%s','%s','%s','%s','%s','%s','%s','%s')"%(url,code, blocked, send, wait, receive, ttfb, network))
        
    def end(self,cur,conn):  
        conn.commit()
        #cur.close() 
        #conn.close()
        
        
        

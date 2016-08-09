'''
Created on 2015 8 21

@author: Administrator
'''
import MySQLdb

tableName='simple0821171846'
conn=MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="",db="client_performance")
cur=conn.cursor()
        #url, code, blocked, send, wait, receive, ttfb, network
        #sql="insert into simplesummary values(%s,%s,%s,%s,%s,%s,%s,%s)"
        #tmp=(url,code,blocked,send,wait,receive,ttfb,network)
        #cur.executemany(sql,tmp)
        
#sql="create table simpleTime(id int(4) not null primary key auto_increment,url char(50) not null,code char(3) not null,blocked char(10) not null,send char(10) not null,wait char(10) not null,receive char(10) not null,ttfb char(10) not null,network char(10) not null)"
#cur.execute(sql)
url='12121'
code=200
cur.execute("insert into simple0821181238(url, code, blocked, send, wait, receive, ttfb, network)values('%s','%s',%s,%s,%s,%s,%s,%s)"%(url,code, "blocked", "send", "wait", "receive", "ttfb", "network"))
#cur.execute(sql)  
cur.close()
conn.commit()
conn.close()
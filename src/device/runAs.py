'''
Created on 2015 year 8 mouth 21 day

@author: Administrator
'''
import pythonTohttpWatch
import time
tableName='simple'+time.strftime("%m%d%H%M%S")
run=pythonTohttpWatch.toWatch()
plugin=run.create()
run.excute(plugin,tableName)
run.close(plugin)
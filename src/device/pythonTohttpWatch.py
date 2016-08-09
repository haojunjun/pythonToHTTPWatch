'''
Created on 2015 year 8 mouth 21 day

@author: Administrator
'''
import win32com.client
import connMySql
conn=connMySql.conn()
con=conn.connDB()
cur=conn.cursor(con)

class toWatch:
    def create(self):
        #create a new instance of httpwatch in ie
        control=win32com.client.Dispatch('HttpWatch.Controller')
        #open the ie browser
        plugin=control.IE.new()
    
        #start recording http traffic
        plugin.Log.EnableFilter(False)
        #plugin.clearCache
        plugin.Record()
        #goto to the url and wait for the page to be loaded
        plugin.GotoURL("www.xnw.com")
        control.Wait(plugin,-1)
        #stop recording
        plugin.Stop()
        return plugin
    
       
    def excute(self,plugin,tableName):
        print(plugin.Log.entries.count)
        #print(plugin.Log..entries)
        conn.create(cur,tableName)
       
        for s in plugin.Log.entries:
            url=s.URL
            code=str(s.result)
            blocked=str(s.timings.blocked.Duration)
            send=str(s.timings.Send.Duration)
            wait=str(s.timings.Wait.Duration)
            receive=str(s.timings.Receive.Duration)
            ttfb=str(s.timings.TTFB.Duration)
            network=str(s.timings.NetWork.Duration)
            
            conn.INSERT(cur,tableName,url,code,blocked,send,wait,receive,ttfb,network)
        

          
            #print(s.URL)
            #print(s.time)
            #print('code:'+str(s.result))
            #print('Blocked:'+str(s.timings.blocked.Duration))
            #print('Send:'+str(s.timings.Send.Duration))
            #print('Wait:'+str(s.timings.Wait.Duration))
            #print('Receive:'+str(s.timings.Receive.Duration))
            #print('TTFB:'+str(s.timings.TTFB.Duration))
            #print('NetWork:'+str(s.timings.NetWork.Duration))
        return map
    def close(self,plugin):
        plugin.CloseBrowser()


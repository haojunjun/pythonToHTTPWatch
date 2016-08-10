'''
Created on 2016-8-9

@author: Xcar
'''
import win32com.client

#create a new instance of httpwatch in firefox
control=win32com.client.Dispatch('HttpWatch.Controller')
#open the ie browser
plugin=control.firefox.new()

#close Filter
plugin.Log.EnableFilter(False)
plugin.Clear()
plugin.clearCache
#start recording http traffic
plugin.Record()
#goto to the url and wait for the page to be loaded
plugin.GotoURL("a.xcar.com.cn")
# don't return until the page loads
control.Wait(plugin,-1)
#stop recording
plugin.Stop()
        
    
print(plugin.Log.entries.count)
    
for s in plugin.Log.entries:
    print(s.URL)
    print(s.time)
    print('code:'+str(s.result))
  
    #print('Blocked:'+str(s.Timings.Blocked.Duration))
    #print('Send:'+str(s.timings.Send.Duration))
    #print('Wait:'+str(s.timings.Wait.Duration))
    #print('Receive:'+str(s.timings.Receive.Duration))
    #print('TTFB:'+str(s.timings.TTFB.Duration))
    #print('NetWork:'+str(s.timings.NetWork.Duration))
Entries = plugin.Log.Pages.Item(0).Entries
summary = Entries.summary   
print"Total time to load page (secs):", summary.Time

plugin.CloseBrowser()
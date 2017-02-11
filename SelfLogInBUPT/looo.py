'''
北京邮电大学自动登录程序

'''
import urllib.request
##url="http://10.3.8.211/a11.htm"
url="http://10.3.8.211"
##data="DDDDD=2014010000&upass=mimapassword&0MKKey="
data =  urllib.parse.urlencode({'DDDDD':'2011010xxx','upass':'your passord','0MKKey':''})
data = data.encode('utf-8')
resp=urllib.request.urlopen(url,data)

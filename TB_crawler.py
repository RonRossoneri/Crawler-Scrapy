# -*- coding: utf-8 -*- 

import string, urllib2

def baidu_tieba(url, begin_page, end_page):
	for i in range (begin_page, end_page + 1):
		sName = string.zfill(i, 5) + 'html'
		print 'Downing page No.'+ str(i),', stroing it as', sName,'......'
		f = open(sName, 'w') 
		m = urllib2.urlopen(url + str(i)).read()
		f.write(m)
		f.close

# 这个是山东大学的百度贴吧中某一个帖子的地址
#bdurl = 'http://tieba.baidu.com/p/2296017831?pn='
#iPostBegin = 1
#iPostEnd = 10

url = str(raw_input(u'input your url here ending at pn= : \n'))

begin_page = int(raw_input(u'input starting page: \n'))

end_page = int(raw_input(u'input ending page: \n'))

baidu_tieba(url, begin_page, end_page)


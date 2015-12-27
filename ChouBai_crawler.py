# -*- coding: utf-8 -*- 

import urllib2
import urllib
import re
import thread
import time


class HTML_Tool(object):
	"""docstring for HTML_Tool"""
	BgnCharToNoneRex = re.compile("(\t|\n| |<a.*?>|<img.*?>)")
	EndCharToNoneRex = re.compile("<.*?>")
	BgnPartRex = re.compile("<p.*?>")
	CharToNewLineRex = re.compile("(<br/>|</p>|<tr>|<div>|</div>)")
	CharToNextTabRex = re.compile("<td>")
	
	replaceTab = [("&lt;","<"),("&gt;",">"),("&amp;","&"),("&amp;","\""),("&nbsp;"," ")]

	def replaceChar(self, x):
		x = self.BgnCharToNoneRex.sub("",x)
		x = self.BgnPartRex.sub("\n    ",x)
		x = self.CharToNewLineRex.sub("\n",x)
		x = self.CharToNextTabRex.sub("\t",x)
		x = self.EndCharToNoneRex.sub("",x)

		for t in self.replaceTab:
			x = x.replace(t[0], t[1])
		return x
		

class Spider:
	
    def __init__(self):
		self.page = 1  # page是一个指数
		self.pages = []  #pages 是存页码的一个list
		self.myTool = HTML_Tool()
		self.enable = False


		#这一段是将所有的文字拿出来，添加到列表中的程序
    def GetPage(self, page):
		myurl = "http://m.qiushibaike.com/hot/page/" + page

		# here I change the header to Mac OSX
		user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1)'
		header = {'User-Agent' : user_agent}
		req = urllib2.Request(myurl, headers = header)
		Myrespone = urllib2.urlopen(req)
		Mypage = Myrespone.read()
		if Mypage:
			print '拿到最初的pageeeeeeee啦~~'

		#把这些拿到的数据变成utf8code
		Mycode = Mypage.decode("utf-8")

		myItem = re.findall(r'<div.*?class="content".*?title="(.*?)">(.*?)</div>', Mycode, re.S)
		# similar to the java replaceAll, but with more functionality

		items = []
		print '处理标题和内容' 
		for item in myItem:
			# 
			items.append([item[0].replace("\n",""), item[1].replace("\n","")])
		return items

    
    def LoadPage(self):
		while self.enable:

			# 如果pages数组中的内容小于2
			if len(self.pages) < 2:
				try:
					print"获取新页面中·····"
					#获取新页面
					Mypage = self.GetPage(str(self.page))
					self.page += 1
					self.pages.append(Mypage)
				except Exception, e:
					print "无法链接糗事百科"

			else:
				print "要睡啦要睡啦~"
				time.sleep(1)

    
    def showPage(self, q, page):

		for items in q:
		    print u'第%d页' % page, items[0]
		    print self.myTool.replaceChar(items[1])
		    myInput = raw_input()
		    if myInput == 'quit':
			    self.enable = False
			    break


    def Start(self):
		self.enable = True
		page = self.page

		print '正在加载中请稍后·····'

		thread.start_new_thread(self.LoadPage())

		
		while self.enable:
			if self.pages:
				nowPage = self.pages[0]
				del self.pages[0]
				print '要load page啦~'
				self.showPage(nowPage, page)
				page += 1


    
    
print 'press enter to start'    
raw_input(' ')    
myModel = Spider()    
myModel.Start()    


		
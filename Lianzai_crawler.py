# -*- coding: utf-8 -*-

import string
import urllib2
import re

class HTML_tool:

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

class Lianzai_crawler:
	"""docstring for Lianzai_cramlwr"""
	def __init__(self, url):
		self.myUrl = url + '?see_lz=1'
		self.datas = []
		self.myTool = HTML_tool()
		print u'开始爬了咔嚓咔嚓'

	def Tb_crawler(self):
		# user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) '
		
		# header = {'User-Agent' : user_agent}

		# req = urllib2.Request(self.myUrl, headers = header)
		
		# myPage = urllib2.urlopen(req).read()
		myPage = urllib2.urlopen(self.myUrl).read().decode("utf-8")

		endPage = self.Page_Counter(myPage)

		title = self.Find_Title(myPage)
		print title

		self.save_data(self.myUrl, title, endPage)


	def Page_Counter(self, myPage):
		match = re.search(r'<span class="red">(\d+?)</span>', myPage, re.S)
		if match:
			endPage = int(match.group(1))
			#print '共有' + endPage + '页内容'
			print u'爬虫报告：发现楼主共有%d页的原创内容' % endPage 
		else:
			endPage = 0
			print '无法提取页数'
		return endPage

		# to find the title, for the name of files to be saved
	def Find_Title(self, myPage):
		match = re.search(r'<title>(.*?)</title>', myPage, re.S)
		title = u'无标题'
		if match:
			title = match.group(1)
		else:
			print '无法获取标题'
		#文件名不能包含以下字符： \ / ： * ? " < > |  
		title.replace('\\','').replace('/','').replace(':','').replace('*','').replace('?','').replace('"','').replace('>','').replace('<','').replace('|','')
		return title
		

	def save_data(self, url, title, endPage):
		self.get_data(url, endPage)

		f = open(title+'.txt', 'w')
		f.writelines(self.datas)
		f.close()
		print u'文件已下载完成'
		print u'请按任意键退出'
		raw_input();
	

	def get_data(self, url, endPage):
		url = url + '&pn='
		for i in range(1, endPage + 1):
			print u'爬虫%d正在加载中咔嚓咔嚓....' % i
			myPage = urllib2.urlopen(url + str(i)).read() 
			
			self.deal_data(myPage.decode('utf-8')) 



	def deal_data(self, myPage):
		myItems = re.findall('id="post_content.*?>(.*?)</div>',  myPage, re.S)
		for item in myItems:
			data = self.myTool.replaceChar(item.replace("\n", "").encode('utf-8'))
			self.datas.append(data+'\n')




print u'Here Runs the Program'

print u'input the address here'

bdurl = 'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/'))  

Spider = Lianzai_crawler(bdurl)

Spider.Tb_crawler()
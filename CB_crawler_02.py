# -*- coding: utf-8 -*- 

import urllib2
import urllib
import re
import thread
import time

class Spider:
	
    def __init__(self):
		self.page = 1  # 页码
		self.stories = []  #每一页的段子
		self.enable = False


		#这一段是将所有的文字拿出来，添加到列表中的程序
    def GetPage(self, page):
		try:
			myurl = "http://www.qiushibaike.com/hot/page/" + page
			# here I change the header to Mac OSX
			user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1)'
			header = {'User-Agent' : user_agent}
			req = urllib2.Request(myurl, headers = header)
			Myrespone = urllib2.urlopen(req)
			Mypage = Myrespone.read().decode("utf-8")
			if Mypage:
				print '拿到最初的pageeeeeeee啦~~'
			return Mypage
		
		except urllib2.URLError, e:
			if hasattr(e, "reason"):
				print u"连接糗事百科失败,错误原因", e.reason
				return None
 
		

    def getPageItems(self, page):
    	myPage = self.GetPage(str(page))
    	if not myPage:
    		print "页面加载失败····"
    		return None
    	#patten = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
    	#patten = re.compile('<div class="content">(.*?)<!--(.*?)-->.*?</div>', re.S)
    	patten = re.compile('<div class="author clearfix">.*?<a href=".*?" target=".*?" title="(.*?)"><h2>.*?</h2></a></div>', re.S)
    						

    	items = re.findall(patten, myPage)
    	#这个search这里有问题·东西是空的
    	if items:
    		print 'sth in the items'
    	else:
    		print 'nothing in the items' 
    	
    	pageStory = []

    	for item in items:
    		print item[0], item[1]

    	# for item in items:
    	# 	print item[0], item[1], item[2], item[3], item[4]
    	
    	# for item in items:

    	# 	haveImg = re.search('<img>', item[3])
    	# 	if not haveImg:
    	# 		print "loading"
    	# 		replaceBr = re.compile('<br/>')
    	# 		text = re.sub(replaceBR,"\n",item[1])
    	# 		pageStory.append(item[0].strip(), text.strip(), item[2].strip(), item[4].strip)
    	print "successfully get the page"
    	return pageStory


    def LoadPage(self):
		if self.enable:
			# 如果pages数组中的内容小于2
			if len(self.stories) < 2:
				print"获取新页面中·····"
				#获取新页面
				Mypage = self.getPageItems(str(self.page))
				print Mypage
				if Mypage:
					self.stories.append(Mypage)
					self.page += 1
		print 'end of LoadPage'
				
    
    def getOneStory(self, pageStory, page):
    	for story in pageStory:
    		input = raw_input()
    		self.LoadPage()
    		if input == 'Q':
    			self.enable = False
    			return
    		print u"第%d页\t发布人:%s\t发布时间:%s\t赞:%s\n%s" %(page,story[0],story[2],story[3],story[1])

    def Start(self):
		self.enable = True
		self.LoadPage()
		nowPage = 0

		print self.enable

		while self.enable:
			# print len(self.stories)
			if len(self.stories)>0:
				print '#从全局list中获取一页的段子'
				pageStories = self.stories[0]
				print' #当前读到的页数加一'
				nowPage += 1
                #将全局list中第一个元素删除，因为已经取出
				del self.stories[0]
                #输出该页的段子
				self.getOneStory(pageStories,nowPage)


myModel = Spider()    
myModel.Start()    


		
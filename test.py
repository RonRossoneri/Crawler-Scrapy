# -*- coding: utf-8 -*- 
import re

str = '''
<div class="article block untagged mb15" id="qiushi_tag_114462119">
<div class="author clearfix">
<a href="/users/28769298" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/2876/28769298/medium/20150602224225.jpg" alt="娄子哥">
</a>
<a href="/users/28769298" target="_blank" title="娄子哥">
<h2>娄子哥</h2>
</a>
</div>
<div class="content">
听我战友讲的真实糗事:多年前他作为犯罪嫌疑人被关进了局子，一次提审时，他为了和警察套近乎，说自己是特警兵。从那天起，里面给了他特殊照顾，晚上为他增加了脚镣，怕他脱逃。
<!--1451371744-->
</div>
<div class="stats">
<span class="stats-vote"><i class="number">13323</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/114462119" data-share="/article/114462119" id="c-114462119" class="qiushi_comments" target="_blank">
<i class="number">81</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_114462119" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-114462119" class="up">
<a href="javascript:voting(114462119,1)" class="voting" data-article="114462119" id="up-114462119" rel="nofollow">
<i class="iconfont" data-icon-actived="󰁡" data-icon-original="󰀟">󰀟</i>
<span class="number hidden">13640</span>
</a>
</li>
<li id="vote-dn-114462119" class="down">
<a href="javascript:voting(114462119,-1)" class="voting" data-article="114462119" id="dn-114462119" rel="nofollow">
<i class="iconfont" data-icon-actived="󰀠" data-icon-original="󰀠">󰀠</i>
<span class="number hidden">-317</span>
</a>
</li>
<li class="comments">
<a href="/article/114462119" id="c-114462119" class="qiushi_comments" target="_blank">
<i class="iconfont" data-icon-actived="󰁢" data-icon-original="󰀝">󰀝</i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<!-- JiaThis Button BEGIN -->
<div class="jiathis_style">
<span class="jiathis_txt">分享到：</span>
<a href="###" class="jiathis_button_weixin" rel="external nofollow" title="分享到微信"><span class="jiathis_txt jtico jtico_weixin"></span></a>
<a href="###" class="jiathis_button_cqq" rel="external nofollow" title="分享到QQ好友"><span class="jiathis_txt jtico jtico_cqq"></span></a>
<a href="###" class="jiathis_button_qzone" rel="external nofollow" title="分享到QQ空间"><span class="jiathis_txt jtico jtico_qzone"></span></a>
<a href="###" class="jiathis_button_tsina" rel="external nofollow" title="分享到新浪微博"><span class="jiathis_txt jtico jtico_tsina"></span></a>
<a href="###" class="jiathis_button_tieba" rel="external nofollow" title="分享到百度贴吧"><span class="jiathis_txt jtico jtico_tieba"></span></a>
<a href="http://www.jiathis.com/share" class="jiathis jiathis_txt jtico jtico_jiathis" target="_blank" rel="external nofollow"></a>
</div>
<!-- JiaThis Button END -->
</div>
<div class="single-clear"></div>
</div>





<div class="article block untagged mb15" id="qiushi_tag_114459534">
<div class="author clearfix">
<a href="/users/26781942" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/2678/26781942/medium/20150409111518.jpg" alt="城市猎人……">
</a>
<a href="/users/26781942" target="_blank" title="城市猎人……">
<h2>城市猎人……</h2>
</a>
</div>


<div class="content">

今天看见我初中时的同学，我问他晚上怎么不出来玩了？他说在家辅导刚上学的儿子，听了之后，我的心理五味陈杂，他上学时考的最好的一次是倒数第三
<!--1451342253-->

</div>



<div class="stats">
<span class="stats-vote"><i class="number">13569</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/114459534" data-share="/article/114459534" id="c-114459534" class="qiushi_comments" target="_blank">
<i class="number">122</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_114459534" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-114459534" class="up">
<a href="javascript:voting(114459534,1)" class="voting" data-article="114459534" id="up-114459534" rel="nofollow">
<i class="iconfont" data-icon-actived="󰁡" data-icon-original="󰀟">󰀟</i>
<span class="number hidden">13925</span>
</a>
</li>
<li id="vote-dn-114459534" class="down">
<a href="javascript:voting(114459534,-1)" class="voting" data-article="114459534" id="dn-114459534" rel="nofollow">
<i class="iconfont" data-icon-actived="󰀠" data-icon-original="󰀠">󰀠</i>
<span class="number hidden">-356</span>
</a>
</li>

<li class="comments">
<a href="/article/114459534" id="c-114459534" class="qiushi_comments" target="_blank">
<i class="iconfont" data-icon-actived="󰁢" data-icon-original="󰀝">󰀝</i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<!-- JiaThis Button BEGIN -->
<div class="jiathis_style">
<span class="jiathis_txt">分享到：</span>
<a href="###" class="jiathis_button_weixin" rel="external nofollow" title="分享到微信"><span class="jiathis_txt jtico jtico_weixin"></span></a>
<a href="###" class="jiathis_button_cqq" rel="external nofollow" title="分享到QQ好友"><span class="jiathis_txt jtico jtico_cqq"></span></a>
<a href="###" class="jiathis_button_qzone" rel="external nofollow" title="分享到QQ空间"><span class="jiathis_txt jtico jtico_qzone"></span></a>
<a href="###" class="jiathis_button_tsina" rel="external nofollow" title="分享到新浪微博"><span class="jiathis_txt jtico jtico_tsina"></span></a>
<a href="###" class="jiathis_button_tieba" rel="external nofollow" title="分享到百度贴吧"><span class="jiathis_txt jtico jtico_tieba"></span></a>
<a href="http://www.jiathis.com/share" class="jiathis jiathis_txt jtico jtico_jiathis" target="_blank" rel="external nofollow"></a>
</div>
<!-- JiaThis Button END -->
</div>
<div class="single-clear"></div>
</div>
'''


def finda(str):
	pat = re.compile('<h2>(.*?)</h2>.*?<div class="content">(.*?)<!--.*?-->.*?</div>.*?<span class="stats-vote"><i class="number">(.*?)</i>.*?<i class="number">(.*?)</i>', re.S)
	items = re.findall(pat, str)
	if items:
		for item in items:
			for i in item:
				print i
	else:
		print "no match for findall"
def find(str):
	#pat = re.compile(r'<h2>(.*?)</h2>')
	pat = re.compile('<h2>(.*?)</h2>.*?<div class="content">(.*?)<!--.*?-->.*?</div>.*?<span class="stats-vote"><i class="number">(.*?)</i>.*?<i class="number">(.*?)</i>', re.S)
	res = pat.search(str)
	if res:
		print res.group(1)
		print res.group(2)
		print res.group(3)
		print res.group(4)
		print res.group(1)
	else:
		print "no match for FIND"

#finda('<div.*?author">.*?<a.*?<img.*?><a.*?><h2>(.*?)</h2></a>.*?<div.*?content">(.*?)<!--(.*?)-->.*?</div><div class="stats.*?class="number">(.*?)</i>' ,str)
#finda('<a.*?title="(.*?)"><h2>', '<a href="/users/28769298" target="_blank" title="娄子哥"><h2>')
str1 = '''
<a href="/users/28769298" target="_blank" title="娄子哥">
<h2>娄子哥</h2>
</a>
</div>
<div class="content">
听我战友讲的真实糗事:多年前他作为犯罪嫌疑人被关进了局子，一次提审时，他为了和警察套近乎，说自己是特警兵。从那天起，里面给了他特殊照顾，晚上为他增加了脚镣，怕他脱逃。
<!--1451371744-->
</div>
<div class="stats">
<span class="stats-vote"><i class="number">13323</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/114462119" data-share="/article/114462119" id="c-114462119" class="qiushi_comments" target="_blank">
<i class="number">81</i> 评论
</a>
'''

finda(str)







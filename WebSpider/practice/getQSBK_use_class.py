#!/usr/bin/env python
# coding=utf-8
import urllib
import urllib2
import re
import thread
import time

#糗事百科爬虫类
class QSBK:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.stories =[]
        self.enable = False

    def getPage(self, pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            request = urllib2.Request(url, headers= self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print u"连接糗事百科失败，错误原因", e.reason
                return None

    def getPageItems(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "page load failed...."
            return None
        pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?</div>.*?'\
                            '<div.*?class="content".*?>(.*?)<!--(.*?)-->.*?</div>.*?'\
                            '<div.*?class="stats".*?class="number">(.*?)</i>',re.S)
        items = re.findall(pattern, pageCode)
        pageStories = []
        for item in items:
            pageStories.append([item[0].strip(),item[1].strip(),item[2].strip(),item[3].strip()])
        return pageStories

    def loadPage(self):
        if self.enable == True:
            if len(self.stories) <2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex+=1
    
    def getOneStory(self, pageStories, page):
        for story in pageStories:
            input = raw_input()
            self.loadPage()
            if input == 'Q':
                self.enable = False
                return
            print u"第%d页\t发布人:%s\t发布时间:%s\n%s\n赞:%s\n" %( page, story[0], story[2], story[1], story[3] )

    def start(self):
        print u"正在读取糗事百科,按回车查看新段子，Q退出"
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                pageStories = self.stories[0]
                nowPage+=1
                del self.stories[0]
                self.getOneStory(pageStories, nowPage)

if __name__ == "__main__":
    spider = QSBK()
    spider.start()
    '''
    第1页   发布人:脱裤子耍流氓-    发布时间:2015-06-10 17:06:52
    一代宗师林正英，<br/>糗友们是否看过他的电影长大的，长大之后才发现他已去世。<br/>为他点满10万个赞。
    赞:15871

    第1页   发布人:发红包发红包 发布时间:2015-06-10 15:02:11
    连续下了几天的大雨，回家路上看见这一幕，果断拍下，大雨也阻挡不了多篮球的热爱
    赞:2303

    第1页   发布人:难是真字名个起我 发布时间:2015-06-10 17:46:28
    一个轮胎就下河抓鱼了，就现在就在面前，太有才了！小时候买不起泳圈那会多期盼能有个轮胎玩，有过同样想法的举手吧！
    赞:1905


    第1页   发布人:当年的包子头 发布时间:2015-06-10 14:44:58
    每次苍蝇在交配的时候最容易被拍死<br/>这就叫“秀恩爱，死的快！”
    赞:1459


    第1页   发布人:水翼ｓ   发布时间:2015-06-10 17:30:01
    今天朋友来微信说没钱吃饭了，我给他卡打了1000，就刚刚来电话说让我去他家拿果6，还说一共发了18个人，就2个给打钱了。他家刚拆迁完今天钱到账了。麻痹这种兄弟真有才！
    赞:13169
    '''

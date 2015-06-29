__author__ = 'ntkodev'
#coding=utf-8


import urllib
import urllib2
import re

class Utill(object):
    removeImg = re.compile('<img.*?>| {7}|')
    removeAddr = re.compile('<a.*?>|</a>')
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    replaceTab = re.compile('<td>')
    replacePara = re.compile('<p.*?>')
    replaceBr = re.compile('<br><br>|<br>')
    removeExtraTag = re.compile('<.*?>')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTab, "\t",x)
        x = re.sub(self.replacePara, "\n   ", x)
        x = re.sub(self.replaceBr, '\n', x)
        x = re.sub(self.removeExtraTag, "", x)
        return x.strip()

class BDTB(object):
    def __init__(self, baseURL, seeLZ, floorTag):
        self.baseURL = baseURL
        self.seeLZ = '?see_lz='+str(bool(seeLZ))
        self.utill = Utill()
        self.file = None
        self.floor = 1
        self.defaultTitle = "baudutieba"

        self.floorTag = floorTag

    def getPage(self, pageNum):
        try:
            url = self.baseURL + self.seeLZ+'&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            #print response.read()
            return response
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print 'failed:', e.reason
                return None

    def getTitle(self, page):
        patt = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>', re.S)
        result = re.search(patt, page)
        if result:
            return result.group(1).strip()
        else:
            return None

    def getPageNum(self, page):
        patt = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(patt, page)
        if result:
            return result.group(1).strip()
        else:
            return None

    def getContent(self, page):
        patt = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(patt, page)
        contents=[]
        for item in items:
            content = "\n"+self.utill.replace(item)+"\n"
            contents.append(content.decode('utf-8'))
        return contents

    def setFileTitle(self,title):
        if title is not None:
            self.file = open(title + ".txt","w+")
        else:
            self.file = open(self.defaultTitle + ".txt","w+")


    def writeData(self,contents):
        for item in contents:
            if self.floorTag == '1':
                floorLine = "\n" + str(self.floor) + u"-----------------------------------------------------------------------------------------\n"
                self.file.write(floorLine)
            self.file.write(item)
            self.floor += 1

    def start(self):
        indexPage = self.getPage(1).read()
        pageNum = self.getPageNum(indexPage)
        title = self.getTitle(indexPage)
        self.setFileTitle(title)
        if pageNum == None:
            print "URL failed"
            return
        try:
            print "all " + str(pageNum) + "pages"
            for i in range(1,int(pageNum)+1):
                print "writing now" + str(i) + "page's data"
                page = self.getPage(i)
                contents = self.getContent(page)
                self.writeData(contents)

        except IOError,e:
            print "Reason: " + e.message
        finally:
            print "finished"

if __name__ == '__main__':
    baseURL = 'http://tieba.baidu.com/p/3138733512'
    bdtb = BDTB(baseURL, True, 1)
    bdtb.start()
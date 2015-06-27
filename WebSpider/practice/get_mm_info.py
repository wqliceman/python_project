# -*- coding: utf-8 -*-
__author__ = 'wqliceman'

import urllib
import urllib2
import re
import os


__author__ = 'CQC'
#-*- coding:utf-8 -*-
import re

#处理页面标签类
class Tool:
    #去除img标签,1-7位空格,&nbsp;
    removeImg = re.compile('<img.*?>| {1,7}|&nbsp;')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    #将多行空行删除
    removeNoneLine = re.compile('\n+')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        x = re.sub(self.removeNoneLine,"\n",x)
        #strip()将前后多余内容删除
        return x.strip()


class CMMInfo(object):
    def __init__(self):
        self.sitURL = 'http://mm.taobao.com/json/request_top_list.htm'
        self.tool = Tool()

    def getPage(self, pageNum):
        url = self.sitURL + "?page="+str(pageNum)
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('gbk')

    def getContents(self, pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>', re.S)
        items = re.findall(pattern, page)
        contents =[]
        for item in items:
            contents.append([item[0],item[1], item[2], item[3], item[4]])
        return contents

    def getDetailPage(self, infoUrl):
        response = urllib2.urlopen(infoUrl)
        return response.read().decode('gbk')

    def getInfomation(self, page):
        pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
        result = re.search(pattern, page)
        return self.tool.replace(result.group(1))

    def getAllimag(self, page):
        pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
        content = re.search(pattern, page)
        patImg = re.compile('<img.*?src="(.*?)"', re.S)
        images = re.findall(patImg, content.group(1))
        return  images

    def saveImages(self, images, name):
        number = 1
        for imageUrl in images:
            splitpath = imageUrl.split('.')
            fTail = splitpath.pop()
            fileName = name+'/'+str(number)+'.'+fTail
            self.saveImg(imageUrl, fileName)
            number+=1

    def saveIcon(self, iconURL, name):
        splitPath = iconURL.split('.')
        fTail = splitPath.pop()
        fileName = name+'/icon.'+ fTail
        self.saveImg(iconURL, fileName)

    def saveInfomation(self, content, name):
        filename = name+'/'+name+'.txt'
        f = open(filename, 'w+')
        f.write(content.encode('utf-8'))
        f.close()

    def saveImg(self, imageURL, fileName):
        u = urllib.urlopen(imageURL)
        f = open(fileName, 'wb')
        f.write(u.read())
        f.close()

    def mkdir(self, path):
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
        else:
            return False

    def savePageInfo(self, pageIndex):
        contents = self.getContents(pageIndex)
        for item in contents:
            print u"发现一位模特,名字叫",item[2],u"芳龄",item[3],u",她在",item[4]
            detailUrl = 'http:'+ item[0]
            print detailUrl
            detailPage = self.getDetailPage(detailUrl)
            information = self.getInfomation(detailPage)
            images = self.getAllimag(detailPage)
            self.mkdir(item[2])
            self.saveInfomation(information, item[2])
            self.saveIcon('http:'+item[1], item[2])
            self.saveImages(images, item[2])


    def savePagesInfo(self, start, end):
        for i in range(start, end+1):
            self.savePageInfo(i)


if __name__ == '__main__':
    mmInfo = CMMInfo()
    mmInfo.savePagesInfo(5, 10)
# -*- coding: utf-8 -*-
__author__ = 'wqliceman'

import urllib
import urllib2
import re
import cookielib
import webbrowser
import json
import xlwt
import sys
import  os
import math
import random

#1. get login capcha url

#2. get login capcha images

#3. login

#4. goto account pages


class CDianpingOrder:
    def __init__(self, owner, username, password):
        self.loginURL = "http://t.dianping.com/login?redirect=/account/coupons"
        self.host = "http://t.dianping.com"
        self.loginAjax = "http://t.dianping.com/ajax/wwwaccount/logint"
        #退款URL
        self.refundURL=self.host + "/receipt/refund/"

        self.UserAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"

        self.owner = owner
        self.username = username
        self.password = password
        self.capcha = ""
        self.save_rows = 0
        self.workbook = xlwt.Workbook(encoding='utf-8')
        self.worksheet = self.workbook.add_sheet('点评订单')

        self.Cookie = 'ctu=5687191ae9b782fbe7ca4fe79751249a6e32c84e463d95e1a78578d94a11057de8ae6f03850af2dcc8e7cb93acf6299c; _tr.u=iTU5BfYgBCLl2c0L; _hc.v="\\"6f018ca8-ccff-45f4-9fc7-a014f3133a8c.1437790955\\""; ctu=8abaa8148fbc3603e4050d4c8d3847789e483fdb7eb4cfcb368b1f015ee6f936; PHOENIX_ID=0a017715-14ec4373426-7b77b; ua=13883614086; lln=13883614086; ctu=5687191ae9b782fbe7ca4fe79751249a6e32c84e463d95e1a78578d94a11057d8043e7356a5cf261db9383a19a3f5c96; _tr.s=VAZxRZMWeQL6FLmn; cy=9; cye=chongqing; JSESSIONID=69661B4EB010A5B57A0ECF5E1EB8D70B'

        self.postHerder = {
            "Host": "t.dianping.com",
            "Connection": "keep-alive",
            "Origin": "http://t.dianping.com",
            "X-Request": "JSON",
            "User-Agent": self.UserAgent,
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8;",
            "Accept": "application/json, text/javascript",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "http://t.dianping.com/login?redirect=/account/coupons",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
            "Cookie": self.Cookie
        }

        #cookie
        cookie = cookielib.CookieJar()
        cookie_handler = urllib2.HTTPCookieProcessor(cookie)
        self.opener = urllib2.build_opener(cookie_handler, urllib2.HTTPHandler)
        urllib2.install_opener(self.opener)

    def getCapchaUrl(self):
        post_header = {
            "Host": "t.dianping.com",
            "Connection": "keep-alive",
            "User-Agent": self.UserAgent
        }
        request = urllib2.Request(url=self.loginURL, headers=post_header)

        response = self.opener.open(request)
        content = response.read()
        status = response.getcode()
        if status == 200:
            print "获取请求成功"
            pattern = re.compile('<img id="mcImgVC" src=\'(.*?)\'', re.S)
            matchResult = re.search(pattern, content)
            if matchResult and matchResult.group(1):
                print matchResult.group(1)
                return self.host+matchResult.group(1)
            else:
                return False

        else:
            return False

    def doSomethingBeforegetCapcha(self):
        getURL = "http://t.dianping.com/ajax/wwwaccount/captcha/2"
        post_header = {
            "Host": "t.dianping.com",
            "Connection": "keep-alive",
            "User-Agent": self.UserAgent,
            "Accept": "application/json, text/javascript",
            "X-Requested-With": "XMLHttpRequest",
            "X-Request": "JSON",
            "Referer": "http://t.dianping.com/login?redirect=/account/coupons"
        }
        request = urllib2.Request(url=getURL, headers=post_header)

        response = self.opener.open(request)
        status = response.getcode()
        if status == 200:
            print "获取请求成功before get capcha"

    def getCapchaImage(self, capchaURL):
        request = urllib2.Request(capchaURL)
        request.add_header("Host", "t.dianping.com")
        request.add_header("Connection", "keep-alive")
        request.add_header("User-Agent", self.UserAgent)
        request.add_header("Referer", "http://t.dianping.com/login?redirect=/account/coupons"),
        request.add_header("Cookie", self.Cookie)

        response = self.opener.open(request)
        content = response.read()
        status = response.getcode()
        if status == 200:
            image = open(".\capcha\capcha.png", 'wb')
            image.write(content)
            image.close()
            return  True
        else:
            return  False

    def beginLogin(self):
        post = {
            'username': self.username,
            'password': self.password,
            'vcode': self.capcha,
            'keepLogin': 'true',
            'capcha': self.capcha
        }
        postData = "username=%s&password=%s&vcode=%s&keepLogin=true&capcha=%s"\
                  % (self.username, self.password, self.capcha, self.capcha)
        #postData = urllib.urlencode(post)
        print postData
        request = urllib2.Request(self.loginAjax, postData, self.postHerder)
        response = urllib2.urlopen(request)
        content = response.read()
        status = response.getcode()
        if status == 200:
            encodeJson = json.dumps(eval(content), sort_keys=False)
            decodeJson = json.loads(encodeJson)
            if decodeJson['code'] == 200:
                request = urllib2.Request("http://t.dianping.com/account/coupons")
                request.add_header("Host", "t.dianping.com")
                request.add_header("Connection", "keep-alive")
                request.add_header("User-Agent", self.UserAgent)
                request.add_header("Referer", "http://t.dianping.com/login?redirect=/account/coupons")

                response = self.opener.open(request)
                content = response.read()
                status = response.getcode()
                if status == 200:
                    return content
            else:
                print content.decode('utf-8').encode('utf-8')
                return False
        else:
            return  False

    def getPageNumbers(self, page):
        #首先查找是否存在多页
        page_num = 1
        pattern = re.compile('<div class="pages-wrap">(.*?)</div>', re.S)
        result = re.search(pattern, page)
        if result and result.group(1):
            content = result.group(1).strip().replace('\n', '')
            if len(content) == 0:
                return  page_num
            else:
                #改程序登录，存在多页时，默认选择第一页，故只需要查找其他页码的最大值即可
                pattern = re.compile('data-pg="(.*?)"', re.S)
                result = re.findall(pattern, content)
                if result:
                    for item in result:
                        if page_num < int(item):
                            page_num = int(item)
                else:
                    return  page_num

        return page_num

    def getOrderPageInfo(self, page_num):
        print '开始获取页面'
        request = urllib2.Request("http://t.dianping.com/account/coupons" + "?pageno=" + str(page_num))
        request.add_header("Host", "t.dianping.com")
        request.add_header("Connection", "keep-alive")
        request.add_header("User-Agent", self.UserAgent)
        request.add_header("Referer", "http://t.dianping.com/account/coupons")

        response = self.opener.open(request)
        content = response.read()
        status = response.getcode()
        if status == 200:
            print '获取页面成功'
            return content
        else:
            return False

    def getOrders(self, page):
        #依次为：团购ID，团购名称，团购券号，数量，退款单号
        pattern = re.compile('<div class="txt">.*?href="(.*?)".*?target="_blank">(.*?)</a>.*?'
                             '<span class="ing"><b>(.*?)</b>.*?<td class="t-amount">.*?<span>(.*?)</span>'
                             '.*?class="J_refund.*?data-receiptid="(.*?)"', re.S)
        print '开始该页扒订单'
        result = re.findall(pattern, page)
        if self.save_rows == 0:
            self.worksheet.write(0, 0, u"账号")
            self.worksheet.write(0, 1, u"名称")
            self.worksheet.write(0, 2, u"券号")
            self.worksheet.write(0, 3, u"数量")
            self.worksheet.write(0, 4, u"原始价格")
            self.worksheet.write(0, 5, u"购买价格")
            self.worksheet.write(0, 6, u"立减差价")
            self.save_rows += 1
            print "写入头成功"

        for item in result:
            # saveStr = "名称: "+item[1].strip().replace('\n',' ').replace(' ','')+"\t券号: "+item[2].strip()+"\t数量: "+item[3].strip()\
            #           +'\t原始价格: '+self.getGoodsOriginPrice(item[0].strip()) \
            #           +'\t购买价格: '+ self.getRealPayPrice(item[4].strip())[1]+os.linesep
            #print str(saveStr).decode('utf-8').encode('utf-8')
            self.worksheet.write(self.save_rows, 0, self.username)
            name = str(item[1].strip().replace('\n', ' ').replace(' ', ''))
            print name
            self.worksheet.write(self.save_rows, 1, name)
            ticket_num = item[2].strip()
            self.worksheet.write(self.save_rows, 2, ticket_num)
            count = int(item[3].strip())
            self.worksheet.write(self.save_rows, 3, count)

            order_price = float(self.getGoodsOriginPrice(item[0].strip()))
            self.worksheet.write(self.save_rows, 4, order_price)

            real_price = float(self.getRealPayPrice(item[4].strip())[1])
            self.worksheet.write(self.save_rows, 5, real_price)

            self.worksheet.write(self.save_rows, 6, (order_price - real_price))
            self.save_rows += 1

    #获取商品原始价格
    def getGoodsOriginPrice(self, goodsID):
        request = urllib2.Request(self.host+goodsID)
        request.add_header("Host", "t.dianping.com")
        request.add_header("Connection", "keep-alive")
        request.add_header("User-Agent", self.UserAgent)
        request.add_header("Referer", "http://t.dianping.com/login?redirect=/account/coupons")

        response = self.opener.open(request)
        content = response.read()
        status = response.getcode()
        if status == 200:
            pattern = re.compile('class="price-wrap">.*?class="price-display">.*?</em>(.*?)</span>', re.S)
            result = re.search(pattern, content)
            if result and result.group(1):
                return result.group(1).strip()
        else:
            return False


    #获取商品实际付款价格
    def getRealPayPrice(self, reundID):
        request = urllib2.Request(self.refundURL + reundID)
        request.add_header("Host", "t.dianping.com")
        request.add_header("Connection", "keep-alive")
        request.add_header("User-Agent", self.UserAgent)
        request.add_header("Referer", "http://t.dianping.com/login?redirect=/account/coupons")

        response = self.opener.open(request)
        content = response.read()
        status = response.getcode()
        if status == 200:
            pattern = re.compile('<div class="box-wrap">.*?align="center">(.*?)</td>.*?Price-font Price-sc">(.*?)</div>', re.S)
            result = re.search(pattern, content)
            if result:
                return [result.group(1).strip(), result.group(2).strip()]
        else:
            return False

    def main(self):
        retValue = False

        save_filename = './' + self.owner + '/' + self.username + '.xls'
        if os.path.exists(save_filename):
            print save_filename.decode('gbk').encode('utf-8') + "存在"
            return True

        capchaUrl = "http://t.dianping.com/account/tuan.jpg?xx=" + str(int(math.floor(random.random()*1001)))  #self.getCapchaUrl()
        #self.doSomethingBeforegetCapcha()
        if capchaUrl:
            while self.getCapchaImage(capchaUrl):
                webbrowser.open_new_tab(".\capcha\capcha.png")
                self.capcha = raw_input("输入看到的验证码：")
                retPage = self.beginLogin()
                if retPage:
                    retValue = True
                    break
            if retValue:
                print "登录成功"
                page_total = self.getPageNumbers(retPage)
                print page_total
                page = 1
                while page <= page_total:
                    print u"Get page: " + str(page)
                    self.getOrders(self.getOrderPageInfo(page))
                    page += 1
                self.workbook.save(save_filename)
            else:
                print "登录失败"
        else:
            print "获取验证码地址错误"


if __name__ == '__main__':
    # 创建文件夹
    path = os.getcwd()                       # 获取此脚本所在目录
    new_path = os.path.join(path, u'capcha')
    if not os.path.isdir(new_path):
        os.mkdir(new_path)
    for dirpath, dirnames, filenames in os.walk('./owner'):
        #获取每个用户
        for item in filenames:
            owner = os.path.splitext(item)[0]
            new_path = os.path.join(path, owner)
            if not os.path.isdir(new_path):
                os.mkdir(new_path)
            #获取用户购买账号
            print item.decode('gbk').encode('utf-8')
            info = open(dirpath + os.sep + item, 'r')
            lines = info.readlines()
            for line in lines:
                account = line.replace('\n','').split('\t')
                username = account[0]
                password = account[1]
                dianping = CDianpingOrder(owner, username, password)
                dianping.main()

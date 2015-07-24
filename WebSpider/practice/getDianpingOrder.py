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

#1. get login capcha url

#2. get login capcha images

#3. login

#4. goto account pages

class CDianpingOrder:
    def __init__(self, username, password):
        self.loginURL = "http://t.dianping.com/login?redirect=/account/coupons"
        self.host = "http://t.dianping.com"
        self.loginAjax = "http://t.dianping.com/ajax/wwwaccount/logint"
        #退款URL
        self.refundURL=self.host + "/receipt/refund/"

        self.UserAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"

        self.username = username
        self.password = password
        self.capcha = ""

        self.postHerder = {
            "Host": "t.dianping.com",
            "Origin": "http://t.dianping.com",
            "X-Request": "JSON",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8;",
            "Connection": "Keep-Alive",
            "Accept": "application/json, text/javascript",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": self.UserAgent,
            "Pragma": "no-cache",
            "Referer": "http://t.dianping.com/login?redirect=/account/coupons"
        }

        #cookie
        cookie = cookielib.LWPCookieJar()
        cookie_handler = urllib2.HTTPCookieProcessor(cookie)
        self.opener = urllib2.build_opener(cookie_handler, urllib2.HTTPHandler)
        urllib2.install_opener(self.opener)

    def getCapchaUrl(self):
        postHeader = {
            "Host": "t.dianping.com",
            "Connection": "keep-alive",
            "User-Agent": self.UserAgent
        }
        request = urllib2.Request(url=self.loginURL, headers=postHeader)
        # request.add_header("Host", "t.dianping.com")
        # request.add_header("User-Agent", self.UserAgent)
        # request.add_header("Connection", "keep-alive")

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

    def getCapchaImage(self, capchaURL):
        request = urllib2.Request(capchaURL)
        request.add_header("Host", "t.dianping.com")
        request.add_header("Connection", "keep-alive")
        request.add_header("User-Agent", self.UserAgent)
        request.add_header("Referer", "http://t.dianping.com/login?redirect=/account/coupons")

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
        postData = urllib.urlencode(post)
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
                print decodeJson
                return False
        else:
            return  False

    def getOrders(self, page):
        #依次为：团购ID，团购名称，团购券号，数量，退款单号
        pattern = re.compile('<div class="txt">.*?href="(.*?)".*?target="_blank">(.*?)</a>.*?'
                             '<span class="ing"><b>(.*?)</b>.*?<td class="t-amount">.*?<span>(.*?)</span>'
                             '.*?data-receiptid="(.*?)"', re.S)
        result = re.findall(pattern, page)

        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('点评订单')
        rows = 0

        for item in result:
            saveStr = "名称: "+item[1].strip().replace('\n',' ').replace(' ','')+"\t券号: "+item[2].strip()+"\t数量: "+item[3].strip()\
                      +'\t原始价格: '+self.getGoodsOriginPrice(item[0].strip()) \
                      +'\t购买价格: '+ self.getRealPayPrice(item[4].strip())[1]+os.linesep
            print str(saveStr).decode('utf-8').encode('utf-8')
            col = 0
            for val in item:
                worksheet.write(rows, col, val)
                col+=1
            rows+=1
        workbook.save(self.username+'.xls')

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
        request = urllib2.Request(self.refundURL+reundID)
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
        capchaUrl = self.getCapchaUrl()
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
                self.getOrders(retPage)
            else:
                print "登录失败"
        else:
            print "获取验证码地址错误"


if __name__ == '__main__':

    dianping = CDianpingOrder("13883614086", "wangqiulin1989")
    dianping.main()


'''
    #
    def getPageNum(self, page):


    def getOrderPages(self, pageNum):
        return onePage


'''
# -*- coding: utf-8 -*-
__author__ = 'wqliceman'


import requests


post_header = {
            "Host": "t.dianping.com",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
        }
x = requests.session()
x.get('http://t.dianping.com/login?redirect=/account/coupons', headers=post_header)
#print x.cookies

loginAjax = "http://t.dianping.com/ajax/wwwaccount/logint"
postHerder = {
            "Host": "t.dianping.com",
            "Origin": "http://t.dianping.com",
            "X-Request": "JSON",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8;",
            "Connection": "Keep-Alive",
            "Accept": "application/json, text/javascript",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
            "Pragma": "no-cache",
            "Referer": "http://t.dianping.com/login?redirect=/account/coupons",
            "Cookie": '_tr.u=iTU5BfYgBCLl2c0L; _hc.v="\\"6f018ca8-ccff-45f4-9fc7-a014f3133a8c.1437790955\\""; ctu=8abaa8148fbc3603e4050d4c8d3847789e483fdb7eb4cfcb368b1f015ee6f936; PHOENIX_ID=0a017715-14ec4373426-7b77b; ua=13883614086; lln=13883614086; ctu=5687191ae9b782fbe7ca4fe79751249a6e32c84e463d95e1a78578d94a11057d8043e7356a5cf261db9383a19a3f5c96; _tr.s=VAZxRZMWeQL6FLmn; cy=9; cye=chongqing; JSESSIONID=F9EA3A5E48F3AA80E3912DE6F7B001ED'

        }
postData = "username=%s&password=%s&vcode=%s&keepLogin=true&capcha=%s" % ("13883614086", "wangqiulin1989", "fsdf", "fsdf")
x2 = x.post(url=loginAjax, data=postData, headers=postHerder)
print x2.content
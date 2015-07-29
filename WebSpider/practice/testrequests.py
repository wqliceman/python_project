# -*- coding: utf-8 -*-
__author__ = 'wqliceman'


import requests
from PIL import Image
from StringIO import StringIO
import math
import random


# r = requests.get('http://t3.s2.dpfile.com/t/res/favicon.5ff777c11d7833e57e01c9d192b7e427.ico')
# i = Image.open(StringIO(r.content))
# print i.show()
# f = open('test.ico', 'wb')
# #f.write(i)
# f.close()

loginURL = "http://t.dianping.com/login?redirect=/account/coupons"
UserAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
capchaUrl = "http://t.dianping.com/account/tuan.jpg?xx=" + str(int(math.floor(random.random() * 1001)))

post_header = {
            "Host": "t.dianping.com",
            "Connection": "keep-alive",
            "User-Agent": UserAgent,
            "Referer": "http://t.dianping.com/login?redirect=/account/coupons"
        }

# r = requests.get(loginURL, headers=post_header)
# print r.headers
# print r.cookies
#
# r2 = requests.get(capchaUrl, headers=post_header)
# print r2.cookies

s = requests.session()
r = s.get(loginURL, headers=post_header)
print r.cookies
r2 = s.get(capchaUrl, headers=post_header)
print r2.cookies


#test requests post
# url = 'http://httpbin.org/post'
# files = {'file': open('test.html', 'rb')}
# r = requests.post(url, files=files)
# print r.cookies['httpbin.org']
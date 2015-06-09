#!/usr/bin/env python
# coding=utf-8
import urllib2
import cookielib
import urllib
from bs4 import BeautifulSoup

filename = "cookie.txt"
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

loginurl="http://passport.csdn.net/account/login"
request = urllib2.Request(loginurl)
result = urllib2.urlopen(request)
soup = BeautifulSoup(result)
inputs = soup.find_all('input')
#print inputs
lt_value = inputs[3]['value']
execution_value = inputs[4]['value']
#print soup.form
print lt_value
print execution_value
postdata = urllib.urlencode({
    "username":"wangqiulin123456",
    "password":"wqliceman123456",
    "lt":lt_value,
    "execution":execution_value,
    '_eventId':'submit'
})
print postdata
result = opener.open(loginurl, postdata)
print result.read()
cookie.save(ignore_discard=True, ignore_expires=True)
blogurl = "http://blog.csdn.net/wangqiulin123456/article/details/17258647"
result = opener.open(blogurl)
print result.read()

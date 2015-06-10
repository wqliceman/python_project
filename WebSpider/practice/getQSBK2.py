#!/usr/bin/env python
# coding=utf-8
import urllib
import urllib2
import re

page=1
url = 'http://www.qiushibaike.com/hot/page/'+str(page)
user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36'
headers = {'User-Agent': user_agent}
try:
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    print '-----get conten------'
    pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?</div>.*?'\
                        '<div.*?class="content".*?>(.*?)<!--(.*?)-->.*?</div>.*?'\
                        '<div.*?class="stats".*?class="number">(.*?)</i>',re.S)
    items = re.findall(pattern, content)
    print '-------get items count:'+str(len(items))+"-----"
    for item in items:
        print 'user:'+item[0],'content:'+item[1], item[2], 'stats:'+item[3]
except urllib2.URLError, e:
    if hasattr(e, 'code'):
        print e.code
    if hasattr(e, 'reason'):
        print e.reason


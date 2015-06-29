# -*- coding: utf-8 -*-
__author__ = 'wqliceman'

import urllib

url = "http://www.baidu.com"

response = urllib.urlopen(url)

print response.geturl()
print response.getcode()
print response.read()

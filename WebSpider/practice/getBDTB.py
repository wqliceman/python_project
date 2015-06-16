__author__ = 'ntkodev'

import urllib
import urllib2
import re

class BDTB(object):
    def __init__(self, baseURL, seeLZ):
        self.baseURL = baseURL
        self.seeLZ = '?see_lz='+str(bool(seeLZ))

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

    def getTitle(self):
        page = self.getPage(1)
        patt = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>', re.S)
        result = re.search(patt, page.read())
        if result:
            print result.group(1).strip()
            return result.group(1).strip()
        else:
            return None

if __name__ == '__main__':
    baseURL = 'http://tieba.baidu.com/p/3138733512'
    bdtb = BDTB(baseURL, True)
   # bdtb.getPage(1)
    bdtb.getTitle()

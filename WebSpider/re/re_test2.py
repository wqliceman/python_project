__author__ = 'wqliceman'

import re

m = re.match('[a-z]ce', 'Icenice')
if m is not None:
    print m.group()
else:
    print "match None"

m = re.search('[a-z]ce', 'icenice')
if m is not None:
    print m.group()
else:
    print "search None"

patt = '\w+@(\w+.)*\w+.com'
print re.match(patt,"wqliceamn@gmail.com").group()
print re.match(patt,"wqliceamn@www.gmail.com").group()

m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
if m is not None:
    print m.group()
    print m.group(1),m.group(2)
    print m.groups()
else:
    print "None"

patt = '[abc]ar'
m = re.findall(patt, 'carfadfbarrewrwaar')
if m is not None:
    print m
else:
    print "NOne"

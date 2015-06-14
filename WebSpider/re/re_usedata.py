__author__ = 'wqliceman'

import re

file = open('data.txt', 'r')

patt = '^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)'
for line in file.readlines():
    m = re.match(patt, line)
    if m is not None:
        print m.group()
    else:
        print 'The line"'+line+'" hasn\'t match string'
file.close()

print '---'*10
file = open('data.txt', 'r')
'''
for line in file.readlines():
    m = re.search('\d+-\d+-\d+', line)
    if m is not None:
        print m.group()
    else:
        print "None"
'''
for line in file.readlines():
    m = re.search('.*?(\d+-\d+-\d+)', line)
    if m is not None:
        print m.group(1)
    else:
        print "None"
file.close()

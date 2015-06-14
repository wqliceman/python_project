__author__ = 'wqliceman'

from random import randint, choice
from string import lowercase
from sys import maxint
from time import ctime

doms = ('com', 'cn', 'edu', 'net', 'org', 'gov','com.cn')

file = open('data.txt', 'w')

for i in range(randint(5,10)):
    dtime_int = randint(0, maxint)
    dtime_str = ctime(dtime_int)

    shorter = randint(4,7)
    em = ''
    for j in range(shorter):
        em+=choice(lowercase)

    longer = randint(shorter, 12)
    dn = ''
    for j in range(longer):
        dn+=choice(lowercase)

    str = '%s::%s@%s.%s::%d-%d-%d'%(dtime_str, em,dn, choice(doms), dtime_int, shorter, longer)
    print str
    file.write(str+"\n")

file.close()


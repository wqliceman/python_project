__author__ = 'wqliceman'

from os import popen
from re import split

f = popen('dir', 'r')
for eachLine in f.readlines():
    print split('\s\s+|\t', eachLine.strip())
f.close()

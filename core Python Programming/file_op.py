# -*- coding: utf-8 -*-
__author__ = 'wqliceman'
import os
import sys
import base64

file = open('makeTextFile.py', 'r')
print file.tell()
for line in file:
    line.strip(os.linesep)
    print len(line),type(line)
print file.tell()
file.seek(0)
data = file.readline()
print data
print file.encoding

file.close()

print len(sys.argv), sys.argv
print os.stat(sys.argv[0])

print "--"*20
tempdir = '.\\tmp'
if not os.path.exists(tempdir):
    print 'dir not found, then new one'
    os.mkdir(tempdir)
else:
    print 'got it'

os.chdir(tempdir)
cwd = os.getcwd()
print '***current directory is: ', cwd

print '***create a new dir : example'
if not os.path.exists('example'):
    os.mkdir('example')
os.chdir('example')
cwd = os.getcwd()
print cwd

print '**creating test file'
f = open('test.txt', 'w')
f.write('foo'+os.linesep)
f.write('bar'+os.linesep)
f.close()
print '***dir list'
print os.listdir(cwd)

print '***rename test.txt file--> helloworld.txt'
if not os.path.exists('helloworld.txt'):
    os.rename('test.txt', 'helloworld.txt')
print '**full path is:'
fullname = os.path.join(cwd, os.listdir(cwd)[0])
print fullname
print os.path.split(fullname)

print 'delete the file, then del example and tmp dir'
os.remove(fullname)
os.chdir(os.pardir)
os.rmdir('.\\example')
os.chdir(os.pardir)
os.rmdir('.\\tmp')
print '****over'

print '---'*20
str = "wqliceman"
encode_str =  base64.encodestring(str)
print 'str= %s, encode_str= %s' % (str, encode_str)
decode_str = base64.decodestring(encode_str)
print 'decode_str= %s' % decode_str



#!/usr/bin/env python
# coding=utf-8

import re

pattern = re.compile(r'hello')
result1 = re.match(pattern, 'hello')
result2 = re.match(pattern, "hello, wqliceman")
result3 = re.match(pattern, 'Hello, ice')

if result1:
    print result1.group()
    print result1.re
    print result1.endpos
else:
    print '1 failed'

if result2:
    print result2.group()
else:
    print '2 failed'

if result3:
    print result3.group()
else:
    print '3 failed'
print '---'*10
m = re.match(r'(\w+) (\w+)(?P<id>.*)', 'hello world!!! wqliceman')

print 'm.string:', m.string
print 'm.re', m.re
print 'm.pos;', m.pos
print 'm.endpos:', m.endpos
print 'm.lastindex:', m.lastindex
print 'm.lastgroup:', m.lastgroup
print 'm.group():', m.group()
print 'm.group(1,2):', m.group(1,2)
print 'm.groups():', m.groups()
print 'm.start(2):', m.start(2)
print 'm.end(2):', m.end(2)
print 'm.span(2):', m.end(2)
print r'm.expand(r"\g \g\g"):', m.expand(r'\2 \2\3')

print '---'*10
pattern = re.compile(r'world')
match = re.search(pattern, 'hello world!!')
if match:
    print match.group()
else:
    print "NONE"

print '---'*10
pattern = re.compile(r'\d+')
print re.split(pattern, 'one1two2three3four4five555six666')

print '---'*10
print re.findall(pattern, 'one1two2three3four4five555six666')

print '---'*10
for m in re.finditer(pattern, 'one1two2three3four4five555six666'):
    print m.group()

print '---'*10
pattern = re.compile(r'(\w+) (\w+)')
s = 'hello world! are you ok?'

print re.sub(pattern, r'\2 \1', s)

def func(m):
    return m.group(1).title() +' ' + m.group(2).title()

print re.sub(pattern, func, s)

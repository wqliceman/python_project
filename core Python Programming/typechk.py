#!/usr/bin/env python

def displayNumType(num):
    print num, 'is'
    if(isinstance(num, (int, long, float, complex))):
       print 'a number of type:', type(num).__name__
    else:
       print 'not a number at all!'

displayNumType(-69)
displayNumType(999999999999999999999999999L)
displayNumType(98.5)
displayNumType(-5.2+2.3j)
displayNumType("xxxx")


foo  = "abcdefgh"
print foo[::-1]

print foo[:2:-1]

print foo[2:1:-2]

foolist = [1234,"abcd", 234.56, "dcba"]

print foolist[::-1]
print foolist

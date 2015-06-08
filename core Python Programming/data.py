along = 3333333333333333333333333333333333l
print str(along)
print repr(along)

aComplex = 4.5+23.5j
print aComplex.real
print aComplex.imag
print aComplex.conjugate()


print 4.2**3.2
print 8.0/3.0
print 14*0x04

print 30&45
print 30|45
print 30&45


print '-----------------------------'

print cmp(2, 4)

print int(4.5555)
print long(423)
print complex(34)
print complex(32,-5)

strInt="2323"
print   long(strInt)  #strInt.atol()

print abs(-1)
print abs(-10.)
print coerce(1,2)
print coerce(1j, 134L)

print divmod(10,3)

print pow(2,3,3)

print round(3.45)
print round(3.55)
print round(3.87)
print round(3.4565, 2)
print round(3.4565, 3)
import math
for i in range(10):
    print round(math.pi, i)

for i in(0.2, 0.7, 1.2, 1.7, -0.2, -0.7, -1.2, -1.7):
    print "int(%.1f)\t%+.1f" % (i, float(int(i)))
    print "floor(%.1f)\t%+.1f" %(i, math.floor(i))
    print "round(%.1f)\t%+.1f" %(i, round(i))
    print '-'*20


print hex(233)
print hex(65535)

print oct(255)
print ord('a')
print ord('A')
print ord('1')

print chr(100)
print chr(48)

bar = True
print bar+100

from decimal import Decimal
dec = Decimal(.1)
print dec
dec = Decimal('.1')
print dec

print '--'*20
import random
#print randint(1,30)
#print random()


def degree(score):
    retVal = ''
    if(score >=90 and score <=100):
        retVal= 'A'
    elif(score >=80 and score <=89):
        retVal='B'
    elif(score >=70 and score <=79):
        retVal = 'C'
    elif(score >=60 and score <=69):
        retVal = 'D'
    else:
        retVal = 'F'
    return retVal

print degree(78)

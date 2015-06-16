__author__ = 'ntkodev'
import threading
from time import sleep, ctime

loops=[4,2]

'''
class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        apply(self.func, self.args)

def loop(nloop, nsec):
    print 'start loop',nloop, 'at:',ctime()
    sleep(nsec)
    print 'loop',nloop, 'done at:',ctime()

def main():
    print 'starting at;',ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(
            target=ThreadFunc(loop, (i, loops[i]), loop.__name__)
        )
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print 'all DONE at:', ctime()
'''

from MyThread import Mythread


def fib(x):
    sleep(0.05)
    if x<2: return 1
    return (fib(x-2) + fib(x-1))

def fac(x):
    sleep(0.1)
    if x<2: return 1
    return (x*fac(x-1))

def sum(x):
    sleep(0.1)
    if x<2: return 1
    return (x + sum(x-1))

funcs = [fib, fac, sum]
n = 12

def main():
    nfuncs = range(len(funcs))
    print '******SIGNAL THREAD********'
    for i in nfuncs:
        print 'starting', funcs[i].__name__, 'at:', ctime()
        print funcs[i](n)
        print funcs[i].__name__, 'finished at:',ctime()

    print '\n******MULTIL THREAD******'
    threads=[]
    for i in nfuncs:
        t = Mythread(funcs[i], (n,), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
        print threads[i].getResult()

    print 'All DONE'

if __name__ == "__main__":
    main()

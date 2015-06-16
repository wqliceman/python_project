__author__ = 'ntkodev'

from random import randint
from time import sleep
from Queue import Queue
from MyThread import Mythread

def writeQ(queue):
    print 'producting object for Q...', queue.put('wqliceman',1)
    print 'size now :', queue.qsize()

def readQ(queue):
    val = queue.get(1)
    print 'consumed object from Q.... size now:',queue.qsize()

def writer(queue, nloops):
    for i in range(nloops):
        writeQ(queue)
        sleep(randint(1,3))

def reader(queue, nloops):
    for i in range(nloops):
        readQ(queue)
        sleep(randint(2,5))


funcs = [ writer, reader]
nfuncs = range(len(funcs))

def main():
    nloops = randint(2,5)
    q = Queue(32)

    threads = []
    for i in nfuncs:
        t = Mythread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print "all Done"

if __name__ == "__main__":
    main()
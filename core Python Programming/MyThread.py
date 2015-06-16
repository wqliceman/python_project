__author__ = 'ntkodev'
import threading
from time import sleep, ctime

class Mythread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        print 'starting', self.name, 'at:',ctime()
        self.res = apply(self.func, self.args)
        print self.name, 'finishedad :', ctime()

    def loop(nloop, nsec):
        print 'start loop',nloop, 'at:',ctime()
        sleep(nsec)
        print 'loop',nloop,'done at;', ctime()

    def main(self):
        print 'starting at:',ctime()
        threads = []
        nloops = range(len(loops))

        for i in nloops:
            t = Mythread(self.loop, (i, loops[i]), self.loop.__name__)
            threads.append(t)

        for i in nloops:
            threads[i].start()

        for i in nloops:
            threads[i].join()

        print 'all DONE at:',ctime()
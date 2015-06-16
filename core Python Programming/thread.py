__author__ = 'ntkodev'
import thread
import threading
from time import sleep, ctime

'''
def loop0():
    print 'start loop0 at:', ctime()
    sleep(4)
    print 'loop0 done at:', ctime()

def loop1():
    print 'start loop1 at:', ctime()
    sleep(2)
    print 'loop1 done at:', ctime()

def main():
    print 'start at:', ctime()
    thread.start_new_thread(loop0,())
    thread.start_new_thread(loop1,())
    sleep(6)
    print 'all DONE at;', ctime()

'''
loops = [4,2]
def loop(nloop, nsec):
    print 'start loop',nloop, 'at;',ctime()
    sleep(nsec)
    print 'loop',nloop, 'done at;', ctime()

def main():
    print 'starting at;',ctime()
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = threading.Thread(target=loop,
                             args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()


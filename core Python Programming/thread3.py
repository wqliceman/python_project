#!/usr/bin/env python
# coding=utf-8

import threading
import time

data = 0
rlock = threading.RLock()

def func():
    global data
    print '%s acquire lock......' % threading.currentThread().getName()
    if rlock.acquire():
        print '%s get the lock..' % threading.currentThread().getName()
        data += 1
        time.sleep(2)

        print '%s acquire lock again...' % threading.currentThread().getName()
        if rlock.acquire():
            print "%s get the lock." %  threading.currentThread().getName()
            time.sleep(2)

        print '%s release lock...'% threading.currentThread().getName()
        rlock.release()
        time.sleep(2)

        print '%s release lock 2.' % threading.currentThread().getName()

        rlock.release()

threads = []

for i in range(0,4):
    threads.append(threading.Thread(target=func))

for i in range(0,4):
    threads[i].start()

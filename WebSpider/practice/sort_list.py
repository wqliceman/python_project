# -*- coding: utf-8 -*-
__author__ = 'wqliceman'

import random

def bubble(list):
    for i in range(len(list)):
        for j in range(0, len(list)-i-1):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1], list[j]




if __name__ == '__main__':
    list = []
    for i in range(10):
        list.append(random.randint(1, 100))

    print 'list :', list

    bubble(list)
    print 'bubble sort: ', list
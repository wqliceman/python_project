# -*- coding: utf-8 -*-
__author__ = 'wqliceman'

import xlwt

workbook = xlwt.Workbook(encoding='utf-8')
booksheet = workbook.add_sheet('Sheet 1')


test = ['a', 'b', 'c', 'd']
for i in range(0, 10):
    for j in range(0,4):
        booksheet.write(i, j, test[j])
workbook.save('test.xls')



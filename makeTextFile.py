#!/usr/bin/env python

'makeTextFile.py ---create text file'


import os
ls = os.linesep

#get filename
while True:
    fname = raw_input("Please input a file name:")
    if os.path.exists(fname):
        print "ERROR: '%s' already exists." % fname
    else:
        break

# get file content

all = []
print "\nEnter lines  ('.' by itself to quit)\n"

while True:
    entry = raw_input(">")
    if entry == '.':
        break
    else:
        all.append(entry)

# write file
fobj = open(fname, 'w')
fobj.writelines('%s%s' % (x, ls) for x in all)
fobj.close()
print 'DONE!'

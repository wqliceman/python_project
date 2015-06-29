#!/usr/bin/env python
# coding=utf-8

import sys
import os
import ConfigParser

cfg = ConfigParser()

if __name__ == "__main__":
    print len(sys.argv)
    for arg in sys.argv:
        print arg

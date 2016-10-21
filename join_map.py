#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:24:14 2016

@author: Yaqian
"""

'''
#!/usr/bin/env python2
"""Example mapper module for counting words via map-reduce.

This file is saved as wc_mapper.py with execute permission 
(chmod +x wc_mapper.py)"""

import sys


def main():
    """Take lines from stdin and emit each word with count 1.

    This is for illustration purposes, treating any string separated by
    whitespace as a 'word'. Additional cleaning (e.g., removing punctuation)
    could be added if necessary."""
    for line in sys.stdin:
        words = line.strip().split()
        for word in words:
            print word + '\t' + '1'

if __name__ == "__main__":
    main()
'''

import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        line = line.strip(",")
        print line

if __name__ == "__main__":
    main()
    

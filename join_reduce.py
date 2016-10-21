#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:24:43 2016

@author: Yaqian
"""

'''
#!/usr/bin/env python2
"""Example reducer module for counting words via map-reduce.

This file is saved as wc_reducer.py with execute permission 
(chmod +x wc_reducer.py)"""

from itertools import groupby
from operator import itemgetter
import sys


def read_mapper_output(lines):
    """Returns generator over each line of lines as a list split by tabs."""
    for line in lines:
        yield line.rstrip().split('\t', 1)


def main():
    """Take lines from stdin and print the sum in each group of words."""
    data = read_mapper_output(sys.stdin)
    for word, group in groupby(data, itemgetter(0)):
        total_count = sum([int(count) for _, count in group])
        print word + '\t' + str(total_count)

if __name__ == "__main__":
    main()
'''

#check for obvious errors and only output those that appear to be reasonable

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(lines):
    for line in lines:
        line = line.strip()
        line = line.split(",")
        

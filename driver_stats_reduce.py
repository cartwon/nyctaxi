#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:38:50 2016

@author: Yaqian
"""

import sys
from itertools import groupby
from operator import itemgetter

def main():
    
    n_trip = 0
    for line in sys.stdin:
        line=line.strip().split("\t")
        hack=line[0]
        date=line[1]
        hour=line[2]
        t_onduty=
        t_occupied=
        
        for hour, group in groupby(line,itemgetter(5)):
            n_pass=sum([int(count) for _, count in group])
        for hour, group in groupby(line,itemgetter(6)):
            n_trip=n_trip+1
        for hour, group in groupby(line,itemgetter(7)):
            n_mile=sum([int(count) for _, count in group])
        for hour, group in groupby(line,itemgetter(8)):
            earnings=sum([int(count) for _, count in group])
            
        print "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t" % (date, hour, hack,\
                t_onduty, t_occupied, n_pass, n_trip, n_mile, earnings)

if __name__ == "__main__":
   main()

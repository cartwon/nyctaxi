#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:38:50 2016

@author: Yaqian
"""


import sys

def main():
    
    for line in sys.stdin:
        line = line.strip().split("\t") #6 columns in total
        hack_pickup = line[0] #[id yyyy-mm-dd hh]
        hack, date, hour = hack_pickup.split(" ")
        t_occupied = line[1]
        n_pass = line[2]
        n_trip = line[3]
        n_mile = line[4]
        earning = line[5]
        
        #key: date-hour
        date_hour=date + " " + hour
        
        print "%s\t%s\t%s\t%s\t%s\t%s\t%s" % (date_hour,"1",t_occupied, n_pass, n_trip, n_mile, earning)

if __name__ == "__main__":
   main()
   

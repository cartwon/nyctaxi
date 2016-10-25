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

    current_date_hour = None
    drivers_occupied=0
    total_occupied=0
    total_pass = 0
    total_trip = 0
    total_mile = 0
    total_earnings = 0


    for line in sys.stdin:
        line=line.strip()
        date_hour, driver_count, t_occupied, n_pass, n_trip, n_mile, earning = line.split("\t")
        
        try:
            driver_count=int(driver_count)
            t_occupied=float(t_occupied)
            n_pass=int(n_pass)
            n_trip=int(n_trip)
            n_mile=float(n_mile)
            earning=float(earning)
        except:
            continue

        if current_date_hour==date_hour: #if this is an existing driver-hour
            drivers_occupied += driver_count
            total_occupied += t_occupied
            total_pass += n_pass
            total_trip += n_trip
            total_mile += n_mile
            total_earnings += earning
        else:
            if current_date_hour:
                print "%s\t%s\t%s\t%s\t%s\t%s\t%s" % (current_date_hour, drivers_occupied, total_occupied, total_pass, total_trip, total_mile, total_earnings)
            drivers_occupied=driver_count
            total_occupied=t_occupied
            total_pass=n_pass
            total_trip=n_trip
            total_mile=n_mile
            total_earnings=earning
            current_date_hour=date_hour

    if current_date_hour==date_hour:
        print "%s\t%s\t%s\t%s\t%s\t%s\t%s" % (current_date_hour, drivers_occupied, total_occupied, total_pass, total_trip, total_mile, total_earnings)

if __name__ == "__main__":
   main()

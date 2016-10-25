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

    current_hack_year_day_hr = None
    t_occupied=0
    n_pass = 0
    n_trip = 0
    n_mile = 0
    earnings = 0


    for line in sys.stdin:
        line=line.strip()
        hack_year_day_hr, trip_count, pickup_date, pickup_time,dropoff_datetime,passenger_count, trip_time, trip_mile,trip_earning = line.split("\t")
        try:
            trip_count=int(trip_count)
            passenger_count=int(passenger_count)
            trip_time=float(trip_time)/3600 #in hour
            trip_mile=float(trip_mile)
            trip_earning=float(trip_earning)
        except:
            continue

        if current_hack_year_day_hr==hack_year_day_hr: #if this is an existing driver-hour
            t_occupied+=trip_time
            n_pass+=passenger_count
            n_trip+=trip_count
            n_mile+=trip_mile
            earnings+=trip_earning

        else:
            if current_hack_year_day_hr:
                print "%s\t%s\t%s\t%s\t%s\t%s" % (current_hack_year_day_hr, t_occupied, n_pass, n_trip, n_mile, earnings)
            t_occupied=trip_time
            n_pass=passenger_count
            n_trip=trip_count
            n_mile=trip_mile
            earnings=trip_earning
            current_hack_year_day_hr=hack_year_day_hr

if __name__ == "__main__":
   main()

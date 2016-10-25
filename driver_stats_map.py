#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:38:50 2016

@author: Yaqian
"""


import sys
import datetime

def main():
    
    for line in sys.stdin:
        line = line.strip().split("\t") #20 columns in total
        hack_pickup = line[1] #[id yyyy-mm-dd hh:mm:ss]
        hack, pickup_date, pickup_time = hack_pickup.split(" ")
        dropoff_datetime=line[5]
        passenger_count = line[6]
        trip_time = line[7]
        trip_mile = line[8]
        trip_earning = line[19]
        
        #key: id-date-hour
        pickup_time_hour, pickup_time_min=pickup_time.split(":",1)
        hack_year_day_hr = hack + " " + pickup_date + " " + pickup_time_hour
        #convert time string to datetime object
        pickup_time=datetime.datetime.strptime(pickup_time, "%H:%M:%S")
        
        
        print "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (hack_year_day_hr,"1",\
            pickup_date, pickup_time,dropoff_datetime,passenger_count,\
            trip_time, trip_mile,trip_earning)

if __name__ == "__main__":
   main()
   

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
        line = line.strip().split(",")
        hack_license = line[1]
        
        pickup_datetime = line[5].split(" ")
        pickup_date=pickup_datetime[0]
        # round the time to the nearest hour
        pickup_time=pickup_datetime[1]
        pickup_time=datetime.datetime.strptime(pickup_time, "%H:%M:%S")
        dropoff_datetime = line[6].split(" ")
        dropoff_date=dropoff_datetime[0]
        # round the time to the nearest hour
        dropoff_time=dropoff_datetime[1]
        
        passenger_count = line[7]
        trip_mile = line[9]
        trip_earning = line[20]
        print "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (hack_license,\
            pickup_date, pickup_time,dropoff_date,dropoff_time,passenger_count,\
            "1",trip_mile,trip_earning)

if __name__ == "__main__":
   main()
   

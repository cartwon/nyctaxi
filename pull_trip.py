#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 20:15:20 2016

@author: Yaqian
"""

import sys

def main():
        
        medallion = "-1"
        hack_license = "-1"
        vendor_id = "-1"
        rate_code = "-1"
        store_flag = "-1"
        pickup_datetime = "-1"
        dropoff_datetime = "-1"
        passenger_count = "-1"
        trip_time = "-1"
        trip_distance = "-1"
        pickup_lati = "-1"
        pickup_longi = "-1"
        dropoff_lati = "-1"
        dropoff_longi = "-1"
        for line in sys.stdin:
            line = line.strip()
            obs = line.split(",") #a list of values
            medallion = obs[0]
            hack_license = obs[1]
            vendor_id = obs[2]
            rate_code = obs[3]
            store_flag = obs[4]
            pickup_datetime = obs[5]
            dropoff_datetime = obs[6]
            passenger_count = obs[7]
            trip_time = obs[8]
            trip_distance = obs[9]
            pickup_lati = obs[10]
            pickup_longi = obs[11]
            dropoff_lati = obs[12]
            dropoff_longi = obs[13]
            if "2013-01-01 01:" in pickup_datetime: #an hour of trip data
                print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s'\
            % (medallion, hack_license, vendor_id, rate_code,\
            store_flag, pickup_datetime, dropoff_datetime,\
            passenger_count, trip_time, trip_distance, pickup_longi,\
            pickup_lati, dropoff_longi, dropoff_lati)

if __name__ == "__main__":
    main()

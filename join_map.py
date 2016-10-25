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
    try:
        
        for line in sys.stdin:
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
            payment_type = "-1"
            fare = "-1"
            surcharge = "-1"
            tax = "-1"
            tip = "-1"
            tolls = "-1"
            total_amount = "-1"

            line = line.strip()
            obs = line.split(",") #a list of values
            if len(obs)==14: #trip data
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
                
            else: #fare data
                medallion = obs[0]
                hack_license = obs[1]
                vendor_id = obs[2]
                pickup_datetime = obs[3]
                payment_type = obs[4]
                fare = obs[5]
                surcharge = obs[6]
                tax = obs[7]
                tip = obs[8]
                tolls = obs[9]
                total_amount = obs[10]
            print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s'\
            % (medallion, hack_license, vendor_id, rate_code,\
            store_flag, pickup_datetime, dropoff_datetime,\
            passenger_count, trip_time, trip_distance, pickup_longi,\
            pickup_lati, dropoff_longi, dropoff_lati, payment_type,\
            fare, surcharge, tax, tip, tolls, total_amount) 
    except:
        pass
    
if __name__ == "__main__":
    main()
    

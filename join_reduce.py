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
        yield line.rstrip().split('\t', 1) #split the string by '\t' one time


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

import sys

last_hack_license = None
cur_pickup_datetime = "-"
cur_payment_type = "-"
cur_fare = "-"
cur_surcharge = "-"
cur_tax = "-"
cur_tip = "-"
cur_tolls = "-"
cur_total_amount = "-"

for line in sys.stdin:
    line = line.strip()
    medallion, hack_license, vendor_id, rate_code,\
    store_flag, pickup_datetime, dropoff_datetime,\
    passenger_count, trip_time, trip_distance, pickup_longi,\
    pickup_lati, dropoff_longi, dropoff_lati, payment_type,\
    fare, surcharge, tax, tip, tolls, total_amount = line.split("\t")

    if not last_hack_license or last_hack_license != hack_license: #if this is a new driver, remember the fare data
        last_hack_license = hack_license
        cur_pickup_datetime = pickup_datetime
        cur_payment_type = payment_type
        cur_fare = fare
        cur_surcharge = surcharge
        cur_tax = tax
        cur_tip = tip
        cur_tolls = tolls
        cur_total_amount = total_amount
    elif hack_license == last_hack_license: # then add the fare data to the trip data
        pickup_datetime = cur_pickup_datetime
        payment_type = cur_payment_type
        fare= cur_fare
        surcharge = cur_surcharge
        tax = cur_tax
        tip = cur_tip
        tolls = cur_tolls
        total_amount = cur_total_amount
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (medallion, hack_license, vendor_id, rate_code,\
                          store_flag, pickup_datetime, dropoff_datetime,\
                          passenger_count, trip_time, trip_distance, pickup_longi,\
                          pickup_lati, dropoff_longi, dropoff_lati, payment_type,\
                          fare, surcharge, tax, tip, tolls, total_amount)
        
        
        

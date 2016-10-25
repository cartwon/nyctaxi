#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-



import sys

last_hack_pickup = None
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
    medallion, hack_pickup, vendor_id, rate_code,\
    store_flag, dropoff_datetime,\
    passenger_count, trip_time, trip_distance, pickup_longi,\
    pickup_lati, dropoff_longi, dropoff_lati, payment_type,\
    fare, surcharge, tax, tip, tolls, total_amount = line.split("\t")

    if not last_hack_pickup or last_hack_pickup != hack_pickup: #if this is a new driver, remember the fare data
        last_hack_pickup = hack_pickup
        cur_payment_type = payment_type
        cur_fare = fare
        cur_surcharge = surcharge
        cur_tax = tax
        cur_tip = tip
        cur_tolls = tolls
        cur_total_amount = total_amount
    elif hack_pickup == last_hack_pickup: # then add the fare data to the trip data
        payment_type = cur_payment_type
        fare= cur_fare
        surcharge = cur_surcharge
        tax = cur_tax
        tip = cur_tip
        tolls = cur_tolls
        total_amount = cur_total_amount
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (medallion, hack_pickup, vendor_id, rate_code,\
                          store_flag, dropoff_datetime,\
                          passenger_count, trip_time, trip_distance, pickup_longi,\
                          pickup_lati, dropoff_longi, dropoff_lati, payment_type,\
                          fare, surcharge, tax, tip, tolls, total_amount)
        
        
        

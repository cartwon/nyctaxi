#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 20:42:36 2016

@author: Yaqian
"""

import sys

def main():
        
        medallion = "-1"
        hack_license = "-1"
        vendor_id = "-1"
        pickup_datetime = "-1"
        payment_type = "-1"
        fare = "-1"
        surcharge = "-1"
        tax = "-1"
        tip = "-1"
        tolls = "-1"
        total_amount = "-1"
            
        for line in sys.stdin:
            line = line.strip()
            obs = line.split(",") #a list of values
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
            if "2013-01-01 01:" in pickup_datetime: #an hour of trip data
                print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s'\
            % (medallion, hack_license, vendor_id, \
            pickup_datetime, payment_type,\
            fare, surcharge, tax, tip, tolls, total_amount)

if __name__ == "__main__":
    main()

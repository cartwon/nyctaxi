#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import copy
from datetime import datetime, timedelta

def main():
	fmt = '%Y-%m-%d %H:%M:%S'
	for line in sys.stdin:
		line = line.strip()
		data = line.split('\t')
		pt = datetime.strptime(data[5], fmt)
		dt = datetime.strptime(data[6], fmt)
		if (dt - pt).total_seconds() < 1:
			continue
		speed = float(data[9]) / (dt - pt).total_seconds()
		earning_rate = float(data[20]) / (dt - pt).total_seconds()
		# key, value = line.split('\t')
		# value = value.split(',')
		# temp = copy.deepcopy(value)
		while pt.hour != dt.hour:
			time_segment = timedelta(hours = 1, minutes = -pt.minute, seconds = -pt.second-1)
			time_break = pt + time_segment
			distance = time_segment.total_seconds() * speed
			earnings = time_segment.total_seconds() * earning_rate
			key = data[1] + datetime.strftime(pt, fmt)[:13]
			value = ",".join([datetime.strftime(pt, fmt), \
				datetime.strftime(time_break, fmt), data[7], \
				str(distance), str(earnings)])
			print(key + '\t' + value)
			pt = pt + time_segment + timedelta(seconds = 1)
			# temp[4] = pt + timedelta(hours = 1, minutes = -pt.minute, seconds = -pt.second-1)
			# temp[6] = str(timedelta.total_seconds(temp[4] - pt))
			# temp[4] = datetime.strftime(temp[4], fmt)
			# temp = ','.join(temp)
			# key_out = key[:10] + datetime.strftime(pt, fmt)
			# sys.stdout.write("{0}\t{1}\n".format(key_out, temp))
			# pt = pt + timedelta(hours = 1, minutes = -pt.minute, seconds = -pt.second)
		key = data[1] + datetime.strftime(pt, fmt)[:13]
		value = ",".join([datetime.strftime(pt, fmt), \
			datetime.strftime(dt, fmt), data[7], \
			data[9], data[20]])
		print(key + '\t' + value)

if __name__ == "__main__":
    main()

'''
DATA: 
0 medallion 
1 hack_license
2 vendor_id
3 rate_code
4 store_and_fwd_flag
5 pickup_datetime
6 dropoff_datetime
7 passenger_count
8 trip_time_in_secs
9 trip_distance
10 pickup_longitude
11 pickup_latitude
12 dropoff_longitude
13 dropoff_latitude
14 payment_type
15 fare_amount
16 surcharge
17 mta_tax
18 tip_amount
19 tolls_amount
20 total_amount
'''
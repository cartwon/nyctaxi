#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
from itertools import groupby
from operator import itemgetter
from datetime import datetime, timedelta

def read_mapper_output(file, separator = '\t'):
	for line in file:
		yield line.rstrip().split(separator, 1)

def main():
	fmt = '%Y-%m-%d %H:%M:%S'
	data = read_mapper_output(sys.stdin, separator = '\t')
	for key, group in groupby(data, itemgetter(0)):
		pt, dt, t_onduty, t_occupied, n_pass, n_trip, n_mile, earnings = None, None, 0, 0, 0, 0, 0, 0

		for key, value in group:
			value = value.strip().split(',')
			pt_tmp = datetime.strptime(value[0], fmt)
			dt_tmp = datetime.strptime(value[1], fmt)
			trip_time_tmp = (dt_tmp - pt_tmp).total_seconds() / 3600 # in hour
			t_occupied += trip_time_tmp
			n_pass += int(value[2])
			n_trip += 1
			n_mile += float(value[3])
			earnings  += float(value[4])
			t_onduty += trip_time_tmp
			if dt == None and pt_tmp.minute < 30:
				t_onduty += pt_tmp.minute / 60
			elif dt != None and (pt_tmp - dt).total_seconds() < 1800:
				t_onduty += (pt_tmp - dt).total_seconds() / 3600
			pt = pt_tmp
			dt = dt_tmp
		out_string = [key[10:20], key[21:], key[:10],\
		 str(t_onduty), str(t_occupied), str(n_pass), str(n_trip), str(n_mile), str(earnings)]
		out_string = '\t'.join(out_string)
		print out_string
if __name__ == "__main__":
	main()

'''
value: 
0 pickup_datetime
1 dropoff_datetime
2 passenger_count
3 trip_distance
4 total_amount
'''
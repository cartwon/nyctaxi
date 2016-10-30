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
	data = read_mapper_output(sys.stdin, separator = '\t')
	for key, group in groupby(data, itemgetter(0)):

		drivers_onduty, drivers_occupied, t_onduty, t_occupied,\
		n_pass, n_trip, n_mile, earnings = 0, 0, 0, 0, 0, 0, 0, 0

		for key, value in group:
			value = value.strip().split(',')
			if float(value[0]) > 0:
				drivers_onduty += 1
			if float(value[1]) > 0:
				drivers_occupied += 1
			t_onduty += float(value[0])
			t_occupied += float(value[1])
			n_pass += int(value[2])
			n_trip += int(value[3])
			n_mile += float(value[4])
			earnings += float(value[5])
		out_string = [key[:10], key[10:], str(drivers_onduty), str(drivers_occupied),\
		str(t_onduty), str(t_occupied), str(n_pass), str(n_trip), str(n_mile), str(earnings)]
		out_string = '\t'.join(out_string)
		print out_string
if __name__ == "__main__":
	main()

'''
DATA: 
0 t_onduty
1 t_occupied
2 n_pass
3 n_trip
4 n_mile
5 earnings
'''
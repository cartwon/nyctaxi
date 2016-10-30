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
	fmt = "%Y-%m-%d %H:%M:%S"
	data = read_mapper_output(sys.stdin, separator = '\t')
	for key, group in groupby(data, itemgetter(0)):
		left = []
		right = []
		for key, value in group:
			value = value.strip().split(",")
			if len(value) == 14:
				left = value
				try:
					pt = datetime.strptime(value[5], fmt)
					dt = datetime.strptime(value[6], fmt)
				except:
					left = []
			elif len(value) == 11:
				right = value
			else:
				pass

		try:
			dis_lati = (float(left[11])-float(left[13]))*110.574/1.609
			dis_longi = (float(left[11])-float(left[13]))*110.574*0.7578/1.609
			if left == [] or right == []:
				pass
			elif float(left[10]) < -80 or float(left[10]) > -60\
			or float(left[11]) < 30 or float(left[11]) > 50\
			or float(left[12]) < -80 or float(left[12]) > -60\
			or float(left[13]) < 30 or float(left[13]) > 50\
			or (dis_lati**2+dis_longi**2) > 2 * (float(left[9])**2)\
			or (dt - pt).total_seconds() > float(left[8]) * 1.5\
			or (dt - pt).total_seconds() < float(left[8]) * 0.67:
				pass
			else:
				print("\t".join(left + right[4:]))
		except:
			pass
if __name__ == "__main__":
    main()
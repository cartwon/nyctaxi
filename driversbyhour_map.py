#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys

def main():
	for line in sys.stdin:
		data = line.strip().split('\t')
		key = data[0] + data[1]
		value = ','.join(data[3:])
		print key + '\t' + value
if __name__ == "__main__":
	main()
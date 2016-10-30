#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        obs = line.split(",") #a list of values
        key = ""
        value = ""
        if obs[0] == "medallion":
        	continue
        if len(obs) == 14: #trip data
            key = obs[1] + obs[5]
        elif len(obs) == 11: #fare data
            key = obs[1] + obs[3]
        separator = '\t'
        out_string = key + separator +line
        print(out_string)
    
if __name__ == "__main__":
    main()
    

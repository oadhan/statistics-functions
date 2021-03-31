#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 21:16:50 2020

@author: oviya
"""

'''
This function takes a file and a percentile tail, and finds the lower and upper
bounds of the data set in the file set at the tails given.

1) An numpy array is created out of the file, sorted, sized

2) The number of samples per percentile is calculated

3) The total probability mass is found and divided by two to find the end tails

4) The indices are calculated from the tails and the samples in each percentile. 
(Subtracted from 1 to fit Python indexing rules --> start at 0)

5) The upper and lower bounds from the data are found with the indices.

6) A print output is generated.
'''

import numpy as np

def empiricalSampleBounds(file, tail):
    data = np.genfromtext(file, delimiter = ",")
    data = np.sort(data)
    length = data.size
    samples_in_one_percentile = length / 100
    
    total_probability_mass = 100 - tail
    upper_tail = 100 - (total_probability_mass / 2)
    lower_tail = total_probability_mass / 2
    
    upper_index = 1 - round(samples_in_one_percentile * upper_tail)
    lower_index = 1 - round(samples_in_one_percentile * lower_tail)
    
    upper_bound = data[upper_index]
    lower_bound = data[lower_index]
    
    print("lowerBound = " + lower_bound + ", upperBound = " + upper_bound)
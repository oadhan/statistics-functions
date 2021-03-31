#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 19:45:39 2020

@author: oviya

This function takes an array, finds its mean, median, 
standard deviation, mean absolute deviation, length, 
and standard error of the mean and outputs it all as 
an array when all_descriptives() is called.

"""


import numpy as np

def mad(array):
    array = np.array(array)
    sum = np.sum(array)   
    length = array.size
    mean = sum/length
    
    sum_of_diffs = 0
    i = 0
    
    while i < length:
        difference = mean - array[i]
        absolute_diff = np.absolute(difference)
        sum_of_diffs = sum_of_diffs + absolute_diff
        i = i + 1
        
    mad = sum_of_diffs / length
    
    writtenBy = "Oviya Adhan"
    
    return mad

def all_descriptives(array):
    array = np.array(array)
    mean = np.mean(array)
    median = np.median(array)
    stddev = np.std(array)
    mad = mad(array)
    
    rows = len(array)
    columns = len(array[0])
    n = rows * columns
    
    sem = stddev / (n ** (1/2))
    
    alldescriptives = [mean, median, stddev, mad, n, sem]
    
    return alldescriptives
    
    
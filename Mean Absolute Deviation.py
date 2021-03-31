#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 09:30:06 2020

@author: oviya
"""

# Inputs: Any set of numbers (ex. lists, arrays)
# Outputs: Mean absolute deviation (MAD)

import numpy as np

def mad(numbers):
    array = np.array(numbers)
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

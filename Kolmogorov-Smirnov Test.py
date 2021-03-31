#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 20:06:32 2020

@author: oviya
"""

"""

This function runs the  Kolmogorov-Smirnov (KS) test, a classic example of a goodness-of-fit hypothesis test

Input: takes in 1-D Numpy arrays

Process:
    Flag 1 --> Classic KS 
    Flag 2 --> Total KS 

Output:
    Flag 1 --> (largest distance between the two cumulative sample disturbutions)
    Flag 2 --> (total difference between the two sample dsitributions)
"""

import numpy as np

data = np.genfromtext(r'/Users/oviya/Desktop/Data Science/Data/kSinput2.csv', delimiter = ',')
x1 = data[:,0]
x2 = data[:,1]

def kstest(x1, x2, flag):
    #Flag 1 computes largest distance between the two cumulative sample disturbutions (classic KS)
    if flag == 1:
        max = np.max(x1+x2)
        min = np.min(x1+x2)
        sample_size = x1.size
        #space taken up by each point
        area = (max-min) / sample_size
        
        
        
    #Flag 2 computes total difference between the two sample dsitributions (total KS)
    elif flag == 2:
        
        
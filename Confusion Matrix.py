#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 18:46:13 2020

@author: oviya
"""

'''
This function takes in 3 columns of a csv, 
and a returns a matrix with true and false positives and negatives.
'''

import numpy as np

data = np.genfromtext(file, delimiter = ',')
x = data[,1]
y0 = data[,2]
y1 = data[,3]

def confusionMatrix(x, y0, y1, threshold):
    index = 0
    flag = 0
    while flag == 0:
        if x[index] == threshold:
            index = index 
            flag = flag + 1
        else:
            index = index + 1
    
    #COUNTDOWN TO THRESHOLD OF Y1
    i = y1.len()
    true_positives = 0
    while i >= index + 1:
        true_positives = true_positives + y1[i]
        i = i - 1
    
    #COUNTDOWN TO THRESHOLD OF Y0    
    j = y0.len()
    false_positives = 0
    while i >= index + 1:
        false_positives = false_positives + y0[j]
        j = i - 1
    
    #COUNTUP TO THRESHOLD OF Y1
    i = 0
    false_negatives = 0
    while i <= index:
        false_negatives = false_negatives + y1[i]
        i = i + 1   
    
    #COUNTUP TO THRESHOLD OF Y0
    j = 0
    true_negatives = 0
    while i <= index:
        true_negatives = true_negatives + y0[j]
        j = j + 1
    
    #Create output matrix
    confusion_matrix = np.array[[true_positives, false_positives],[false_negatives, true_negatives]]
    return confusion_matrix
    
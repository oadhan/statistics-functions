#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 19:02:59 2020

@author: oviya
"""

"""

a) Take in four inputs as arguments, in this order: a: The prior probability of A, b: The prior probability of B, c: The likelihood
(the probability of B given A) and d: A flag (the number 1 or 2) whether this function will implement 1) the simple or 2) the
explicit version of Bayes theorem. If the flag is set to 2 (the explicit version), input argument b should be interpreted as “the
probability of B given not A”, instead of the prior probability of B.

b) Regardless of the flag, the function should calculate the posterior probability of A given B from the information given in the
input arguments.

c) The function should return the value computed in b)

d) Assumptions: The input arguments should be real numbers from 0 to 1 for input arguments a to c and the integers 1 or 2
for input argument d, as stated in a).

"""

def bayesCalculator(a, b, c, d):
    #flag set to 1, simple version (prior probability of b KNOWN)
    if d == 1:
        prior_prob_a = a
        prior_prob_b = b
        b_given_a = c
        
        a_given_b = (prior_prob_a * b_given_a) / prior_prob_b
        
        return a_given_b
    
    #flag set to 2, explicit version (prior probability of b UNKNOWN)   
    elif d == 2:
        prior_prob_a = a
        b_given_not_a = b
        b_given_a = c
        
        a_given_b = (prior_prob_a * b_given_a) / ((prior_prob_a * b_given_a) + ((1 - prior_prob_a) * b_given_not_a))
        
        return a_given_b

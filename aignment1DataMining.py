#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#UserID::MovieID::Rating::Timestamp

import numpy as np


#global avarage
def globalAverage(matrix):
	avg = np.mean(matrix[:,2])
	return avg

def itemAverage(matrix, items):
    averages = []
    gb_avg = globalAverage(matrix)    
    for i in range (1, items + 1):
        arr = matrix[np.where(matrix[:,1] == i)]
        if (arr.size != 0):
            avg = globalAverage(arr)
        else:
            avg = gb_avg       
        averages.append(avg)
    return np.array(averages)

def userAverage(matrix, users):
    averages = []
    gb_avg = globalAverage(matrix)
    for i in range(1, users + 1):
        arr = matrix[np.where(matrix[:,0] == i)]
        if (arr.size != 0):
            avg = globalAverage(arr)
        else:
            avg = gb_avg
        averages.append(avg)
    return np.array(averages)










'''
ratingsFile = open('ratings.dat', 'r')
ratingsArray = []

for line in ratingsFile:
	splitted = line.split("::")
	ratingsArray.append(splitted)
'''	



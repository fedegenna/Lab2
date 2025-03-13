import numpy as np

def median(array):
	array = np.sort(array)
	if (len(array) % 2== 1):
		return array[int((len(array)-1)/2)]
	else:
		return (array[int(len(array)/2)-1]+ array[int(len(array)/2)])/2
		
def mean(array):
	mean = 0
	for i in range(len(array)):
		mean += array[i]
	mean = mean/len(array)
	return mean
	
	
from math import sqrt 

def mean2 (sample) :
    '''
    calculates the mean of the sample present in the object
    '''
    summ = sum (sample)
    N = len (sample)
    return summ / N

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 

def variance (sample, bessel = True) :
    '''
    calculates the variance of the sample present in the object
    '''
    summ = 0.
    sum_sq = 0.
    N = len (sample)
    for elem in sample :
       summ += elem
       sum_sq += elem * elem
    var = sum_sq / N - summ * summ / (N * N)
    if bessel : var = N * var / (N - 1)
    return var

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 

def sigma (sample, bessel = True) :
    '''
    calculates the sigma of the sample present in the object
    '''
    return sqrt (variance (sample, bessel))

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 

def sigma_mean (sample, bessel = True) :
    '''
    calculates the sigma of the sample present in the object
    '''
    N = len (sample)
    return sqrt (variance (sample, bessel) / N)
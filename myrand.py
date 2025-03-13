import random
import numpy as np
import matplotlib.pyplot as plt

def linear_random_generator(A,C,M,x):
	x= (A*x + C) %M
	return x
	

def rand_range (xMin, xMax) :
    '''
    generazione di un numero pseudo-casuale distribuito fra xMin ed xMax
    '''
    return xMin + random.random () * (xMax - xMin)
    
    
def rand_TAC(f, xMin, xMax):
    x = rand_range(xMin, xMax)
    y = rand_range(0, xMax)
    while y > f(x):
        x = rand_range(xMin, xMax)
        y = rand_range(0, xMax)
    return x
    
def generate_exponential(n_samples, tau):
    samples = []
    for _ in range(n_samples):
        u = rand_range(0, 1)  # Genera un numero casuale uniforme tra 0 e 1
        samples.append(-tau * np.log(1 - u))  # Metodo dell'inversa
    return samples

def rand_TCL_ms (mean, sigma, N_sum = 10) :
    '''
    generazione di un numero pseudo-casuale 
    con il metodo del teorema centrale del limite
    note media e sigma della gaussiana
    '''
    y = 0.
    delta = np.sqrt (3 * N_sum) * sigma
    xMin = mean - delta
    xMax = mean + delta
    for i in range (N_sum) :
        y = y + rand_range (xMin, xMax)
    y /= N_sum ;
    return y ;
    
def generate_uniform (N, seed = 0.) :
    '''
    generazione di N numeri pseudo-casuali distribuiti fra 0 ed 1
    a partire da un determinato seed
    '''
    if seed != 0. : random.seed (float (seed))
    randlist = []
    for i in range (N):
        # Return the next random floating point number in the range 0.0 <= X < 1.0
        randlist.append (random.random ())
    return randlist
    	

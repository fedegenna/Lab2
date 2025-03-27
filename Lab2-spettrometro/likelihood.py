import numpy as np

def exp_pdf (x, tau) :      
    '''
    the exponential probability density function
    '''
    if tau == 0. : return 1.
    if x < 0. : return 0. 
    return np.exp (-1 * x / tau) / tau
    
def loglikelihood (theta, pdf, sample) :
    '''
    the log-likelihood function calculated
    for a sample of independent variables idendically distributed 
    according to their pdf with parameter theta
    '''
    logL = 0.
    for x in sample:
      if (pdf (x, theta) > 0.) : logL = logL + np.log (pdf (x, theta))    
    return logL

def loglikelihood_product (theta, pdf, sample):
    
    product_of_pdf = 1.
    for x in sample:
      if (pdf (x, theta) > 0.) : product_of_pdf = product_of_pdf * pdf (x, theta)  
    logL = np.log (product_of_pdf (x, theta))  
    return logL

def loglikelihood_ratio (theta, pdf, sample, theta_hat) :
   
    return loglikelihood (theta, pdf, sample) - loglikelihood (theta_hat, pdf, sample)
       
def sezioneAureaMax_LL (
    g,              # funzione di likelihood trovare il massimo
    pdf,            # probability density function of the events
    sample,         # sample of the events
    x0,             # estremo dell'intervallo          
    x1,             # altro estremo dell'intervallo         
    prec = 0.0001): # precisione della funzione     
    
    r = 0.618
    x2 = x0 + r * (x1 - x0)
    x3 = x0 + (1. - r) * (x1 - x0) 
    larghezza = abs (x1 - x0)

    if (larghezza < prec)  : return ( x0 + x1) / 2.
    elif (g (x3, pdf, sample) < g (x2, pdf, sample)) :
      return sezioneAureaMax_LL (g, pdf, sample, x3, x1, prec)
    else:
      return sezioneAureaMax_LL (g, pdf, sample, x0, x2, prec) 
         

def intersect_LLR (
    g,              # funzione di cui trovare lo zero
    pdf,            # probability density function of the events
    sample,         # sample of the events
    xMin,           # minimo dell'intervallo          
    xMax,           # massimo dell'intervallo 
    ylevel,         # value of the horizontal intersection    
    theta_hat,      # maximum of the likelihood    
    prec = 0.0001): # precisione della funzione        
    '''
    Funzione che calcola zeri
    con il metodo della bisezione
    '''
    def gprime (x) :
        return g (x, pdf, sample, theta_hat) - ylevel

    xAve = xMin 
    while ((xMax - xMin) > prec) :
        xAve = 0.5 * (xMax + xMin) 
        if (gprime (xAve) * gprime (xMin) > 0.) : xMin = xAve 
        else                                    : xMax = xAve 
    return xAve 
    


import numpy as np 
import math

def passo (n, l, theta):
    return (n * l)/ np.sin(theta)

def errore_passo (n, l, theta, d_lambda, d_theta):
    return np.sqrt((n/np.sin(theta) * d_lambda)**2 + (n * l * np.cos(theta) / np.sin(theta)**2 * d_theta)**2)
           
''''def passo_medio (n, lambda, theta):
    return np.mean(passo(n, lambda, theta))
    
def errore_passo_medio (n, lambda, theta, d_lambda, d_theta):
    return np.sqrt(np.sum(errore_passo(n, lambda, theta, d_lambda, d_theta)**2))/len(n)'''

def angoli_rad (gradi, primi):
    """
    Converte un angolo espresso in gradi e primi in radianti.
    
    Parametri:
    gradi (int): La parte intera dell'angolo in gradi.
    primi (float): La parte frazionaria dell'angolo in primi.
    
    Ritorna:
    float: L'angolo in radianti.
    """
    angolo_in_gradi = gradi + primi / 60
    angolo_in_radianti = np.deg2rad(angolo_in_gradi)
    return angolo_in_radianti

def compatibilita (x, y, dx, dy):
    return abs(x - y) / np.sqrt(dx**2 + dy**2)

def main ():
    n = 1
    
    ''' lunghezze d'onda Na verde e arancione'''
    lambda_v = 498 * 10**(-9)
    d_lamda_v = 0.1 * 10**(-9)
    lambda_a = 615 * 10**(-9)
    d_lamda_a = 0.1 * 10**(-9)
    lambda_g = 589 * 10**(-9)
    d_lamda_g = 0.1 * 10**(-9)
    
    theta_v = 0.5 * (angoli_rad(239-167, 45-5))
    theta_a = 0.5 * (angoli_rad(248-159, 16-10))
    theta_g = 0.5 * (angoli_rad(246-161, 10))
    
    passo_v = passo(n, lambda_v, theta_v)
    passo_a = passo(n, lambda_a, theta_a)
    passo_g = passo(n, lambda_g, theta_g)
    
    d_passo_v = errore_passo(n, lambda_v, theta_v, d_lamda_v, 0.5 * angoli_rad(0, 3))
    d_passo_a = errore_passo(n, lambda_a, theta_a, d_lamda_a, 0.5 * angoli_rad(0, 3))
    d_passo_g = errore_passo(n, lambda_g, theta_g, d_lamda_g, 0.5 * angoli_rad(0, 3))
    
    print ("Passo verde: ", passo_v, "m")
    print ("Errore passo verde: ", d_passo_v, "m")
    print ("Passo arancione: ", passo_a, "m")
    print ("Errore passo arancione: ", d_passo_a, "m")
    print ("Passo giallo: ", passo_g, "m")
    print ("Errore passo giallo: ", d_passo_g, "m")
    
    '''print ("Compatibilità: ", compatibilita(passo_v, passo_a, d_passo_v, d_passo_a))
     '''   
if __name__ == "__main__":
    main()

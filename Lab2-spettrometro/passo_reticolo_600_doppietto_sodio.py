import numpy as np 
import math
from stats import stats

def passo (n, l, theta):
    return (n * l)/ np.sin(theta)

def errore_passo (n, l, theta, d_lambda, d_theta):
    return np.sqrt((n/np.sin(theta) * d_lambda)**2 + (n * l * np.cos(theta) / np.sin(theta)**2 * d_theta)**2)
           

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
    lambdas_doppietto = [5.89 * 10**(-7) , 5.896 * 10**(-7)]
    lambda_doppietto_stats = stats(lambdas_doppietto)
    lambda_doppietto = lambda_doppietto_stats.mean()
    d_lambda = lambda_doppietto_stats.sigma_mean()
    
    theta_1 = 0.5 * (angoli_rad(223-181, 10-30))
    theta_2 = 0.5 * (angoli_rad(223-181, 15-28))
    theta_3 = 0.5 * (angoli_rad(223-181, 8-37))
    
    thetas = [theta_1, theta_2, theta_3]
    theta_stats = stats(thetas)
    theta = theta_stats.mean()
    d_theta = theta_stats.sigma_mean()

    passo_doppietto = passo(n, lambda_doppietto, theta)
    d_passo_doppietto = errore_passo(n, lambda_doppietto, theta, d_lambda, d_theta)
    
    
    print ("Passo del reticolo da 1200: ", passo_doppietto, "m")
    print ("Errore passo: ", d_passo_doppietto, "m")
    
if __name__ == "__main__":
    main()

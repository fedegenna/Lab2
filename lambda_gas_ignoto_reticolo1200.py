import numpy as np 
import math
from stats import stats

def lunghezza (n, passo, theta):
    return passo * np.sin(theta)/n

def errore_lunghezza (n, passo, theta, d_passo, d_theta):
    return np.sqrt((np.sin(theta)/n * d_passo)**2 + (passo * np.cos(theta) / n * d_theta)**2)
           
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
    passi = [8.41 * 10**(-7) , 8.77 * 10**(-7), 8.70 * 10**(-7) ]
    passi_stats = stats(passi)
    passo = passi_stats.mean()
    d_passo = passi_stats.sigma_mean()

    theta_v = 0.5 * (angoli_rad(243-163, 30-10))
    theta_g = 0.5 * (angoli_rad(247-159, 45-30))
    theta_r = 0.5 * (angoli_rad(253-154, 30-7))
    theta_a = 0.5 * (angoli_rad(248-158, 45-20))

    lunghezza_v = lunghezza(n, passo, theta_v)
    lunghezza_a = lunghezza(n, passo, theta_a)
    lunghezza_r= lunghezza(n, passo, theta_r)
    lunghezza_g = lunghezza(n, passo, theta_g)
    
    d_lunghezza_v = errore_lunghezza(n, passo, theta_v, d_passo, 0.5 * angoli_rad(1, 0))
    d_lunghezza_a = errore_lunghezza(n, passo, theta_a, d_passo, 0.5 * angoli_rad(1, 0))
    d_lunghezza_r = errore_lunghezza(n, passo, theta_r, d_passo, 0.5 * angoli_rad(1, 0))
    d_lunghezza_g = errore_lunghezza(n, passo, theta_g, d_passo, 0.5 * angoli_rad(1, 0))

    print ("Lunghezza verde: ", lunghezza_v, "m")
    print ("Errore lunghezza verde: ", d_lunghezza_v, "m")
    print ("Lunghezza arancione: ", lunghezza_a, "m")
    print ("Errore lunghezza arancione: ", d_lunghezza_a, "m")
    print ("Lunghezza rossa: ", lunghezza_r, "m")
    print ("Errore lunghezza rossa: ", d_lunghezza_r, "m")
    print ("Lunghezza giallo: ", lunghezza_g, "m")
    print ("Errore lunghezza giallo: ", d_lunghezza_g, "m")
    
if __name__ == "__main__":
    main()

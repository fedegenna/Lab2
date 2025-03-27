import numpy as np 
import math
from stats import stats

def lunghezza (n, passo, theta):
    return passo * np.sin(theta)/n

def errore_lunghezza (n, passo, theta, d_passo, d_theta):
    return np.sqrt((np.sin(theta)/n * d_passo)**2 + (passo * np.cos(theta) / n * d_theta)**2)   

def angoli_rad (gradi, primi):
    angolo_in_gradi = gradi + primi / 60
    angolo_in_radianti = np.deg2rad(angolo_in_gradi)
    return angolo_in_radianti

def compatibilita (x, y, dx, dy):
    return abs(x - y) / np.sqrt(dx**2 + dy**2)

def sigma (x , y, t):
    return abs(x - y)/t

def main ():
    n = 1
    passo = 8.399 * 10**(-7)
    d_passo = 5 * 10**(-10)

    theta_v_1 = 0.5 * (angoli_rad(239-167, 45-5))
    theta_v_2 = 0.5 * (angoli_rad(239-167, 47-2))
    theta_v_3 = 0.5 * (angoli_rad(239-167, 43-6))

    theta_g_1 = 0.5 * (angoli_rad(246-161, 10))
    theta_g_2 = 0.5 * (angoli_rad(246-161, 7-4))
    theta_g_3 = 0.5 * (angoli_rad(246-160, 12-57))

    thetas_v = [theta_v_1, theta_v_2, theta_v_3]
    thetas_g = [theta_g_1, theta_g_2, theta_g_3]
    
    theta_stats_v = stats(thetas_v)
    theta_stats_g = stats(thetas_g)

    theta_v = theta_stats_v.mean()
    theta_g = theta_stats_g.mean()

    d_theta_v = theta_stats_v.sigma_mean()
    d_theta_g = theta_stats_g.sigma_mean()

    lunghezza_v = lunghezza(n, passo, theta_v)
    lunghezza_g = lunghezza(n, passo, theta_g)

    '''
    d_lunghezza_v = errore_lunghezza(n, passo, theta_v, d_passo, d_theta_v)
    d_lunghezza_g = errore_lunghezza(n, passo, theta_g, d_passo, d_theta_g)
    '''
    lunghezza_tabulata_v= 514.9 * 10**(-9)
    lunghezza_tabulata_g= 568.8 * 10**(-9)
    t=2

    sigma_v = sigma(lunghezza_v, lunghezza_tabulata_v, t)
    sigma_g = sigma(lunghezza_g, lunghezza_tabulata_g, t)

    print ("Lunghezza verde: ", lunghezza_v, "m")
    print ("Lunghezza gialla: ", lunghezza_g, "m")
    print ("Sigma verde: ", sigma_v, "m")
    print ("Sigma gialla: ", sigma_g, "m")

if __name__ == "__main__":
    main()

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

    theta_v_1 = 0.5 * (angoli_rad(243-163, 30-10))
    theta_v_2 = 0.5 * (angoli_rad(243-163, 33-6))
    theta_v_3 = 0.5 * (angoli_rad(243-163, 27-11))

    theta_g_1 = 0.5 * (angoli_rad(247-159, 45-30))
    theta_g_2 = 0.5 * (angoli_rad(248-159, -32))
    theta_g_3 = 0.5 * (angoli_rad(247-159, 40-27))

    theta_a_1 = 0.5 * (angoli_rad(248-158, 45-20))
    theta_a_2 = 0.5 * (angoli_rad(249-158, 2-15))
    theta_a_3 = 0.5 * (angoli_rad(248-158, 43-24))

    theta_r_1 = 0.5 * (angoli_rad(253-154, 30-7))
    theta_r_2 = 0.5 * (angoli_rad(253-154, 36-9))
    theta_r_3 = 0.5 * (angoli_rad(253-153, 34-58))

    thetas_v = [theta_v_1, theta_v_2, theta_v_3]
    thetas_g = [theta_g_1, theta_g_2, theta_g_3]
    thetas_a = [theta_a_1, theta_a_2, theta_a_3]
    thetas_r = [theta_r_1, theta_r_2, theta_r_3]

    theta_stats_v = stats(thetas_v)
    theta_stats_g = stats(thetas_g)
    theta_stats_a = stats(thetas_a)
    theta_stats_r = stats(thetas_r)

    theta_v = theta_stats_v.mean()
    theta_g = theta_stats_g.mean()
    theta_a = theta_stats_a.mean()
    theta_r = theta_stats_r.mean()

    d_theta_v = theta_stats_v.sigma_mean()
    d_theta_g = theta_stats_g.sigma_mean()
    d_theta_a = theta_stats_a.sigma_mean()
    d_theta_r = theta_stats_r.sigma_mean()

    lunghezza_v = lunghezza(n, passo, theta_v)
    lunghezza_g = lunghezza(n, passo, theta_g)
    lunghezza_a = lunghezza(n, passo, theta_a)
    lunghezza_r = lunghezza(n, passo, theta_r)

    errore_lunghezza_v = errore_lunghezza(n, passo, theta_v, d_passo, d_theta_v)
    errore_lunghezza_g = errore_lunghezza(n, passo, theta_g, d_passo, d_theta_g)        
    errore_lunghezza_a = errore_lunghezza(n, passo, theta_a, d_passo, d_theta_a)
    errore_lunghezza_r = errore_lunghezza(n, passo, theta_r, d_passo, d_theta_r)

    print ("Lunghezza verde: ", lunghezza_v, "m")
    print ("Lunghezza gialla: ", lunghezza_g, "m")
    print ("Lunghezza arancione: ", lunghezza_a, "m")
    print ("Lunghezza rossa: ", lunghezza_r, "m")
    print ("Errore lunghezza verde: ", errore_lunghezza_v, "m")
    print ("Errore lunghezza gialla: ", errore_lunghezza_g, "m")
    print ("Errore lunghezza arancione: ", errore_lunghezza_a, "m")
    print ("Errore lunghezza rossa: ", errore_lunghezza_r, "m")

if __name__ == "__main__":
    main()

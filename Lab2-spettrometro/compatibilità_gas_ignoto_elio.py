import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

def compatibilità(x, y, dx, dy):
    return abs(x - y) / np.sqrt(dx**2 + dy**2)

def main(): 

    lunghezza_v = 5.428 * 10**(-7)
    lunghezza_a = 5.965 * 10**(-7)
    lunghezza_r =6.409 * 10**(-7)
    lunghezza_g = 5.851 * 10**(-7)
    
    d_lunghezza_v = 4 * 10**(-10)
    d_lunghezza_a = 8 * 10**(-10)
    d_lunghezza_g = 5 * 10**(-10)
    d_lunghezza_r = 5 * 10**(-10)
    
    lunghezza_elio_v = 5.016 * 10**(-7)
    lunghezza_elio_a = 6.05 * 10**(-7)
    lunghezza_elio_r = 6.678 * 10**(-7)
    lunghezza_elio_g = 5.876 * 10**(-7)
    d_lunghezze_elio = 0

    compatibilità_v = compatibilità(lunghezza_v, lunghezza_elio_v, d_lunghezza_v, d_lunghezze_elio)
    compatibilità_a = compatibilità(lunghezza_a, lunghezza_elio_a, d_lunghezza_a, d_lunghezze_elio)
    compatibilità_r = compatibilità(lunghezza_r, lunghezza_elio_r, d_lunghezza_r, d_lunghezze_elio)
    compatibilità_g = compatibilità(lunghezza_g, lunghezza_elio_g, d_lunghezza_g, d_lunghezze_elio)

    print("Compatibilità verde: ", compatibilità_v)
    print("Compatibilità arancione: ", compatibilità_a)
    print("Compatibilità rosso: ", compatibilità_r)
    print("Compatibilità giallo: ", compatibilità_g)

if __name__ == "__main__":
    main()

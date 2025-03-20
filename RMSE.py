import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

def calculate_rmse(experimental, theoretical):
    """
    Calcola la distanza quadratica media (RMSE) tra i valori sperimentali e quelli teorici.
    
    Parametri:
    experimental (list or array): Lista di lunghezze d'onda misurate sperimentalmente.
    theoretical (list or array): Lista di lunghezze d'onda tabulate (valori di riferimento).
    
    Ritorna:
    float: Il valore RMSE che misura la compatibilità tra i due set di dati.
    """
    if len(experimental) != len(theoretical):
        raise ValueError("Le liste devono avere la stessa lunghezza")
    
    errors = np.array(experimental) - np.array(theoretical)
    rmse = np.sqrt(np.mean(errors**2))
    return rmse

def main(): 

    lunghezza_v = 5.428 * 10**(-7)
    lunghezza_a = 5.965 * 10**(-7)
    lunghezza_r =6.409 * 10**(-7)
    lunghezza_g = 5.851 * 10**(-7)
    
    lunghezza_elio_v = 5.016 * 10**(-7)
    lunghezza_elio_a = 6.05 * 10**(-7)
    lunghezza_elio_r = 6.678 * 10**(-7)
    lunghezza_elio_g = 5.876 * 10**(-7)
  
    lunghezza_neon_v = 5.401 * 10**(-7)
    lunghezza_neon_a = 6.03 * 10**(-7)
    lunghezza_neon_r = 6.402 * 10**(-7)
    lunghezza_neon_g = 5.852 * 10**(-7)

    experimental = [lunghezza_v, lunghezza_a, lunghezza_r, lunghezza_g]
    theoretical_elio = [lunghezza_elio_v, lunghezza_elio_a, lunghezza_elio_r, lunghezza_elio_g]
    theoretical_neon = [lunghezza_neon_v, lunghezza_neon_a, lunghezza_neon_r, lunghezza_neon_g]

    rmse_elio = calculate_rmse(experimental, theoretical_elio)
    rmse_neon = calculate_rmse(experimental, theoretical_neon)

    print("RMSE Elio: ", rmse_elio)
    print("RMSE Neon: ", rmse_neon)

if __name__ == "__main__":
    main()

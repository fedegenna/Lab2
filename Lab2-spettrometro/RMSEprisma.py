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
    rosso_sperimentale = 642.0
    giallo_sperimentale = 589.9
    verde_sperimentale = 545.4
    azzurro_sperimentale = 483.2
    viola_sperimentale = 440.2
    
    #valori tabulati, Neon:
    
    rosso_neon = 640.2
    giallo_neon = 585.2
    verde_neon = 540.1
    azzurro_neon = 479.2
    viola_neon = 437.7
    
    #valori tabulati, Elio:
    
    rosso_elio = 667.8
    giallo_elio = 587.6
    verde_elio = 501.6
    azzurro_elio = 492.2
    viola_elio = 471.2
    
    sperimentale = [rosso_sperimentale, giallo_sperimentale, verde_sperimentale, azzurro_sperimentale, viola_sperimentale]
    tabulato_neon = [rosso_neon, giallo_neon, verde_neon, azzurro_neon, viola_neon]
    tabulato_elio = [rosso_elio, giallo_elio, verde_elio, azzurro_elio, viola_elio]
    distanza_neon = calculate_rmse(sperimentale, tabulato_neon)
    distanza_elio = calculate_rmse(sperimentale, tabulato_elio)
    print("RMSE Neon: ", distanza_neon)
    print("RMSE Elio: ", distanza_elio)
    
if __name__ == "__main__":
    main()
    
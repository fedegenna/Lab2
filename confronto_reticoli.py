import numpy as np
import matplotlib.pyplot as plt
from astropy.coordinates import Angle
from iminuit import Minuit
from iminuit.cost import LeastSquares
from scipy.stats import chi2

def linear_func(x, A, B):
    return A + B*x

def main(): 

    inverse_reticolo = [1/1200, 1/600, 1/300]
    passo_1200 = 8.399 * 10**(-7)
    passo_600 = 1.657 * 10**(-6)
    passo_300 = 6.715 * 10**(-6)
    passi = [passo_1200, passo_600, passo_300]
    errore_passo_1200 = 5 * 10**(-10)
    errore_passo_600 = 3 * 10**(-9)
    errore_passo_300 =3 * 10**(-8)
    errori_passo =[errore_passo_1200, errore_passo_600, errore_passo_300]


    fig,ax = plt.subplots()
    ax.errorbar(inverse_reticolo, passi, yerr=errori_passo,fmt='o',label='boh')
    plt.grid()
    plt.xlabel('Inverso del numero di fenditure')
    plt.ylabel('Passo del reticolo')
    plt.title('Passo del reticolo in funzione del numero di fenditure')
    plt.legend()
    
    
    #interpolazione per ottenere i coefficenti:
    my_cost_func = LeastSquares(inverse_reticolo, passi, errori_passo, linear_func)
    m = Minuit(my_cost_func, A=1, B=0.001 ) 
    m.migrad()
    A = m.values['A']
    B = m.values['B']
    chi_squared = m.fval
    p_value = 1 - chi2.cdf(chi_squared,3)
    print(m.values)
    print(m.errors)
    print(m.covariance)
    
    #grafico con interpolazione:
    
    textstr = (
    f"A = {m.values['A']:.4f} ± {m.errors['A']:.4f}\n"
    f"B = {m.values['B']:.4f} ± {m.errors['B']:.4f}\n"
    f"Chi² = {chi_squared:.2f}\n"
    f"p-value = {p_value:.4f}"
    )
    ax.text(
    0.05, 0.95, textstr, transform=ax.transAxes, fontsize=10,
    verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.5)
    )

    x = np.linspace(0.0005,0.007,100)
    y = linear_func(x,m.values['A'],m.values['B'])
    ax.plot(x,y,label='Interpolazione')
    plt.legend()
    plt.show()
    
    
    
if __name__ == "__main__":
    main()

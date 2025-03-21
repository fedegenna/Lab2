import numpy as np
import matplotlib.pyplot as plt
from astropy.coordinates import Angle
from iminuit import Minuit
from iminuit.cost import LeastSquares
from scipy.stats import chi2

def sessagesimale_to_decimale(gradi, primi):
    # Crea un oggetto Angle utilizzando i gradi e i primi
    angolo = Angle(f'{gradi}d{primi}m')
    # Converte l'angolo in gradi decimali
    return angolo.deg
def decimale_to_sessagesimale(angolo):
    # Crea un oggetto Angle utilizzando i gradi decimali
    angolo = Angle(angolo, unit='deg')
    # Converte l'angolo in gradi e primi
    return angolo.dms


def grad_to_rad(angolo):
    return np.radians(angolo)


def coeff_rifrazione(delta_min,alpha):
    return np.sin(grad_to_rad((delta_min+alpha)/2))/np.sin(grad_to_rad(alpha/2))


def error_coeff_rifrazione(delta_min, delta_min_err, alpha, alpha_err):
    term1 = (np.cos(grad_to_rad((delta_min + alpha) / 2)) / (2 * np.sin(grad_to_rad(alpha / 2)))) * delta_min_err
    term2 = ((np.cos(grad_to_rad((delta_min + alpha) / 2)) / (2 * np.sin(grad_to_rad(alpha / 2)))) - 
             (np.sin(grad_to_rad((delta_min + alpha) / 2)) * np.cos(grad_to_rad(alpha / 2)) / 
              (2 * np.sin(grad_to_rad(alpha / 2))**2))) * alpha_err
    return np.sqrt(term1**2 + term2**2)
def func_mod1(lenght,A,B):
    return A + B/(pow(lenght,2))

def funcmod2(lenght,A,B,C):
    return A + B/(pow(lenght,2)) + C/(pow(lenght,4))

def main(): #programma che quantifica la relazione tra linghezza d'onda ed indice di rifrazione, intepolando per ottenere i coefficenti di Cauchy
    #angoli iniziali:
    Theta_iniz = sessagesimale_to_decimale(199,34)
    Theta_iniz_err = sessagesimale_to_decimale(0,1)
    alpha = sessagesimale_to_decimale(59,30)
    alpha_err =  sessagesimale_to_decimale(0,1)
    
    lambdas = [407, 434, 480, 546, 615] #ossia viola,blu,azzurro,verde,arancione su cui poniamo errore nullo
    
    #prime misure degli angoli per ogni colore(3) e statistiche:
    delta_viola = [sessagesimale_to_decimale(156,29),sessagesimale_to_decimale(156,31),sessagesimale_to_decimale(156,26)]
    delta_azzurro = [sessagesimale_to_decimale(158,28),sessagesimale_to_decimale(158,30),sessagesimale_to_decimale(158,30)]
    delta_blu = [sessagesimale_to_decimale(157,17),sessagesimale_to_decimale(157,15),sessagesimale_to_decimale(157,16)]
    delta_verde = [sessagesimale_to_decimale(159,6),sessagesimale_to_decimale(159,0),sessagesimale_to_decimale(159,7)]
    delta_arancione = [sessagesimale_to_decimale(159,35),sessagesimale_to_decimale(159,32),sessagesimale_to_decimale(159,35)]
    media_viola = np.mean(delta_viola)
    media_azzurro = np.mean(delta_azzurro)
    media_blu = np.mean(delta_blu)
    media_verde = np.mean(delta_verde)
    media_arancione = np.mean(delta_arancione)
    delta_prima_misura = [media_viola,media_blu,media_azzurro,media_verde,media_arancione]
    delta_prima_misura_err = [np.std(delta_viola)/np.sqrt(3),np.std(delta_blu)/np.sqrt(3),np.std(delta_azzurro)/np.sqrt(3),np.std(delta_verde)/np.sqrt(3),np.std(delta_arancione)/np.sqrt(3)]
    
    #misura dell'angolo rispetto a theta iniziale:
    
    delta_min = []
    for i in range(5):
        delta_min.append(abs(delta_prima_misura[i]-Theta_iniz))
    delta_sessagesimale_viola = []
    delta_sessagesimale_azzurro = []
    delta_sessagesimale_blu = []
    delta_sessagesimale_verde = []
    delta_sessagesimale_arancione = []
    for i in range(3):
        delta_sessagesimale_viola.append(decimale_to_sessagesimale(delta_viola[i]-Theta_iniz))
        delta_sessagesimale_azzurro.append(decimale_to_sessagesimale(delta_azzurro[i]-Theta_iniz))
        delta_sessagesimale_blu.append(decimale_to_sessagesimale(delta_blu[i]-Theta_iniz))
        delta_sessagesimale_verde.append(decimale_to_sessagesimale(delta_verde[i]-Theta_iniz))
        delta_sessagesimale_arancione.append(decimale_to_sessagesimale(delta_arancione[i]-Theta_iniz))
    print('Delta viola:',delta_sessagesimale_viola)
    print('Delta azzurro:',delta_sessagesimale_azzurro)
    print('Delta blu:',delta_sessagesimale_blu)
    print('Delta verde:',delta_sessagesimale_verde)
    print('Delta arancione:',delta_sessagesimale_arancione)
    def error_delta_min(delta_prima_misura_err,Theta_iniz_err):
        return np.sqrt(delta_prima_misura_err**2+Theta_iniz_err**2)
    delta_min_err = []
    for i in range(5):
        delta_min_err.append(error_delta_min(delta_prima_misura_err[i],Theta_iniz_err))
    #calcolo dei coefficienti di rifrazione e relativi errori:   
    n_rifraz = []
    for i in range(5):
        n_rifraz.append(coeff_rifrazione(delta_min[i],alpha))
    
    n_rifraz_err = []
    for i in range(5):
        n_rifraz_err.append(error_coeff_rifrazione(delta_min[i],delta_min_err[i],alpha,alpha_err))
    fig,ax = plt.subplots()
    ax.errorbar(lambdas,n_rifraz,yerr=n_rifraz_err,fmt='o',label='Dati sperimentali')
    
    plt.xlabel('Lunghezza d\'onda [nm]')
    plt.ylabel('Indice di rifrazione')
    plt.title('Indice di rifrazione in funzione della lunghezza d\'onda')
    plt.legend()
    
    
    #interpolazione per ottenere i coefficenti di Cauchy:
    my_cost_func = LeastSquares(lambdas, n_rifraz, n_rifraz_err, func_mod1)
    m = Minuit(my_cost_func, A=1, B=1000 ) 
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
    0.05, 0.25, textstr, transform=ax.transAxes, fontsize=10,
    verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.5)
    )

    x = np.linspace(400,620,100)
    y = func_mod1(x,m.values['A'],m.values['B'])
    ax.plot(x,y,label='Interpolazione',color='red',linestyle='--') 
    plt.legend()
    
    plt.savefig('prismaHg.png')
    plt.show()
    
    
    #seconda interpolazione: proviamo ad aumentare l'ordine di arresto per vedere se migliora il fit;
    my_cost_func2 = LeastSquares(lambdas, n_rifraz, n_rifraz_err, funcmod2)
    m2 = Minuit(my_cost_func2, A=1, B=1000, C=1)
    m2.migrad()
    A2 = m2.values['A']
    B2 = m2.values['B']
    C2 = m2.values['C']
    chi_squared2 = m2.fval
    p_value2 = 1 - chi2.cdf(chi_squared2,2)
    print(m2.values)
    print(m2.errors)
    print(m2.covariance)
    fig,ax = plt.subplots()
    ax.errorbar(lambdas,n_rifraz,yerr=n_rifraz_err,fmt='o',label='Dati sperimentali')
    textstr = (
    f"A = {m2.values['A']:.4f} ± {m2.errors['A']:.4f}\n"
    f"B = {m2.values['B']:.4f} ± {m2.errors['B']:.4f}\n"
    f"C = {m2.values['C']:.4f} ± {m2.errors['C']:.4f}\n"
    f"Chi² = {chi_squared2:.2f}\n"
    f"p-value = {p_value2:.4f}"
    )
    ax.text(
    0.05, 0.25, textstr, transform=ax.transAxes, fontsize=10,
    verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.5)
    )
    x = np.linspace(400,620,100)
    y = funcmod2(x,m2.values['A'],m2.values['B'],m2.values['C'])
    ax.plot(x,y,label='Interpolazione',color='red',linestyle='--')
    plt.legend()
    plt.xlabel('Lunghezza d\'onda [nm]')
    plt.ylabel('Indice di rifrazione')
    plt.title('Indice di rifrazione in funzione della lunghezza d\'onda')
    plt.show()
    
    
    
    
if __name__ == "__main__":
    main()


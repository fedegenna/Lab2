

import numpy as np
import matplotlib.pyplot as plt
from astropy.coordinates import Angle
from iminuit import Minuit
from iminuit.cost import LeastSquares

def sessagesimale_to_decimale(gradi, primi):
    # Crea un oggetto Angle utilizzando i gradi e i primi
    angolo = Angle(f'{gradi}d{primi}m')
    # Converte l'angolo in gradi decimali
    return angolo.deg


def grad_to_rad(angolo):
    return np.radians(angolo)


def coeff_rifrazione(delta_min,alpha):
    return np.sin(grad_to_rad((delta_min+alpha)/2))/np.sin(grad_to_rad(alpha/2))


def error_coeff_rifrazione(delta_min,delta_min_err,alpha,alpha_err):
    return np.sqrt(np.cos(grad_to_rad((delta_min+alpha)/2))/(2*np.sin(grad_to_rad(alpha/2))*np.sin(grad_to_rad((delta_min+alpha)/2)))*delta_min_err)**2+(np.cos(grad_to_rad((delta_min+alpha)/2))/(2*np.sin(grad_to_rad(alpha/2))*np.sin(grad_to_rad((delta_min+alpha)/2)))*alpha_err)**2

def func_mod(lambd,A,B):
    return A + B/pow(float(lambd),2)

def main():
    Theta_iniz = sessagesimale_to_decimale(203, 15)
    Theta_iniz_err = sessagesimale_to_decimale(0,1)
    alpha = sessagesimale_to_decimale(59, 30)
    alpha_err = sessagesimale_to_decimale(0,1)
    lambdas = [407, 440, 434, 546, 615] #ossia viola,indaco (azzurro),blu,verde,arancione su cui poniamo errore nullo
    
    delta_prima_misura = [sessagesimale_to_decimale(151,33),sessagesimale_to_decimale(153,30),sessagesimale_to_decimale(152,20),sessagesimale_to_decimale(146,30),sessagesimale_to_decimale(154,30)]
    #delta_prima_misura_err = [
    delta_min = []
    for i in range(5):
        delta_min.append(abs(delta_prima_misura[i]-Theta_iniz))
        
        
    n_rifraz = []
    for i in range(5):
        n_rifraz.append(coeff_rifrazione(delta_min[i],alpha))
   
    fig,ax = plt.subplots()
    ax.scatter(lambdas,n_rifraz)
    plt.grid()
    plt.show()
    '''my_cost_func = LeastSquares(lambdas, n_rifraz, errors, func_mod)
    m = Minuit(my_cost_func, A=1, B=1)
    m.migrad()
    print(m.values)
    print(m.errors)
    plt.plot(lambdas, func_mod(lambdas, *m.values), label='Fit')
    plt.show()'''
if __name__ == "__main__":
    main()

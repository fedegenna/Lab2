import numpy as np
import matplotlib.pyplot as plt
from astropy.coordinates import Angle
from iminuit import Minuit
from iminuit.cost import LeastSquares
'''alpha = Angle('60d20m')
beta = Angle('30d10m')
sum_angle = alpha + beta
print(f"Somma degli angoli: {sum_angle.to_string(unit='deg', sep='dms')}")'''
def sessagesimale_to_decimale(gradi, primi):
    # Crea un oggetto Angle utilizzando i gradi e i primi
    angolo = Angle(f'{gradi}d{primi}m')
    # Converte l'angolo in gradi decimali
    return angolo.deg
def grad_to_rad(angolo):
    return np.radians(angolo)
def coeff_rifrazione(delta_min,alpha):
    return np.sin(grad_to_rad((delta_min+alpha)/2))/np.sin(grad_to_rad(alpha/2))
def func_mod(lambd,A,B):
    return A + B/pow(float(lambd),2)
def main():
    Theta_iniz = sessagesimale_to_decimale(122, 15)
    alpha = sessagesimale_to_decimale(59, 30)
    lambdas = [410, 467.5, 542.5, 607.5, 682.5]
    delta_prim = [sessagesimale_to_decimale(73,45),sessagesimale_to_decimale(74,11),sessagesimale_to_decimale(77,35),sessagesimale_to_decimale(77,45),sessagesimale_to_decimale(85,10)]
    delta_min = []
    for i in range(5):
        delta_min.append(abs(delta_prim[i]-Theta_iniz))
    n_rifraz = []
    for i in range(5):
        n_rifraz.append(coeff_rifrazione(delta_min[i],alpha))
    errors = [coeff_rifrazione(sessagesimale_to_decimale(1,45),alpha),coeff_rifrazione(sessagesimale_to_decimale(0,55),alpha),coeff_rifrazione(sessagesimale_to_decimale(4,59),alpha),coeff_rifrazione(sessagesimale_to_decimale(4,9),alpha),coeff_rifrazione(sessagesimale_to_decimale(7,50),alpha)] 
    fig,ax = plt.subplots()
    ax.scatter(lambdas,n_rifraz)
    plt.grid()
    my_cost_func = LeastSquares(lambdas, n_rifraz, errors, func_mod)
    m = Minuit(my_cost_func, A=1, B=1)
    m.migrad()
    print(m.values)
    print(m.errors)
    plt.plot(lambdas, func_mod(lambdas, *m.values), label='Fit')
    plt.show()
main()
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


def grad_to_rad(angolo):
    return np.radians(angolo)


def coeff_rifrazione(delta_min,alpha):
    return np.sin(grad_to_rad((delta_min+alpha)/2))/np.sin(grad_to_rad(alpha/2))


def error_coeff_rifrazione(delta_min,delta_min_err,alpha,alpha_err):
    return np.sqrt(np.cos(grad_to_rad((delta_min+alpha)/2))/(2*np.sin(grad_to_rad(alpha/2))*np.sin(grad_to_rad((delta_min+alpha)/2)))*delta_min_err)**2+(np.cos(grad_to_rad((delta_min+alpha)/2))/(2*np.sin(grad_to_rad(alpha/2))*np.sin(grad_to_rad((delta_min+alpha)/2)))*alpha_err)**2

def cauchy (n,a,b):
    return np.sqrt(b/(n-a))

def error_cauchy(n,n_err,a,a_err,b,b_err):
    return np.sqrt((b_err/(2*n*np.sqrt(b/n-a)))**2+(a_err/(2*n*np.sqrt(b/n-a)))**2+(n_err*(b/n-a)**(-1.5)/2)**2)

def main():
    theta_iniz = sessagesimale_to_decimale(202, 40)
    theta_iniz_err = sessagesimale_to_decimale(0,1)
    alpha = sessagesimale_to_decimale(59, 30)
    alpha_err = sessagesimale_to_decimale(0,1)
    A = 1.5093
    
    err_A = 0.0329
    
    B = 10179.559254361111
    
    err_B = 7110.499634169746
    
    #analisi rosso:
    
    delta_misurati_rosso = [sessagesimale_to_decimale(155,10),sessagesimale_to_decimale(155,7),sessagesimale_to_decimale(155,9)]
    delta_min_rosso = abs(np.mean(delta_misurati_rosso)-theta_iniz)
    delta_rosso_err = np.std(delta_misurati_rosso)/np.sqrt(len(delta_misurati_rosso))
    def error_delta_min(delta_prima_misura_err,Theta_iniz_err):
        return np.sqrt(delta_prima_misura_err**2+Theta_iniz_err**2)
    delta_min_rosso_err = error_delta_min(delta_rosso_err,theta_iniz_err)
    coeff_rifrazione_rosso = coeff_rifrazione(delta_min_rosso,alpha)
    err_coeff_rifrazione_rosso = error_coeff_rifrazione(delta_min_rosso,delta_min_rosso_err,alpha,alpha_err)
    lambda_rosso = cauchy(coeff_rifrazione_rosso,A,B)
    err_lambda_rosso = error_cauchy(coeff_rifrazione_rosso,err_coeff_rifrazione_rosso,A,err_A,B,err_B)
    print(f'lambda rosso = {lambda_rosso} +- {err_lambda_rosso}')
    
    #analisi giallo:
    
    delta_misurati_giallo = [sessagesimale_to_decimale(154,30),sessagesimale_to_decimale(154,32),sessagesimale_to_decimale(154,30)]
    delta_min_giallo = abs(np.mean(delta_misurati_giallo)-theta_iniz)
    delta_giallo_err = np.std(delta_misurati_giallo)/np.sqrt(len(delta_misurati_giallo))
    delta_min_giallo_err = error_delta_min(delta_giallo_err,theta_iniz_err)
    coeff_rifrazione_giallo = coeff_rifrazione(delta_min_giallo,alpha)
    err_coeff_rifrazione_giallo = error_coeff_rifrazione(delta_min_giallo,delta_min_giallo_err,alpha,alpha_err)
    lambda_giallo = cauchy(coeff_rifrazione_giallo,A,B)
    err_lambda_giallo = error_cauchy(coeff_rifrazione_giallo,err_coeff_rifrazione_giallo,A,err_A,B,err_B)
    print(f'lambda giallo = {lambda_giallo} +- {err_lambda_giallo}')
    
    #analisi verde:
    
    delta_misurati_verde = [sessagesimale_to_decimale(154,0),sessagesimale_to_decimale(154,2),sessagesimale_to_decimale(153,59)]
    delta_min_verde = abs(np.mean(delta_misurati_verde)-theta_iniz)
    delta_verde_err = np.std(delta_misurati_verde)/np.sqrt(len(delta_misurati_verde))
    delta_min_verde_err = error_delta_min(delta_verde_err,theta_iniz_err)
    coeff_rifrazione_verde = coeff_rifrazione(delta_min_verde,alpha)
    err_coeff_rifrazione_verde = error_coeff_rifrazione(delta_min_verde,delta_min_verde_err,alpha,alpha_err)
    lambda_verde = cauchy(coeff_rifrazione_verde,A,B)   
    err_lambda_verde = error_cauchy(coeff_rifrazione_verde,err_coeff_rifrazione_verde,A,err_A,B,err_B)
    print(f'lambda verde = {lambda_verde} +- {err_lambda_verde}')
    
    #analisi azzurro:
    
    delta_misurati_azzurro = [sessagesimale_to_decimale(153,30),sessagesimale_to_decimale(153,36),sessagesimale_to_decimale(153,29)]
    delta_min_azzurro = abs(np.mean(delta_misurati_azzurro)-theta_iniz)
    delta_azzurro_err = np.std(delta_misurati_azzurro)/np.sqrt(len(delta_misurati_azzurro))
    delta_min_azzurro_err = error_delta_min(delta_azzurro_err,theta_iniz_err)
    coeff_rifrazione_azzurro = coeff_rifrazione(delta_min_azzurro,alpha)
    err_coeff_rifrazione_azzurro = error_coeff_rifrazione(delta_min_azzurro,delta_min_azzurro_err,alpha,alpha_err)
    lambda_azzurro = cauchy(coeff_rifrazione_azzurro,A,B)
    err_lambda_azzurro = error_cauchy(coeff_rifrazione_azzurro,err_coeff_rifrazione_azzurro,A,err_A,B,err_B)
    print(f'lambda azzurro = {lambda_azzurro} +- {err_lambda_azzurro}')
    
    #analisi viola:
    
    delta_misurati_viola = [sessagesimale_to_decimale(153,3),sessagesimale_to_decimale(153,1),sessagesimale_to_decimale(153,2)]
    delta_min_viola = abs(np.mean(delta_misurati_viola)-theta_iniz)
    delta_viola_err = np.std(delta_misurati_viola)/np.sqrt(len(delta_misurati_viola))
    delta_min_viola_err = error_delta_min(delta_viola_err,theta_iniz_err)
    coeff_rifrazione_viola = coeff_rifrazione(delta_min_viola,alpha)
    err_coeff_rifrazione_viola = error_coeff_rifrazione(delta_min_viola,delta_min_viola_err,alpha,alpha_err)
    lambda_viola = cauchy(coeff_rifrazione_viola,A,B)
    err_lambda_viola = error_cauchy(coeff_rifrazione_viola,err_coeff_rifrazione_viola,A,err_A,B,err_B)
    print(f'lambda viola = {lambda_viola} +- {err_lambda_viola}')
    
    
    
if __name__ == '__main__':
    main()
    
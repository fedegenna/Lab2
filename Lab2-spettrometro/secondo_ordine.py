import math

def gradi_primi_a_radianti(gradi, primi):
    """
    Converte un angolo dato in gradi e primi in radianti.

    :param gradi: Parte intera dell'angolo in gradi.
    :param primi: Parte frazionaria dell'angolo in primi (1 grado = 60 primi).
    :return: Angolo in radianti.
    """
    angolo_in_gradi = gradi + primi / 60
    angolo_in_radianti = math.radians(angolo_in_gradi)
    return angolo_in_radianti

import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

def disegna_grafico_con_errori(ascissa, ordinata, errori_ordinate, titolo="Grafico con Errori", xlabel="Ascissa", ylabel="Ordinata"):
    """
    Disegna un grafico con una lista in ascissa, una in ordinata e le bande di errore per le ordinate.
    Disegna anche la retta y=2, calcola il coefficiente k nell'interpolazione lineare dei dati con y=k,
    il suo errore e il valore t=|k-2|/errore_k.

    :param ascissa: Lista dei valori da mettere in ascissa.
    :param ordinata: Lista dei valori da mettere in ordinata.
    :param errori_ordinate: Lista degli errori associati ai valori delle ordinate.
    :param titolo: Titolo del grafico (opzionale).
    :param xlabel: Etichetta dell'asse x (opzionale).
    :param ylabel: Etichetta dell'asse y (opzionale).
    """
    if len(ascissa) != len(ordinata) or len(ordinata) != len(errori_ordinate):
        raise ValueError("Le liste ascissa, ordinata ed errori_ordinate devono avere la stessa lunghezza.")
    
    # Disegna i dati con errori
    plt.errorbar(ascissa, ordinata, yerr=errori_ordinate, fmt='o', ecolor='red', capsize=5, label="Dati con errori")
    
    # Disegna la retta y=2
    plt.axhline(y=2, color='blue', linestyle='--', label="y=2")
    
    # Calcolo del coefficiente k (interpolazione lineare con y=k)
    k = np.mean(ordinata)  # Media dei valori di ordinata come stima di k
    errore_k = np.std(ordinata) / np.sqrt(len(ordinata))  # Errore standard della media
    
    # Calcolo di t = |k - 2| / errore_k
    if errore_k != 0:  # Controllo per evitare divisione per zero
        t = abs(k - 2) / errore_k
    else:
        t = float('inf')  # Se errore_k è zero, t diventa infinito
    
    # Disegna la retta y=k
    plt.axhline(y=k, color='green', linestyle='-', label=f"y=k (k={k:.2f} ± {errore_k:.2f})")
    
    # Configurazione del grafico
    plt.title(titolo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # Stampa i risultati di k, del suo errore e di t
    print(f"Coefficiente k: {k:.2f} ± {errore_k:.2f}")
    print(f"Valore di t: {t:.2f}")

def rapporto_seni(lista1, lista2):
    """
    Calcola il rapporto tra il seno degli elementi corrispondenti di due liste.

    :param lista1: Prima lista di valori (in radianti).
    :param lista2: Seconda lista di valori (in radianti).
    :return: Lista contenente il rapporto sin(lista1[i]) / sin(lista2[i]) per ogni i.
    """
    if len(lista1) != len(lista2):
        raise ValueError("Le due liste devono avere la stessa lunghezza.")
    
    return [math.sin(x) / math.sin(y) if math.sin(y) != 0 else float('inf') for x, y in zip(lista1, lista2)]

def errore_rapporto_seni(lista1, lista2, errori1, errori2):
    """
    Calcola l'errore sul rapporto tra il seno degli elementi corrispondenti di due liste.

    :param lista1: Prima lista di valori (in radianti).
    :param lista2: Seconda lista di valori (in radianti).
    :param errori1: Incertezze associate ai valori della prima lista.
    :param errori2: Incertezze associate ai valori della seconda lista.
    :return: Lista contenente l'errore sul rapporto sin(lista1[i]) / sin(lista2[i]) per ogni i.
    """
    if len(lista1) != len(lista2) or len(lista1) != len(errori1) or len(lista1) != len(errori2):
        raise ValueError("Le liste e i relativi errori devono avere la stessa lunghezza.")
    
    return [math.sqrt((math.cos(x) / math.sin(x) * errori1[i])**2 + (math.cos(y) / math.sin(y) * errori2[i])**2) if math.sin(y) != 0 else float('inf') for i, (x, y) in enumerate(zip(lista1, lista2))]

def main () :
   
    lista_primo_ordine = [gradi_primi_a_radianti(10, 37), gradi_primi_a_radianti(10, 5), gradi_primi_a_radianti(10, 0), gradi_primi_a_radianti(8, 40)]
    lista_secondo_ordine = [gradi_primi_a_radianti(22, 0), gradi_primi_a_radianti(21, 0), gradi_primi_a_radianti(20, 7), gradi_primi_a_radianti(17, 39)]

    rapporto = rapporto_seni(lista_secondo_ordine, lista_primo_ordine)
    print(rapporto)

    errori_primo_ordine = [gradi_primi_a_radianti(0, 2.35), gradi_primi_a_radianti(0, 2.83), gradi_primi_a_radianti(0, 2.83), gradi_primi_a_radianti(0, 2.35)]
    errori_secondo_ordine = [gradi_primi_a_radianti(0, 2.83), gradi_primi_a_radianti(0, 2.35), gradi_primi_a_radianti(0, 2.35), gradi_primi_a_radianti(0, 2.83)]

    errore_rapporto = errore_rapporto_seni(lista_secondo_ordine, lista_primo_ordine, errori_secondo_ordine, errori_primo_ordine)
    print(errore_rapporto)

    lambdas = [615, 588.9, 568.8, 514.9]

    disegna_grafico_con_errori(lambdas, rapporto, errore_rapporto, titolo="Rapporto tra seni", xlabel="Lunghezza d'onda [nm]", ylabel="Rapporto tra seni")




if __name__ == "__main__":
    main()

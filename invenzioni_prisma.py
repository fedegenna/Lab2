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

def radianti_a_gradi_primi(radianti):
    """
    Converte un angolo dato in radianti in gradi e primi.

    :param radianti: Angolo in radianti.
    :return: Una tupla (gradi, primi) dove:
             - gradi è la parte intera dell'angolo in gradi.
             - primi è la parte frazionaria dell'angolo in primi (1 grado = 60 primi).
    """
    angolo_in_gradi = math.degrees(radianti)
    gradi = int(angolo_in_gradi)  # Parte intera in gradi
    primi = (angolo_in_gradi - gradi) * 60  # Parte frazionaria in primi
    return gradi, primi

def delta_inventato(delta0, alpha, lambda_, a, b):
    """
    Calcola il valore di delta inventato secondo la formula:
    delta0 + alpha - 2 * arcsin[(a + b / lambda**2) * sin(alpha / 2)]

    :param delta0: Angolo iniziale (in radianti).
    :param alpha: Angolo alpha (in radianti).
    :param lambda_: Lunghezza d'onda (stessa unità di a e b).
    :param a: Coefficiente a.
    :param b: Coefficiente b.
    :return: Valore calcolato di delta inventato.
    """
    term = (a + b / lambda_**2) * math.sin(alpha / 2)
    delta = delta0 + alpha - 2 * math.asin(term)
    return delta

def main () :
    delta0 = gradi_primi_a_radianti(199, 34)
    alpha = gradi_primi_a_radianti(59, 30)
    lambdas = [633, 575, 540, 480, 436] #rosso, giallo, verde, azzurro, viola
    a = 1.73
    b = 13420
    angoli = []
    for lambda_ in lambdas:
        delta = delta_inventato(delta0, alpha, lambda_, a, b)
        delta = radianti_a_gradi_primi(delta)
        angoli.append(delta)
    
    print(angoli)
if __name__ == "__main__":
    main()

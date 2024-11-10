
import numpy as np
import math
import matplotlib.pyplot as plt
from sympy import Symbol, sin, cos, tan, log, sqrt, sympify

def dichotomie(f, a, b, precision, nmax):
    """
    Méthode de dichotomie pour trouver une solution à l'équation f(x) = 0.

    Args:
        f (function): La fonction à résoudre.
        a (float): La borne inférieure de l'intervalle de recherche.
        b (float): La borne supérieure de l'intervalle de recherche.
        precision (float): La précision souhaitée pour la solution.
        nmax (int): Le nombre maximum d'itérations.

    Returns:
        float: La solution à l'équation f(x) = 0.
    """
    # Initialiser les variables
    Xg = a
    Xd = b
    sol = 0

    # Vérification des conditions initiales
    if f(a) * f(b) > 0:
        raise ValueError("f(a) et f(b) sont de même signe, donc impossible d'utiliser TVI")

    # Boucle jusqu'à ce que la précision soit atteinte ou que le nombre maximal d'itérations soit atteint
    niter = 0
    while abs(Xd - Xg) > precision and niter < nmax:
        Xm = (Xg + Xd) / 2
        if f(Xg) * f(Xm) < 0:
            Xd = Xm
        else:
            Xg = Xm
        niter += 1

    sol = (Xg + Xd) / 2
    return sol

def get_user_function():
    """
    Demande à l'utilisateur de saisir une fonction et la valide.
    """
    while True:
        try:
            print("Exemples de fonctions :")
            print(" - Logarithmique : 'np.log(x) + x**2 - 4'")
            print(" - Racine carrée : 'np.sqrt(x) - 2'")
            print(" - Usuelle : 'x**3 - x**2 + x - 1'")
            print(" - Trigonométriques : 'np.sin(x)', 'np.cos(x)', 'np.tan(x)'")
            print(" - Logarithme naturel (ln) : 'np.log(x)'")

            func_str = input("Entrez la fonction f(x) en termes de 'x' : ")

            def f(x):
                if ('np.log' in func_str or 'np.log10' in func_str or 'math.log' in func_str) and x <= 0:
                    raise ValueError("Le logarithme n'est défini que pour les valeurs positives.")
                elif 'np.sqrt' in func_str and x < 0:
                    raise ValueError("La racine carrée n'est définie que pour les valeurs positives ou nulles.")
                elif ('np.sin' in func_str or 'np.cos' in func_str or 'np.tan' in func_str or
                      'math.sin' in func_str or 'math.cos' in func_str or 'math.tan' in func_str) and not isinstance(x, (int, float)):
                    raise ValueError("Les fonctions trigonométriques nécessitent une valeur numérique.")
                return eval(func_str, {"np": np, "math": math, "x": x, "__builtins__": {}})

            # Tester la fonction pour s'assurer qu'elle est valide
            f(1)
            break
        except Exception as e:
            print(f"Erreur dans la fonction : {e}. Veuillez réessayer.")
    return f

def main():
    while True:
        # Obtention de la fonction définie par l'utilisateur
        user_function = get_user_function()

        # Paramètres
        while True:
            try:
                a = float(input("Entrez la borne inférieure a : "))
                print(type(a))
                break
            except ValueError:
                print("Veuillez entrer un nombre réel valide pour a.")
        while True:
            try:
                b = float(input("Entrez la borne supérieure b : "))
                if b <= a:
                    raise ValueError("La borne supérieure doit être supérieure à la borne inférieure.")
                break
            except ValueError as e:
                print(f"Erreur : {e}. Veuillez entrer un nombre réel valide pour b.")

        while True:
            try:
                precision = float(input("Entrez la précision : "))
                break
            except ValueError:
                print("Veuillez entrer un nombre réel valide pour la précision.")

        while True:
            try:
                nmax = int(input("Entrez le nombre maximum d'itérations : "))
                break
            except ValueError:
                print("Veuillez entrer un nombre entier valide pour le nombre maximum d'itérations.")

        # Calcule de la solution
        try:
            solution = dichotomie(user_function, a, b, precision, nmax)
            print("La solution est :", solution)
        except ValueError as e:
            print(f"Erreur lors du calcul de la solution : {e}. Veuillez vérifier vos bornes et réessayer.")
            continue

        # Demander à l'utilisateur s'il veut recommencer
        retry = input("Voulez-vous recommencer? (oui/non) : ").strip().lower()
        if retry != 'oui':
            break

if __name__ == "__main__":
    main()
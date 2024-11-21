import numpy as np
import sympy as sp
import math
import matplotlib.pyplot as plt


def balayage(f, a, pas, distance):
    """
    Méthode de balayage pour trouver l'intervalle contenant la racine de f(x) = 0.
    Args:
        f (function): La fonction dont on cherche la racine.
        a (float): La borne inférieure de la plage de recherche.
        pas (float): La taille de chaque intervalle pour le balayage.
        distance (float): La distance totale de balayage à partir de la borne inférieure.
    Returns:
        list: Liste des intervalles où la fonction change de signe.
    """
    intervalles = []
    b = a + distance
    x = a
    while x < b:
        if f(x) * f(x + pas) < 0:
            intervalles.append((x, x + pas))
        x += pas
    return intervalles


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
            print(" - Exponentielle: 'np.exp(x) - 2' ")

            func_str = input("Entrez la fonction f(x) en termes de 'x' : ")

            def f(x):
                if ('np.log' in func_str or 'np.log10' in func_str or 'math.log' in func_str) and x <= 0:
                    raise ValueError("Le logarithme n'est défini que pour les valeurs positives.")
                elif 'np.sqrt' in func_str and x < 0:
                    raise ValueError("La racine carrée n'est définie que pour les valeurs positives ou nulles.")
                elif ('np.sin' in func_str or 'np.cos' in func_str or 'np.tan' in func_str or
                      'math.sin' in func_str or 'math.cos' in func_str or 'math.tan' in func_str) and not isinstance(x,
                                                                                                                     (
                                                                                                                     int,
                                                                                                                     float)):
                    raise ValueError("Les fonctions trigonométriques nécessitent une valeur numérique.")
                elif 'np.exp' in func_str and not isinstance(x, (int, float)):
                    raise ValueError("La fonction exponentielle nécessite une valeur numérique.")
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
                break
            except ValueError:
                print("Veuillez entrer un nombre réel valide pour a.")

        while True:
            try:
                pas = float(input("Entrez la taille du pas de balayage : "))
                break
            except ValueError:
                print("Veuillez entrer un nombre réel positif pour la taille du pas de balayage.")

        while True:
            try:
                distance = float(input("Entrez la distance de balayage : "))
                break
            except ValueError:
                print("Veuillez entrer un nombre réel positif pour la distance de balayage.")

        # Recherche des intervalles
        intervalles = balayage(user_function, a, pas, distance)
        if intervalles:
            print("Les intervalles où la fonction change de signe sont :")
            for intervalle in intervalles:
                print(intervalle)
        else:
            print("Aucun changement de signe détecté dans l'intervalle donné.")

        # Demander à l'utilisateur s'il veut recommencer
        retry = input("Voulez-vous recommencer? (oui/non) : ").strip().lower()
        if retry != 'oui':
            break


if __name__ == "__main__":
    main()

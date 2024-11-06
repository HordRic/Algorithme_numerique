# Importation des bibliothèques nécessaires
import numpy as np
import math
import matplotlib.pyplot as plt

# Définition de la fonction à approcher
def masecante(f, a, b, epsilon, nmax):
    x0 = a
    x1 = b
    niter = 0
    infoconvergence = 0
    while abs(f(x1)) > epsilon and niter < nmax:
        z = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))  # Calculer x_n+1
        # mise à jour des 2 points successifs x0 et x1
        x0 = x1  # jouera le rôle de x_n au prochain coup
        x1 = z  # jouera le rôle de x_n+1$   # incrémentation du nombre d'itérations
        niter += 1
    # convergence ou pas
    if niter == nmax:
        print('Nombre de convergence atteint, pas de convergence')
    else:
        print('Convergence OK avec epsilon')
        infoconvergence = 1
    return x1, niter, infoconvergence

# Exemple d'utilisation avec saisie utilisateur
def get_user_function():
    while True:
        try:
            print("Exemples de fonctions :")
            print(" - Logarithmique : 'np.log(x) + x**2 - 4'")
            print(" - Racine carrée : 'np.sqrt(x) - 2'")
            print(" - Usuelle : 'x**3 - x**2 + x - 1'")
            print(" - Trigonométriques : 'np.sin(x)', 'np.cos(x)', 'np.tan(x)'")
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
        # Obtenir la fonction définie par l'utilisateur
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
                b = float(input("Entrez la borne supérieure b : "))
                if b <= a:
                    raise ValueError("La borne supérieure doit être supérieure à la borne inférieure.")
                break
            except ValueError as e:
                print(f"Erreur : {e}. Veuillez entrer un nombre réel valide pour b.")
                
        while True:
            try:
                epsilon = float(input("Entrez la précision epsilon : "))
                break
            except ValueError:
                print("Veuillez entrer un nombre réel valide pour la précision.")
                
        while True:
            try:
                nmax = int(input("Entrez le nombre maximum d'itérations : "))
                break
            except ValueError:
                print("Veuillez entrer un nombre entier valide pour le nombre maximum d'itérations.")

        # Calculer la solution
        try:
            solution, niter, infoconvergence = masecante(user_function, a, b, epsilon, nmax)
            if infoconvergence:
                print("La solution est :", solution)
                print("Nombre d'itérations :", niter)
            else:
                print("La méthode n'a pas convergé.")
        except ValueError as e:
            print(f"Erreur lors du calcul de la solution : {e}. Veuillez vérifier vos bornes et réessayer.")
            continue

        # Demander à l'utilisateur s'il veut recommencer
        retry = input("Voulez-vous recommencer avec une autre fonction? (oui/non) : ").strip().lower()
        if retry != 'oui':
            break

if __name__ == "__main__":
    main()

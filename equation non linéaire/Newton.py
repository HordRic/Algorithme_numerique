# Importation des bibliothèques nécessaires
import numpy as np
import math
import matplotlib.pyplot as plt

# Définition de la méthode de Newton
def meth_newton(f, fprime, xzero, epsilon, nmaxit):
    niter = 0  # compteur d'itération initialisation
    info_conv = 0  # info si convergence ou pas (0 = pas de cv et 1 = conv ok)
    x = xzero  # point courant du calcul
    while abs(f(x)) > epsilon and niter < nmaxit:
        niter += 1
        try:
            x = x - f(x) / fprime(x)  # Formule xn+1 = xn - f(xn)/f'(xn)
        except ZeroDivisionError:
            print("Division par zéro détectée. Ajustez votre fonction dérivée.")
            return x, niter, info_conv
        if abs(f(x)) < epsilon:
            info_conv = 1
            print('Convergence OK avec epsilon')
            break
    if niter == nmaxit:
        print('Nombre d\'itérations maximum atteint, pas de convergence')
    return x, niter, info_conv

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
            func_prime_str = input("Entrez la dérivée f'(x) en termes de 'x' : ")
            
            def f(x):
                if ('np.log' in func_str or 'np.log10' in func_str or 'math.log' in func_str) and x <= 0:
                    raise ValueError("Le logarithme n'est défini que pour les valeurs positives.")
                elif 'np.sqrt' in func_str and x < 0:
                    raise ValueError("La racine carrée n'est définie que pour les valeurs positives ou nulles.")
                elif ('np.sin' in func_str or 'np.cos' in func_str or 'np.tan' in func_str or 
                      'math.sin' in func_str or 'math.cos' in func_str or 'math.tan' in func_str) and not isinstance(x, (int, float)):
                    raise ValueError("Les fonctions trigonométriques nécessitent une valeur numérique.")
                return eval(func_str, {"np": np, "math": math, "x": x, "__builtins__": {}})
            
            def fprime(x):
                return eval(func_prime_str, {"np": np, "math": math, "x": x, "__builtins__": {}})
            
            # Tester les fonctions pour s'assurer qu'elles sont valides
            f(1)
            fprime(1)
            break
        except Exception as e:
            print(f"Erreur dans la fonction : {e}. Veuillez réessayer.")
    return f, fprime

def main():
    while True:
        # Obtenir les fonctions définies par l'utilisateur
        user_function, user_function_prime = get_user_function()

        # Paramètres
        while True:
            try:
                xzero = float(input("Entrez la valeur initiale x0 : "))
                break
            except ValueError:
                print("Veuillez entrer un nombre réel valide pour x0.")
                
        while True:
            try:
                epsilon = float(input("Entrez la précision epsilon : "))
                if epsilon <= 0:
                    raise ValueError("La précision epsilon doit être supérieure à 0.")
                break
            except ValueError as e:
                print(f"Erreur : {e}. Veuillez entrer un nombre réel valide pour la précision.")
                
        while True:
            try:
                nmaxit = int(input("Entrez le nombre maximum d'itérations : "))
                if nmaxit <= 0:
                    raise ValueError("Le nombre maximum d'itérations doit être supérieur à 0.")
                break
            except ValueError as e:
                print(f"Erreur : {e}. Veuillez entrer un nombre entier valide pour le nombre maximum d'itérations.")

        # Calculer la solution
        try:
            solution, niter, info_conv = meth_newton(user_function, user_function_prime, xzero, epsilon, nmaxit)
            if info_conv:
                print("La solution est :", solution)
                print("Nombre d'itérations :", niter)
            else:
                print("La méthode n'a pas convergé.")
        except ValueError as e:
            print(f"Erreur lors du calcul de la solution : {e}. Veuillez vérifier vos données et réessayer.")
            continue

        # Demander à l'utilisateur s'il veut recommencer
        retry = input("Voulez-vous recommencer avec une autre fonction? (oui/non) : ").strip().lower()
        if retry != 'oui':
            break

if __name__ == "__main__":
    main()

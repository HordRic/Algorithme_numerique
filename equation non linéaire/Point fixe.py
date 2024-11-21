import numpy as np
import math
import matplotlib.pyplot as plt


def point_fixe(f, g, x0, tol, max_iter):
    """
    Méthode du point fixe pour résoudre l'équation f(x) = 0.
    Args:
        f (function): La fonction dont on cherche les racines.
        g (function): La fonction d'itération associée.
        x0 (float): La valeur initiale.
        tol (float): La tolérance.
        max_iter (int): Le nombre maximal d'itérations.
    Returns:
        float: La solution approximative, ou None si la convergence n'est pas atteinte.
    """
    x = x0
    iterations = []
    for i in range(max_iter):
        x_nouveau = g(x)
        iterations.append(x_nouveau)
        if abs(x_nouveau - x) < tol:
            plot_iterations(iterations)
            return x_nouveau
        x = x_nouveau
    return None


def plot_iterations(iterations):
    """
    Trace les points intermédiaires de la méthode du point fixe.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(iterations, marker='o')
    plt.title("Convergence de la méthode du point fixe")
    plt.xlabel("Itérations")
    plt.ylabel("Valeur de x")
    plt.grid(True)
    plt.show()


def get_user_functions():
    """
    Demande à l'utilisateur de saisir les fonctions f(x) et g(x).
    """
    while True:
        try:
            func_f_str = input("Entrez la fonction f(x) en termes de 'x' : ")
            func_g_str = input("Entrez la fonction g(x) en termes de 'x' : ")

            def f(x):
                return eval(func_f_str, {'__builtins__': None, 'np': np, 'math': math, 'x': x})

            def g(x):
                return eval(func_g_str, {'__builtins__': None, 'np': np, 'math': math, 'x': x})

            break
        except Exception as e:
            print(f"Erreur dans les fonctions : {e}. Veuillez réessayer.")
    return f, g


def main():
    while True:
        # Obtention des fonctions définies par l'utilisateur
        f, g = get_user_functions()

        # Paramètres
        while True:
            try:
                x0 = float(input("Entrez la valeur initiale x0 : "))
                break
            except ValueError:
                print("Veuillez entrer un nombre réel valide pour x0.")

        while True:
            try:
                tol = float(input("Entrez la tolérance : "))
                break
            except ValueError:
                print("Veuillez entrer un nombre réel positif pour la tolérance.")

        while True:
            try:
                max_iter = int(input("Entrez le nombre maximum d'itérations : "))
                break
            except ValueError:
                print("Veuillez entrer un nombre entier positif pour le nombre maximum d'itérations.")

        # Calcul de la solution
        try:
            solution = point_fixe(f, g, x0, tol, max_iter)
            if solution is not None:
                print("La solution est :", solution)
            else:
                print("La méthode n'a pas convergé.")
        except Exception as e:
            print(f"Erreur lors du calcul de la solution : {e}. Veuillez vérifier vos paramètres et réessayer.")
            continue

        # Demander à l'utilisateur s'il veut recommencer
        retry = input("Voulez-vous recommencer? (oui/non) : ").strip().lower()
        if retry != 'oui':
            break


if __name__ == "__main__":
    main()

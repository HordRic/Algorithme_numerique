import numpy as np

def gauss_seidel(A, b, x0, tol, max_iter):
    """
    Résoudre le système d'équations linéaires Ax = b en utilisant la méthode de Gauss-Seidel.
    Args:
        A (numpy.ndarray): Matrice des coefficients.
        b (numpy.ndarray): Vecteur des constantes.
        x0 (numpy.ndarray): Vecteur initial.
        tol (float): Tolérance pour la convergence.
        max_iter (int): Nombre maximal d'itérations.
    Returns:
        numpy.ndarray: Vecteur solution x.
    """
    n = len(b)
    x = x0.copy()
    for k in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            s1 = sum(A[i, j] * x_new[j] for j in range(i))
            s2 = sum(A[i, j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new
        x = x_new
    raise RuntimeError("La méthode de Gauss-Seidel n'a pas convergé après le nombre maximal d'itérations")

def get_user_input():
    """
    Demande à l'utilisateur de saisir la matrice A, le vecteur b, le vecteur initial x0, la tolérance et le nombre maximal d'itérations.
    """
    while True:
        try:
            n = int(input("Entrez la taille de la matrice carrée A (n x n) : "))
            if n <= 0:
                raise ValueError("La taille de la matrice doit être un entier positif.")
            break
        except ValueError as e:
            print(f"Erreur : {e}. Veuillez réessayer.")

    A = np.zeros((n, n))
    b = np.zeros(n)
    x0 = np.zeros(n)

    print("Entrez les éléments de la matrice A :")
    for i in range(n):
        for j in range(n):
            while True:
                try:
                    A[i, j] = float(input(f"A[{i}][{j}] = "))
                    break
                except ValueError:
                    print("Veuillez entrer un nombre réel valide.")

    print("Entrez les éléments du vecteur b :")
    for i in range(n):
        while True:
            try:
                b[i] = float(input(f"b[{i}] = "))
                break
            except ValueError:
                print("Veuillez entrer un nombre réel valide.")

    print("Entrez les éléments du vecteur initial x0 :")
    for i in range(n):
        while True:
            try:
                x0[i] = float(input(f"x0[{i}] = "))
                break
            except ValueError:
                print("Veuillez entrer un nombre réel valide.")

    while True:
        try:
            tol = float(input("Entrez la tolérance : "))
            if tol <= 0:
                raise ValueError("La tolérance doit être un nombre positif.")
            break
        except ValueError as e:
            print(f"Erreur : {e}. Veuillez entrer un nombre réel positif pour la tolérance.")

    while True:
        try:
            max_iter = int(input("Entrez le nombre maximal d'itérations : "))
            if max_iter <= 0:
                raise ValueError("Le nombre maximal d'itérations doit être un entier positif.")
            break
        except ValueError as e:
            print(f"Erreur : {e}. Veuillez entrer un nombre entier positif pour le nombre maximal d'itérations.")

    return A, b, x0, tol, max_iter

def main():
    while True:
        A, b, x0, tol, max_iter = get_user_input()
        try:
            solution = gauss_seidel(A, b, x0, tol, max_iter)
            print("La solution est :", solution)
        except RuntimeError as e:
            print(f"Erreur lors du calcul de la solution : {e}. Veuillez vérifier vos paramètres et réessayer.")
            continue

        retry = input("Voulez-vous recommencer? (oui/non) : ").strip().lower()
        if retry != 'oui':
            break

if __name__ == "__main__":
    main()
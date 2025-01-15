import numpy as np
from scipy.linalg import cholesky

def cholesky_decomposition(A, b):
    """
    Résout le système d'équations linéaires Ax = b en utilisant la décomposition de Cholesky.
    Args:
        A (numpy.ndarray): Matrice des coefficients.
        b (numpy.ndarray): Vecteur des constantes.
    Returns:
        numpy.ndarray: Vecteur solution x.
    """
    try:
        L = cholesky(A, lower=True)
        y = np.linalg.solve(L, b)
        x = np.linalg.solve(L.T, y)
        return x
    except Exception as e:
        raise RuntimeError(f"Erreur lors de la décomposition de Cholesky : {e}")

def get_user_input():
    """
    Demande à l'utilisateur de saisir la matrice A et le vecteur b.
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

    return A, b

def main():
    while True:
        A, b = get_user_input()
        try:
            solution = cholesky_decomposition(A, b)
            print("La solution est :", solution)
        except RuntimeError as e:
            print(f"Erreur lors du calcul de la solution : {e}. Veuillez vérifier vos paramètres et réessayer.")
            continue

        retry = input("Voulez-vous recommencer? (oui/non) : ").strip().lower()
        if retry != 'oui':
            break

if __name__ == "__main__":
    main()
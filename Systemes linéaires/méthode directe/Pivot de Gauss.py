import numpy as np


def pivot_gauss(A, b):
    """
    Résout le système d'équations linéaires Ax = b en utilisant l'algorithme du pivot de Gauss.
    Args:
        A (numpy.ndarray): Matrice des coefficients.
        b (numpy.ndarray): Vecteur des constantes.
    Returns:
        numpy.ndarray: Vecteur solution x.
    """
    n = len(b)
    # Augmenter la matrice A avec le vecteur b
    Ab = np.hstack([A, b.reshape(-1, 1)])

    try:
        # Appliquer l'élimination de Gauss
        for i in range(n):
            # Recherche du pivot
            max_row = np.argmax(np.abs(Ab[i:, i])) + i
            # Échange des lignes
            Ab[[i, max_row]] = Ab[[max_row, i]]

            # Vérifier si le pivot est nul
            if Ab[i, i] == 0:
                raise ValueError(
                    f"Pivot nul rencontré à la ligne {i}. Le système peut être singulier ou mal conditionné.")

            # Élimination
            for j in range(i + 1, n):
                ratio = Ab[j, i] / Ab[i, i]
                Ab[j, i:] -= ratio * Ab[i, i:]

        # Résolution par substitution arrière
        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            x[i] = (Ab[i, -1] - np.dot(Ab[i, i + 1:n], x[i + 1:n])) / Ab[i, i]

        return x
    except Exception as e:
        raise RuntimeError(f"Erreur lors de l'élimination de Gauss : {e}")


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
            solution = pivot_gauss(A, b)
            print("La solution est :", solution)
        except RuntimeError as e:
            print(f"Erreur lors du calcul de la solution : {e}. Veuillez vérifier vos paramètres et réessayer.")
            continue

        retry = input("Voulez-vous recommencer? (oui/non) : ").strip().lower()
        if retry != 'oui':
            break


if __name__ == "__main__":
    main()
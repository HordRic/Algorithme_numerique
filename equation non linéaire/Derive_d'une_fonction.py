import sympy as sp
import math

def derivee_symbolique(expr):
    """
    Calcule la dérivée symbolique de l'expression donnée.
    Args:
        expr (sympy.Expr): L'expression dont on veut la dérivée.
    Returns:
        sympy.Expr: La dérivée symbolique de l'expression.
    """
    x = sp.symbols('x')
    deriv = sp.diff(expr, x)
    return deriv


def get_user_function():
    """
    Demande à l'utilisateur de saisir une fonction et la valide.
    """
    while True:
        try:
            print("Exemples de fonctions :")
            print(" - Logarithmique : 'log(x) + x**2 - 4'")
            print(" - Racine carrée : 'sqrt(x) - 2'")
            print(" - Usuelle : 'x**3 - x**2 + x - 1'")
            print(" - Trigonométriques : 'sin(x)', 'cos(x)', 'tan(x)'")
            print(" - Exponentielle: 'exp(x) - 2' ")

            func_str = input("Entrez la fonction f(x) en termes de 'x' : ")
            x = sp.symbols('x')
            expr = sp.sympify(func_str)
            break
        except Exception as e:
            print(f"Erreur dans la fonction : {e}. Veuillez réessayer.")
    return expr


def main():
    while True:
        # Obtention de la fonction définie par l'utilisateur
        user_expr = get_user_function()

        # Calcul de la dérivée symbolique
        try:
            deriv = derivee_symbolique(user_expr)
            print(f"La dérivée de la fonction est : {deriv}")
        except Exception as e:
            print(f"Erreur lors du calcul de la dérivée : {e}. Veuillez vérifier vos paramètres et réessayer.")
            continue

        # Demander à l'utilisateur s'il veut recommencer
        retry = input("Voulez-vous recommencer? (oui/non) : ").strip().lower()
        if retry != 'oui':
            break


if __name__ == "__main__":
    main()

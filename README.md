Voici le README mis à jour pour inclure les nouvelles méthodes que vous avez ajoutées :

# AlgorithmeNumerique

## Description

Cette librairie de code en Python implémente des algorithmes numériques, notamment les méthodes de Dichotomie, de Newton, de la Sécante, ainsi que plusieurs méthodes pour résoudre des systèmes d'équations linéaires. Elle est conçue pour aider toutes les personnes qui ont des difficultés dans l'élaboration des algorithmes numériques à trouver un bon algorithme.

- **Procurer un déblocage et continuer son propre code** en se référant juste aux multiples codes présents ici.
- **Aller plus rapidement avec des moyens de bord.**
- **Lire les ressources et comprendre son code de fond en comble.**

## Algorithmes Inclus

### Méthodes pour les Équations Non Linéaires

#### 1. Méthode de Dichotomie
La méthode de Dichotomie est utilisée pour trouver une racine d'une fonction continue en utilisant un intervalle [a, b] et en divisant cet intervalle jusqu'à atteindre une précision donnée.

#### 2. Méthode de Newton
La méthode de Newton, également connue sous le nom de méthode de Newton-Raphson, est un algorithme itératif pour trouver les zéros d'une fonction différentiable.

#### 3. Méthode de la Sécante
La méthode de la Sécante est une méthode itérative pour résoudre des équations non linéaires, similaire à la méthode de Newton mais sans nécessiter la dérivée de la fonction.

### Méthodes pour les Systèmes d'Équations Linéaires

#### 1. Méthode de Gauss avec Pivot
Cette méthode résout le système d'équations linéaires en utilisant l'élimination de Gauss avec pivot pour éviter les erreurs numériques dues aux pivots nuls ou petits.

#### 2. Méthode de Gauss sans Pivot
Cette méthode résout le système d'équations linéaires en utilisant l'élimination de Gauss sans pivot.

#### 3. Décomposition LU
Cette méthode décompose la matrice \(A\) en deux matrices triangulaires \(L\) et \(U\), puis résout le système en deux étapes de substitution.

#### 4. Décomposition de Cholesky
Cette méthode décompose la matrice \(A\) en une matrice triangulaire inférieure \(L\) et sa transposée \(L^T\), puis résout le système en deux étapes de substitution.

#### 5. Méthode de Jacobi
Cette méthode résout le système d'équations linéaires par une série d'itérations successives jusqu'à ce que la solution converge à une tolérance spécifiée.

#### 6. Méthode de Gauss-Seidel
Cette méthode résout le système d'équations linéaires par une série d'itérations successives, en utilisant les valeurs mises à jour dès qu'elles sont disponibles.

## Utilisation

### 1. Choix de la Méthode

L'utilisateur peut choisir parmi les méthodes de Dichotomie, Newton, Sécante, Gauss avec Pivot, Gauss sans Pivot, Décomposition LU, Décomposition de Cholesky, Jacobi, et Gauss-Seidel pour résoudre une équation non linéaire ou un système d'équations linéaires. Les entrées de l'utilisateur sont vérifiées pour assurer la validité et la précision des calculs.

### 2. Exemples de Fonctions

Voici quelques exemples de fonctions que vous pouvez utiliser :
- Logarithmique : 

np.log(x) + x**2 - 4


- Racine carrée : 

np.sqrt(x) - 2


- Usuelle : 

x**3 - x**2 + x - 1


- Trigonométriques : 

np.sin(x)

, 

np.cos(x)

, 

np.tan(x)



### 3. Exemples de Matrices

Voici quelques exemples de matrices que vous pouvez utiliser pour vérifier les méthodes de résolution des systèmes d'équations linéaires :

#### Décomposition de Cholesky
```python
A = np.array([
    [4, 1, 1],
    [1, 3, 1],
    [1, 1, 2]
], dtype=float)
b = np.array([1, 2, 3], dtype=float)
```

#### Décomposition LU
```python
A = np.array([
    [3, 1, 6],
    [2, 1, 3],
    [1, 1, 1]
], dtype=float)
b = np.array([12, 7, 3], dtype=float)
```

## Disclaimer of Warranty

IL N'Y A PAS DE GARANTIE POUR LE PROGRAMME, DANS LA MESURE PERMISE PAR LA LOI APPLICABLE. LE RISQUE ENTIER CONCERNANT LA QUALITÉ ET LES PERFORMANCES DU PROGRAMME VOUS INCOMBE. SI LE PROGRAMME S'AVÈRE DÉFECTUEUX, VOUS ASSUMEZ LE COÛT DE TOUS LES SERVICES, RÉPARATIONS OU CORRECTIONS NÉCESSAIRES. L'ENTRETIEN, LA RÉPARATION OU LA CORRECTION NÉCESSAIRES SONT BIENVENUES.

---

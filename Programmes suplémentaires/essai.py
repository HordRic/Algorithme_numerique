import random
import time

def sort_analysis(A):
    count = 0
    n = len(A)
    for i in range(1, n):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            count += 1
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = v
    return count

sizes = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500]
results = []

print("Début de l'exécution")

for size in sizes:
    print(f"Traitement de la taille: {size}")
    total_time = 0
    for _ in range(20):
        A = [random.randint(0, 10000) for _ in range(size)]
        start_time = time.time()
        sort_analysis(A)
        end_time = time.time()
        total_time += (end_time - start_time) * 1000  # Convert to milliseconds
    average_time = total_time / 20
    results.append((size, average_time))
    print(f"Taille: {size}, Temps moyen (ms): {average_time}")

print("Résultats:")
for size, avg_time in results:
    print(f"Taille: {size}, Temps moyen (ms): {avg_time}")

print("Fin de l'exécution")
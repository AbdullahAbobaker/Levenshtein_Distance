import matplotlib.pyplot as plt
import numpy as np


def levenshtein_distance(s1, s2, del_cost, ins_cost, sub_cost):
    matrix = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    for j in range(1, len(s2) + 1):
        matrix[0][j] = j * ins_cost

    for i in range(1, len(s1) + 1):
        matrix[i][0] = i * del_cost

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):

            if s1[i - 1] == s2[j - 1]:
                cost_sub = 0
            else:
                cost_sub = sub_cost

            matrix[i][j] = min(
                matrix[i - 1][j] + del_cost,  # Deletion
                matrix[i][j - 1] + ins_cost,  # Insertion
                matrix[i - 1][j - 1] + cost_sub  # Substitution
            )

    # The Levenshtein distance is the value in the bottom-right cell
    return matrix[len(s1)][len(s2)]

# Testing
# del_cost=0.5 , ins_cost=0.5 und sub_cost=0.5
s1 = "Maschinelles Lernen"
s2 = "Machine Learning"
s3 = "Vorlesung Maschinelles Lernen"


print("del_cost=0.5 , ins_cost=0.5 und sub_cost=0.5 \n")
print("First String: " + s1 + " // " + "Second String: " + s2 + " --> Min Cost is: " + str(
    levenshtein_distance(s1, s2, 0.5, 0.5, 0.5)))
print("First String: " + s1 + " // " + "Second String: " + s3 + " --> Min Cost is: " + str(
    levenshtein_distance(s1, s3, 0.5, 0.5, 0.5)))
print("First String: " + s2 + " // " + "Second String: " + s3 + " --> Min Cost is: " + str(
    levenshtein_distance(s2, s3, 0.5, 0.5, 0.5)))
print("\n")
# del_cost=2 , ins_cost=0.5 und sub_cost=0.5
print("del_cost=2 , ins_cost=0.5 und sub_cost=0.5 \n")
print("First String: " + s1 + " // " + "Second String: " + s2 + " --> Min Cost is: " + str(
    levenshtein_distance(s1, s2, 2, 0.5, 0.5)))
print("First String: " + s1 + " // " + "Second String: " + s3 + " --> Min Cost is: " + str(
    levenshtein_distance(s1, s3, 2, 0.5, 0.5)))
print("First String: " + s2 + " // " + "Second String: " + s3 + " --> Min Cost is: " + str(
    levenshtein_distance(s2, s3, 2, 0.5, 0.5)))
print("\n")
# del_cost=0.5 , ins_cost=0.5 und sub_cost=2
print("del_cost=0.5 , ins_cost=0.5 und sub_cost=2 \n")
print("First String: " + s1 + " // " + "Second String: " + s2 + " --> Min Cost is: " + str(
    levenshtein_distance(s1, s2, 0.5, 0.5, 2)))
print("First String: " + s1 + " // " + "Second String: " + s3 + " --> Min Cost is: " + str(
    levenshtein_distance(s1, s3, 0.5, 0.5, 2)))
print("First String: " + s2 + " // " + "Second String: " + s3 + " --> Min Cost is: " + str(
    levenshtein_distance(s2, s3, 0.5, 0.5, 2)))
print("\n")


# c) Erweitern Sie die Funktion aus a) um einen Parameter `return_matrix=False`. Wenn dieser auf `True` gesetzt ist, soll die Funktion die Editier-Distanz-Matrix zurückliefern.
# Berechnen Sie die Matrix und visualisieren Sie diese mithilfe von `matplotlib` für `s1='Maschinelles Lernen'`, `s2='Machine Learning'` mit `del_cost=0.5`, `ins_cost=0.5` und `sub_cost=0.5`.


def levenshtein_distance2(s1, s2, del_cost, ins_cost, sub_cost, return_matrix):
    matrix = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    for j in range(1, len(s2) + 1):
        matrix[0][j] = j * ins_cost

    for i in range(1, len(s1) + 1):
        matrix[i][0] = i * del_cost

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            # If characters match, cost is 0 for substitution
            if s1[i - 1] == s2[j - 1]:
                cost_sub = 0
            else:
                cost_sub = sub_cost

            # Calculate minimum cost
            matrix[i][j] = min(
                matrix[i - 1][j] + del_cost,  # Deletion
                matrix[i][j - 1] + ins_cost,  # Insertion
                matrix[i - 1][j - 1] + cost_sub  # Substitution
            )

    if return_matrix:
        return matrix
    else:
        return matrix[len(s1)][len(s2)]


matrix = levenshtein_distance2(s1, s2, 1, 1, 1, True)

# Beispielnutzung
s1 = 'Maschinelles Lernen'
s2 = 'Machine Learning'
del_cost = 0.5
ins_cost = 0.5
sub_cost = 0.5

distance_matrix = levenshtein_distance2(s1, s2, del_cost, ins_cost, sub_cost, return_matrix=True)

plt.figure(figsize=(10, 8))
plt.imshow(distance_matrix, cmap='Blues')
plt.title(f'Levenshtein-Distanz-Matrix\n(del_cost={del_cost}, ins_cost={ins_cost}, sub_cost={sub_cost})')
plt.xlabel('s2: "Machine Learning"')
plt.ylabel('s1: "Maschinelles Lernen"')

for i in range(len(s1) + 1):
    for j in range(len(s2) + 1):
        text = f"{distance_matrix[i][j]:.1f}"
        color = "white" if distance_matrix[i][j] > 5 else "black"
        plt.text(j, i, text, ha="center", va="center", color=color)

plt.xticks(range(len(s2)), list(s2))
plt.yticks(range(len(s1)), list(s1))
plt.colorbar()
plt.show()

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
# L = [5, 3, 8, 1]
# L = [1, 2, 3, 4]


def my_sort(L):
    taille = 0
    coup = 0
    for loop in L:
        taille = taille + 1

    for i in range(taille):
        for j in range(i + 1, taille):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]
                coup += 1
    print(f"Nombre total de coups nécessaires pour trier la liste {coup}")
    print(f"liste triée : {L}")


my_sort(L)

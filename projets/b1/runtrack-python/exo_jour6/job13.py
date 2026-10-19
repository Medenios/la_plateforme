L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]


def elimine(L):
    taille = 0
    for loop in L:
        taille = taille + 1

        for i in range(taille):
            for j in range(i + 1, taille):
                if L[i] > L[j]:
                    L[i], L[j] = L[j], L[i]

    return L


print(elimine(L))
# print(set(L))

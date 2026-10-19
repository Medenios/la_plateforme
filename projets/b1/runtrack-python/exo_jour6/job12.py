L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
# L = ["a", "z", "t", "b"]


def tri(l):
    taille = 0
    for loop in l:
        taille = taille + 1

    for i in range(taille):
        for j in range(i + 1, taille):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]

    return L


print(tri(L))

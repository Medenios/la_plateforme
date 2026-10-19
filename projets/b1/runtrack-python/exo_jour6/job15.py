L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

for i in range(len(L)):
    L[i] = int(L[i])


def tri(liste):
    taille = 1
    for loop in liste:
        taille += 1

    loop1 = False
    while loop1 == False:
        loop1 = True
        i = 0
        while i < taille - 1:
            if liste[i] > liste[i + 1]:
                temp = liste[i]
                liste[i] = liste[i + 1]
                liste[i + 1] = temp
                loop1 = False
            i += 1

    return liste


print(tri(L))

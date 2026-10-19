chaine = "abcdefghijklmnopqrstuvwxyz" * 10

taille_ligne = 1

while taille_ligne <= len(chaine):
    ligne = ""
    i = 0
    while i < taille_ligne:
        ligne = ligne + chaine[i]
        i += 1
    print(ligne)
    taille_ligne = taille_ligne + 2

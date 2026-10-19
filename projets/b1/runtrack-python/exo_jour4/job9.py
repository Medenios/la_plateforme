#!/usr/bin/env python3

note1 = float(input("entrez la 1er note : "))
note2 = float(input("entrez la 2eme note : "))
note3 = float(input("entrez la 3eme note : "))


def Moyenne(note1, note2, note3):
    moyenne = (note1 + note2 + note3) / 3
    return moyenne


moyenne_etudiant = int(Moyenne(note1, note2, note3))

print("la moyenne de l'étudiant: ", moyenne_etudiant)

# if moyenne_etudiant <= 20 and moyenne_etudiant >= 15:
#     print("Tres bon élève")
# elif moyenne_etudiant < 15 and moyenne_etudiant >= 11:
#     print("Bon élève")
# elif moyenne_etudiant < 11 and moyenne_etudiant >= 8:
#     print("Eleve moyen")
# else:
#     print("Eleve devant faire des efforts")

match moyenne_etudiant:
    case m if 15 <= m <= 20:
        print("Très bon élève")
    case m if 11 <= m < 15:
        print("Bon élève")
    case m if 8 <= m < 11:
        print("Élève moyen")
    case _:
        print("Élève devant faire des efforts")

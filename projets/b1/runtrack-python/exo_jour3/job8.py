a = int(input("entrez la longeur a : "))
b = int(input("entrez la longeur b : "))
c = int(input("entrez la longeur c : "))

if a >= b and a >= c:
    grand_cote = a
    petit_cote1 = b
    petit_cote2 = c
elif b >= a and b >= c:
    grand_cote = b
    petit_cote1 = a
    petit_cote2 = c
else:
    grand_cote = c
    petit_cote1 = a
    petit_cote2 = b

if grand_cote >= petit_cote1 + petit_cote2:
    print("Impossible d'avoir un triangle avec ces segments")

if a == b and b == c:
    print("le triangle est équilatéral")
elif (petit_cote1**2 + petit_cote2**2 == grand_cote**2) and (
    a == b or b == c or a == c
):
    print("le triangle est rectangle et isocèle")
elif petit_cote1**2 + petit_cote2**2 == grand_cote**2:
    print("le triangle est rectangle")
elif a == b or b == c or a == c:
    print("le triangle est isocèle")
else:
    print("le triangle est quelconque")

def signe(nombre):
    if nombre > 0:
        return "positif"
    elif nombre < 0:
        return "negatif"
    else:
        return "nul"


print(signe(5))
print(signe(-4))
print(signe(0))

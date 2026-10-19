def parite(nombre):
    if nombre > 0 and isinstance(nombre, int):
        if nombre % 2 == 0:
            return "le nombre est pair"
        else:
            return "le nombre est impair"
    else:
        print("votre nombre ne convient pas ou n'en n'est pas un")


print(parite(4))
print(parite(-5))

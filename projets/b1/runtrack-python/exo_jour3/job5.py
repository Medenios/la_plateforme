for nombre in range(2, 1001):
    nombre_premier = True
    for diviseur in range(2, nombre):
        if nombre % diviseur == 0:
            nombre_premier = False
            break
    if nombre_premier:
        print(nombre, end=" ")

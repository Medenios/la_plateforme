def tapis(n):
    print("+" + "-" * (n + 1) + "+")
    for ligne in range(n + 1):
        espaces_avant = "#" * (n - ligne)
        espaces_apres = "#" * ligne
        print("|" + espaces_avant + " " + espaces_apres + "|")
    print("+" + "-" * (n + 1) + "+")


tapis(10)

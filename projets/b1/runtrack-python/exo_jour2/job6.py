i = 0
number = int(input("entrez votre entier : "))
while i < 11:
    print(f"7 * {i} = {7 * i}")
    i = i + 1
    if i == number:
        break

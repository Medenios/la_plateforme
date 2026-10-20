def tapis(n):
    chaine = n * "#" + " "
    return chaine


def draw_rectangle(n):
    hauteurTotale = n + 1
    for y in range(hauteurTotale):
        if y == 0 or y == hauteurTotale - 1:
            print(f"+{'-' * hauteurTotale}+")
        else:
            print(f"|{tapis(n)}|")


draw_rectangle(10)
tapis(10)
print()

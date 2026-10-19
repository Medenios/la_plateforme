while True:
    n = int(input("entrez un entier superieur à 0 (N) :"))
    if n > 1:
        break

for loop1 in range(n):
    print("Table de multiplication de ", loop1 + 1, ":")
    for loop in range(11):
        print(loop1 + 1, " x ", loop, " = ", (loop1 + 1) * loop)
    print()

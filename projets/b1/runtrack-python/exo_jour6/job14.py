def my_long_word(num, chaine):
    wordlist = []
    wordlist1 = []
    word = ""
    for i in range(len(chaine)):
        if chaine[i] != " " and chaine[i] != ",":
            word += chaine[i]
        else:
            wordlist.append(word)
            word = ""

    for i in range(len(wordlist)):
        if len(wordlist[i]) > num:
            wordlist1.append(wordlist[i])

    print(wordlist1)


machaine = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
longueur = 3

my_long_word(longueur, machaine)

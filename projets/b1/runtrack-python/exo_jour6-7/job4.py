def cesar(message, decalage):
    resultat = ""
    for caractere in message.lower():

        if "a" <= caractere <= "z":
            position = ord(caractere) - 97
            nouvelle_position = (position + decalage) % 26
            resultat = resultat + chr(nouvelle_position + 97)
        else:
            resultat = resultat + caractere

    return resultat


print(cesar("Bonjour", 3))
print(cesar("xyz", 3))
print(cesar("abc", -3))

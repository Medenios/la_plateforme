def jardin(type, saison):
    if type == "fruits" and saison == "hiver":
        return "orange, mandarine et kiwi"
    elif type == "fruits" and saison == "été":
        return "Poire, fraise et cassis"
    elif type == "légumes" and saison == "hiver":
        return "carotte, topinambour, endive"
    else:
        return "artichaut, aubergine,navet"


print(jardin("fruits", "été"))

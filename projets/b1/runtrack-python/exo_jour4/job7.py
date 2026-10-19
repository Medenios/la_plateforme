def dev(langage):
    match langage:
        case "Javascript":
            return "tu es un developpeur web"
        case "python":
            return "tu es un developpeur IA"
        case "java":
            return "tu es un developpeur logiciel"
        case "react":
            return "tu es un developpeur mobile"
        case _:
            return "un jour, je serai le meilleur développeur..."


print(dev("Javascript"))
print(dev("java"))
print(dev(""))

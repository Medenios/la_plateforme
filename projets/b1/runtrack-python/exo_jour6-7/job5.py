def toilettes(nb_marche, hauteur_marche):

    total_semaine = nb_marche * (hauteur_marche / 100) * 2 * 5 * 7

    print(
        f"Pour {nb_marche} marches de {hauteur_marche} cm, le gardien parcourt {total_semaine:.2f} m par semaine."
    )


toilettes(100, 20)
toilettes(50, 17.21)

def time_to_text(nombre):
    heures = nombre // 60
    minutes = nombre % 60
    print(heures, "heures et ", minutes, "minutes")


time_to_text(150)

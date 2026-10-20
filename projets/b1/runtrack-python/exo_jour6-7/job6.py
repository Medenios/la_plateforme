def arrondir_notes(notes):
    liste_notes = []
    for note in notes:
        if note < 40:
            nouvelle_note = note
        else:
            ecart = 5 - note % 5
            if ecart < 3:
                nouvelle_note = note + ecart
            else:
                nouvelle_note = note
        liste_notes.append(nouvelle_note)
    return liste_notes


print(arrondir_notes([73, 67, 38, 33]))
print(arrondir_notes([83, 82, 85, 40, 39, 99]))

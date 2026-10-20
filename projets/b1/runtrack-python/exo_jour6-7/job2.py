def triangle(height):
    for i in range(1, height + 1):
        vide = " " * (height - i)
        if i < height:
            wide = " " * (2 * (i - 1))
        else:
            wide = "_" * (2 * (i - 1))
        print(vide + "/" + wide + "\\")


triangle(5)

def triangle(height):
    offset = height * 2
    for x in range(height):
        wide = (x * 2) - 2
        if x == 0:
            print((offset - x) * " ", "/\\", sep="")
        elif x < height - 1:
            print((offset - x) * " ", "/", wide * " ", "\\", sep="")
        else:
            print((offset - x) * " ", "/", wide * "_", "\\", sep="")


triangle(5)

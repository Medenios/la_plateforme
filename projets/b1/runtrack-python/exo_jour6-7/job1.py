def draw_rectangle(width, height):
    for y in range(height):
        if y == 0 or y == height - 1:
            print(f"|{(width-2) * "-"}|")
        else:
            print(f"|{(width-2) * " "}|")


draw_rectangle(10, 3)
print()

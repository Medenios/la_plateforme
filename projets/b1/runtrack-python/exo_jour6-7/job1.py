def draw_rectangle(width, height):
    for y in range(height):
        if y == 0 or y == height - 1:
            print(f"|{width * "-"}|")
        else:
            print(f"|{width * " "}|")


draw_rectangle(12, 8)
print()

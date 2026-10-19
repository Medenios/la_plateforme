for loop in range(1, 101):
    if loop % 3 == 0 and loop % 5 == 0:
        print("fizzbuzz", end=" ")
        continue
    elif loop % 3 == 0:
        print("fizz", end=" ")
    elif loop % 5 == 0:
        print("buzz", end=" ")
    else:
        print(loop, end=" ")

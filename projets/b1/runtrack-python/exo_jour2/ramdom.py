import random

coup = 1
random_number = random.randint(1, 100)
print(random_number)
while True:
    your_choice = int(input("entrez un nombre entre 1 et 100 : "))
    if coup < 5:
        if random_number != your_choice:
            coup += 1
        else:
            print("vous avez gagné")
            break
        print("vous avez perdu")

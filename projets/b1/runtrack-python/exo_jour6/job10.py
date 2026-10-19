L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
sum = 1

for i in range(len(L)):
    if L[i] >= 25 <= L[i] <= 90:
        sum *= L[i]

print(sum)

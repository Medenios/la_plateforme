L = [8, 24, 48, 2, 16]

# mul = 0
# for i in range(len(L)):
#    if L[i] % 3 == 0:
#        mul += 1

# print(mul)

count = sum(1 for x in L if x % 3 == 0)
print(count)

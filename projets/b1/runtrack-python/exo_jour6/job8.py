L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
# sum = 0

# for i in range(len(L)):
#    if L[i] % 2 == 0:
#        sum += L[i]

sum(x for x in L if x % 2 == 0)

print(sum(x for x in L if x % 2 == 0))

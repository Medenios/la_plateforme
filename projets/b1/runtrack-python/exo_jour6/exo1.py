prenom = ["christophe", "simon", "masha"]
# print(prenom[1])

christophe = 1
simon = True
masha = "test"

list = [christophe, simon, masha]

# for i in range(3):
#    print(list[i])

i = 0
while i < len(list):
    print(list[i])
    i += 1

list1 = {"christophe": 1, "simon": True, "masha": "toto"}

print(list1["masha"])

list2 = [prenom, list, list1]

print(list2[1][1])

L1=[5,7,8,5,6]
print(L1)
print(L1[4])
L1[3]=17
L1[3]=L1[2]+L1[4]
print(L1[-1])
print("la liste horizentalement")
print(L1)
print("la liste verticalement")
for i in range(len(L1)):
    print(L1[i])
print("la liste inversee")
L1.reverse()
print("la liste verticalement inversee")
for i in range(len(L1)):
    print(L1[i])
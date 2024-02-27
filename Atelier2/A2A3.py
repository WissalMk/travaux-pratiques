L3=[8,93,6,7,26]
print(L3)
for i in L3 :
    print(i)
print("la somme est ", sum(L3))
for i in L3:
    p=p*i
print("le produit des vals dont l'indice compris entre 2 et 4 est ", p)
print("la valeur max de L3 est ", max(L3))
print("la valeur min de L3 est ", min(L3))
c=0
for i in L3:
    if(i%3==0):
        c=c+1
print("il y en a",c,"multiples de 3" )



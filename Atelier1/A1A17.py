n=int(input("donner le niveau de votre pyramide "))
for i in range(0,n,1):
    for j in range(i+1,0,-1):
        print(j,end=" ")
    print()
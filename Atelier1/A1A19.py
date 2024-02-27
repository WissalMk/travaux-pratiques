n = int(input("donner le niveau de votre pyramide "))
"""for i in range(n+1, 0, -1):
    for j in range(i, 0, -1):
        print("*", end=" ")
    print()
for i in range(1, n+1, 1):
    for j in range(0,i, 1):
        print("*", end=" ")
    print()
"""
## sol youssra
"""
m=n
l=0
for i in range((n+1)//2):
    print(" "*l,end="")
    print("* "*m,end="")
    m-=2
    l+=1
    print()
m-=4
l+=2
for i in range(n//2):
    print(" "*l,end="")
    print("* "*m,end="")
    m-=2
    l+=1
    print()






###n=int(input("donner le niveau de votre pyramide "))
"""
"""
lhbal diali k
for i in range (n,0,-1):
    print(str("*")*((i)//2))
    print(str(' ')*((n)-i),end=" ")
for i in range (0,n):
    print(str(' ')*((n+1)-i),end=" ")
    print(str("*")*((i-1)*2))"""

###n=int(input("donner le niveau de votre pyramide "))

##for i in range(n,0,-1):
 ##   print(" "*(n-i)+"*"*i)


etoile='*'
for i in range(0,n):
    print(" "*(n-i)+etoile)
    etoile += '**'

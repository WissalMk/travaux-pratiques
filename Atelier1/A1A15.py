##n=int(input("donner le niveau de votre pyramide "))
"""r=0
for i in range(1,n):
    r=r+i
    e=r
    for j in range(1,i+1):
        print(e," ",end=" ")
        e=e-1
    print()
n=int(input("donner le niveau du pyramide"))
for i in range(0,n):
    for j in range(0,i):
        for k in range(1,)
"""
"""k=1
for i in range(0,n):
    for j in range(i,0,-1):
        print(k,end=" ")
        k = k + 1
    print()
"""
### sol manal
"""
i=1
k=1
j=0
while i<11:
    l=i
    for j in range(k):
        print(l-j,end=" ")
    print()
    k=k+1
    i=i+k
#methode2_qst supp
"""
"""
n=int(input("Donner le niveau de votre pyramide"))
i=1
k=0
j=0
while i<=n:
    l=i
    for j in range(k+1):
        print(l+j,end=" ")
    print()
    k=k+1
    i=i+k
"""
n=int(input("taille : "))

for i in range(0,n):
    for j in range(0,n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j or j==n-i-1 :
            print("* ",end="")
        else :
            print("  ",end="")
    print("")


n=int(input("taille : "))

for i in range(0,n):
    for j in range(0,n*2):
        if i+j>n and i+j<n*2 :
            print("* ",end="")
        else :
            print("  ",end="")
            print("")
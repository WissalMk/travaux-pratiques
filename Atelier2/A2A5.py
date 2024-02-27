def F1(arg):
    for i in range(5):
        print(arg)
arg= input(("donner votre mot "))
F1(arg)
def F2(n):
    if(n%10==0):
        print(n,"est divisible par 10")
    else:
        print(n,"n'est pas divisible par 10 :(")
F2(25)
def F4(n):
    if(n==0):
        return 1
    else:
        return (n*F4(n-1))
print("le fact de 4 est ",F4(4))
def F3(l):
    c=0
    for i in l :
        if(i=='a'or i=='e' or i=='i' or i=='u' or i=='o' or i=='y'):
            c=c+1
    return c
print("le nombre de voy dans le mot hello est",F3("hello"))

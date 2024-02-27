t1=[31,28,31,30,31,30,31,31,30,31,30,31]
t2=["Janvier","Fevrier","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Decembre",]

for i in range(1,len(t2)+1):
    t2.insert((i*2)-1,t1[i-1])
print(t2)
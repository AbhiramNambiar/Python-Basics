x=[6,2,4,15,12]
s=len(x)
for i in range(0,(len(x)-1),1):
    for j in range(0,s-1,1):
        if(x[j]>x[j+1]):
            c=x[j+1]
            x[j+1]=x[j]
            x[j]=c
        s=s-1     
print(x)
x=[13,11,6,12,5]
for i in range(1,len(x),1):
    key=x[i]
    j=i-1
    while(j>=0 and x[j]>key):
        x[j+1]=x[j]
        j-=1
    x[j+1]=key

print(x)    
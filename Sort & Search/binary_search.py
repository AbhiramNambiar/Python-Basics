x=[2,14,25,32,46]
s=0
e=len(x)
mid=0
y=int(input("Enter the element to be searched:"))
while(s<=e):
    mid=(s+e)//2
    if(y==x[mid]):
        print("The element is present at position ",mid)
        break
    elif(y<x[mid]):
        e=mid-1
    else:
        s=mid+1
print("Number not found")

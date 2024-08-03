x=int(input("No of shots made by the player:"))
print("Enter the Distances")
d=[]
for i in range(0,x,1):
    dis=int(input("Distance:"))
    d.append(dis)
size=int(input("size of subarray:"))
    
print(d)
subarr=[]
i=x
sum=[]
for j in range(0,x-1,1):
    subarr=d[j:j+2:1]
    print(subarr)
    

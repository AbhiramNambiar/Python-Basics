def previousmaller(arr):
    n=len(arr)
    s=[-1]
    ans=[0]*n
    for i in range(0,n):
        curr=arr[i]
        while(s[-1]!=-1 and s[-1]>curr):
            s.pop()
            
        ans[i]=s[-1]
            
        s.append(curr)
            
    return ans
        
x=[4,5,25,7,8,6]
        
print(previousmaller(x))
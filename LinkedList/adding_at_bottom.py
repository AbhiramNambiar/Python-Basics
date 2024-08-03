class stack:
    def __init__(self):
        self.l=[]
    def retrn(self):
        return self.l
    def push(self,element):
        self.l.append(element)
        return self.l
    def pop(self):
        self.l.pop()
        return self.l
    def top(self):
        return self.l[-1]
s1=stack()
s2=[]
n=int(input("No.of elements:"))
n1=n
for i in range(0,n,1):
    x=int(input("Element:"))
    s1.push(x)
    s2.append(x)
print(s2)
while (n>0):
    s1.pop()
    n=n-1
s1.push(int(input("Number to be added:")))
for i in range(0,n1,1):
    s1.push(s2[i])
print("after adding:",s1.retrn())

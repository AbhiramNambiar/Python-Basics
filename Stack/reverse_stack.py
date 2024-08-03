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
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
len=len(s1.retrn())
s2=stack()
s2.retrn()
while (len>0):
    ele=s1.top()
    s1.pop()
    len=len-1
    s2.push(ele)   
print(s2.retrn())

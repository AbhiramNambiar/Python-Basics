class stack:
    def __init__(self):
        self.l=[]
        
    def push(self,element):
        self.l.append(element)
    def pop(self):
        self.l.pop()
    def top(self):
        return self.l[-1]
    def prin(self):
        print(self.l)
    
s=stack()
s.push(4)
s.push(12)
s.prin()
print(s.top())


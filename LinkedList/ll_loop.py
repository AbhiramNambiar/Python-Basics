class node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=node(1)
f=node(2)
s=node(3)
p=node(4)
head.next=f
f.next=s
s.next=p
q=node(5)
p.next=q
q.next=s
sp=head
fp=head
i=0
while(head!=None):
    sp=sp.next
    fp=fp.next.next
    i=i+1
    if(sp.data==fp.data):
        break
print("loop present at :",i)

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=node(21)
f=node(21)
s=node(46)
p=node(52)
q=node(52)
r=node(63)
u=node(63)
head.next=f
f.next=s
s.next=p
p.next=q
q.next=r
r.next=u
temp=head
while(head!=None):
    print(head.data)
    head=head.next 
head=temp
while(head!=None):
    if(head.data==head.next.data):
        head.next=head.next.next
    head=head.next
print("After sort")
head=temp
while(head!=None):
    print(head.data)
    head=head.next

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=node(32)
f=node(21)
s=node(46)
p=node(46)
q=node(52)
r=node(52)
u=node(24)
head.next=f
f.next=s
s.next=p
p.next=q
q.next=r
r.next=u
temp=head
temp1=head
i=0
while head!=None:
    head=head.next
    i+=1
    
head=temp

for i in range(0,i,1):
    while (head!=None):
        if(head.next is not None and (head.data)>(head.next.data)):
            data1=head.next.data
            head.next.data=head.data
            head.data=data1
        head=head.next
    head=temp1
    i-=1
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
  
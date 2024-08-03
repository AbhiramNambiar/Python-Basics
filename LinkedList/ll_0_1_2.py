class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
head=Node(1)
S=Node(0)
F=Node(2)
T=Node(1)
head.next=S
S.next=F
F.next=T

temp=head
c1=0
c2=0
c0=0
while(temp!=None):
    if(temp.data==2):
        c2+=1
    elif(temp.data==1):
        c1+=1
    else:
        c0+=1
    temp=temp.next

temp1=head
while(temp1!=None):
    if(c0!=0):
        temp1.data=0
        c0-=1
    elif(c1!=0):
        temp1.data=1
        c1-=1
    elif(c2!=0):
        temp1.data=2
        c2-=1
        
    temp1=temp1.next

while(head!=None):
    print(head.data)
    head=head.next



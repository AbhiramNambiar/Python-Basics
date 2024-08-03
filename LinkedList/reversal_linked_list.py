class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
head=Node(1)
S=Node(2)
F=Node(3)
T=Node(4)
head.next=S
S.next=F
F.next=T
curr=head
prev=None
while(curr!=None):
    nxt=curr.next
    curr.next=prev
    prev=curr
    curr=nxt
    
head=prev
while(head!=None):
    print(head.data)
    head=head.next

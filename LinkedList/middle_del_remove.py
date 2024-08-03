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
temp=head
i=0
while temp!=None:
    temp=temp.next
    i+=1

mid=(i+1)//2
i=1
temp=head
while i<mid:
    temp=temp.next
    i+=1
    
middle=temp.data
print(middle)

temp=head
while temp.next.data!=middle:
    temp=temp.next

temp.next=temp.next.next


while temp!=None:
    print(temp.data)
    temp=temp.next

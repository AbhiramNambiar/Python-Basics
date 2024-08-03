class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def addnode(data,head):
    temp=head
    while(temp.next!=None):
        temp=temp.next    
    temp.next=Node(data)
    return head
    
        
head=Node(1)
head=addnode(2,head)
head=addnode(3,head)


while head!=None:
    print(head.data)
    head=head.next
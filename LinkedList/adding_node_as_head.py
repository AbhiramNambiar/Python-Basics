class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def addnode(data,head):
    newnode=Node(data)
    newnode.next=head
    head=newnode
    return head
    
        
head=Node(1)
head=addnode(2,head)

while head!=None:
    print(head.data)
    head=head.next
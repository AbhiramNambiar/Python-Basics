class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
def addnode(data,head):
    newnode=node(data)
    newnode.next=head
    newnode.prev=None
    head=newnode
    return head
def endnode(data,head):
    temp=head
    while(temp.next!=None):
        temp=temp.next    
    temp.next=node(data)
    return head
    
        
head=node(1)
a=node(2)
b=node(3)
head.next=a
a.next=b
b.prev=a
a.prev=head
head1=addnode(4,head)
head1=endnode(4, head1)

while(head1!=None):
    print(head1.data)
    head1=head1.next



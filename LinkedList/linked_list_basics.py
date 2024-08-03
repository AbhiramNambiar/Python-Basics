class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    
        
head=Node(1)
S=Node(2)
head.next=S

while head!=None:
    print(head.data)
    head=head.next
    


class node:
    def __init__(self,data):
        self.data=data
        self.next_N=None
        self.prev=None
class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def append(self,data):
        new_node=node(data)
        if self.head==None:
            self.head=self.tail=new_node
            self.head.prev=None
            self.tail.next_N=None
        else:
            self.tail.next_N=new_node
            new_node.prev=self.tail
            self.tail=new_node
            self.tail.next_N=None
    def middle(self,data,pos):
        new_node=node(data)
        if self.head==None:
            self.head=self.tail=new_node
            self.head.prev=None
            self.tail.next_N=None
        else:
            curr=self.head
            for i in range(1,pos):
                curr=curr.next_N
            last=curr.next_N
            last.prev=curr
            curr.next_N=new_node
            new_node_prev=curr
            new_node.next_N=last
            last.prev=new_node
    def display(self):
        curr=self.head
        while curr:
            print(curr.data,sep="->")
            curr=curr.next_N
my=linkedlist()
my.append(2)
my.append(6)
my.middle(7,1)
my.append(7)
my.middle(10,2)
my.append(1)
my.display()
    
    
        

class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=node()
    def append(self,data):
        new_node=node(data)
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node
    def middle(self,pos,data):
        c=0
        curr=self.head
        while True:
            last=curr
            curr=curr.next
            if c==pos:
                newnode=node(data)
                last.next=newnode
                newnode.next=curr
                return
            c=c+1
    def delete(self,val):
        c=0
        curr=self.head
        while True:
            last=curr
            curr=curr.next
            if val==curr.data:
                last.next=curr.next
                return
    def display(self):
        curr=self.head
        c=[]
        while curr.next!=None:
            curr=curr.next
            c.append(curr.data)
        print(*c,sep="->")
def switch(n):
    switcher={
        0:print("enter  number to add"),
            num=int(input()),
            my.append(num),
        1:print("enter position to insert anymore")
            pos,num=map(int,input()).split(),
            my.middle(pos,num),
        2:print("Enter value to delete value"),
            pos=int(input()),
            my.delete(pos),
        3:print("display"),
            my.display(),
    }
    return switcher.get(n,"invalid")
my=linkedlist()
while True:
    print("enter u r choice 1:num 2.insert 3.delete 4.display")
    n=int(input())
    switch(n)

    
    
        

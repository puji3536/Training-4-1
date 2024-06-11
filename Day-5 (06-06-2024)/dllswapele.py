#Swap the numbers when found mid 
'''
ip: 9 10 12 15 3 5 7 8
op: 3 5 7 8 9  10 12 15
'''
class node:
    def __init__(self,u):
        self.data=u
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def addback(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            self.tail.next=node(x)
            self.tail.next.prev=self.tail
            self.tail=self.tail.next
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
        print()
    '''
    def swap(self):
        f=self.head
        s=self.head
        while(f!=None and f.next!=None):
            s=s.next
            f=f.next.next
        t=self.head
        t1=s
        while(t1!=None):
            t.data,t1.data=t1.data,t.data
            t1=t1.next
            t=t.next
    '''
    def swap(self):
        f=self.head
        s=self.head
        while(f!=None and f.next!=None):
            s=s.next
            f=f.next.next
        self.tail.next=self.head
        self.head.prev=self.tail
        t1=s.prev
        t1.next=None
        s.prev=None
        self.head=s
        s.t=t1
        
            
        
l1=dll()
l1.addback(10)
l1.addback(20)
l1.addback(30)
l1.addback(40)
l1.addback(50)
l1.addback(60)
l1.display()
l1.swap()
l1.display()
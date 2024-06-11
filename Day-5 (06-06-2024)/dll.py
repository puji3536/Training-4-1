#Binary search cannot be implemented in doubly linked list because it requires indexing
class node:
    def __init__(self,u):
        self.data=u
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
        print()
    def addback(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            self.tail.next=node(x)
            self.tail.next.prev=self.tail
            self.tail=self.tail.next
            '''
            t=node(x)
            self.tail.next=t
            t.prev=self.tail
            self.tail=self.tail.next
            '''
    def addfront(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            t.next=self.head
            self.head.prev=t
            self.head=t
    def rev_display(self):
        t=self.tail
        while(t!=None):
            print(t.data,end="->")
            t=t.prev
        print()
    def search(self,x):
        t1=self.head
        t2=self.tail
        while(t1!=t2 and t1!=t2.next):
            if(t1.data==x or t2.data==x):
                return "Found"
            t1=t1.next
            t2=t2.prev
        else:
            if(t1.data==x):
                return "Found"
            else:
                return "Not Found"
    def lengthevodd(self):
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.next):
            t=t.next
            t1=t1.prev
        if(t==t1):
            print("Length is Odd")
        else:
            print("Length is Even")
    def pal(self):
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.next):
            if (t.data!=t1.data):
                t=t.next
                t1=t1.prev
        if (t==t1):
            print("Palindrome")
        else:
            print("Not Palindrome")
    def eosdiff(self,x,es,os):
        if(x==None):
            return abs(es-os)
        if(x.data%2==0):
            es+=x.data
        elif(x.data%2==1):
            os+=x.data
        x=x.next
        return self.eosdiff(x,es,os)
    
    def primec(self,x,c): 
        def prime(y,i):  
            if(y==1):
                return 0
            if i==(y//2)+1:
                return 1
            if y%i==0:
                return 0
            return prime(y,i+1)
        if(x==None):
            return c
        y=x.data
        if(prime(y,2)):
            c+=1
        x=x.next
        return self.primec(x,c)
    
l1=dll()
l1.addback(10)
l1.addback(23)
l1.addback(30)
l1.addback(47)
l1.addback(70)
l1.addback(5)
l1.addfront(50)
l1.display()
print("Reverse order")
print(l1.rev_display())
print(l1.search((30)))
l1.lengthevodd()
l1.pal()
print("Even odd sum difference: ",l1.eosdiff(l1.head,0,0))
print("Prime number count: ",l1.primec(l1.head,0))
            
        
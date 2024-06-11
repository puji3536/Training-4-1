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
#Without using recursion
    '''
    def evodsumdiff(self):
        t=self.head
        se=0
        so=0
        while(t!=None):
            if(t.data%2==0):
                se=se+t.data
            else:
                so=so+t.data
            t=t.next
        print("Even sum= ",se)
        print("Odd sum= ",so)
        print("Diff= ",se-so)
    '''
# Using Recursion
#evsum=90 oddsum=85 diff=5
    def evoddsumdiff(self,t,se,so):
        if(t==None):
            return abs(se-so)
        if(t.data%2==0):
            se=se+t.data
        else:
            so=so+t.data
        return self.evoddsumdiff(t.next,se,so)
     
#Prime numbers count using recursion
    def primerec(self,t,c):
        if(t==None):
            return c
        def pnt(s,n):
            if(s>=(n//2)+1):
                return 1
            if(n%s==0):
                return 0
            return pnt(s+1,n)
        if(pnt(2,t.data)):
            c=c+1
        return self.primerec(t.next,c)
            
        
    
l1=dll()
l1.addback(10)
l1.addback(13)
l1.addback(30)
l1.addback(53)
l1.addback(50)
l1.addback(19)
l1.display()
print(l1.evoddsumdiff(l1.head,0,0))
print(l1.primerec(l1.head,0))
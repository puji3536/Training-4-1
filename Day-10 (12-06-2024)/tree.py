class node:
    def __init__(self,u):
        self.data=u
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None
    def create(self,root,x):
        if(root==None):
            return node(x)
        elif(root.data>x):
            root.left=self.create(root.left,x)
        else:
            root.right=self.create(root.right,x)
        return root
    def inorder(self,root):

        if root:
        # Traverse left
            self.inorder(root.left)
        # Traverse root
            print((root.data), end=' ')
        # Traverse right
            self.inorder(root.right)
       
    def postorder(self,root):

        if root:
        # Traverse left
            self.postorder(root.left)
        # Traverse right
            self.postorder(root.right)
        # Traverse root
            print((root.data), end=' ')
    
    def preorder(self,root):

        if root:
        # Traverse root
            print((root.data), end=' ')
        # Traverse left
            self.preorder(root.left)
        # Traverse right
            self.preorder(root.right)

    def sum1(self,root):
        if(root==None):
            return 0
        return root.data+self.sum1(root.left)+self.sum1(root.right)
    
    def esum(self,root):
        if(root==None):
            return 0
        if(root.data%2==0):
           return root.data+self.esum(root.left)+self.esum(root.right)
        else:
            return self.esum(root.left)+self.esum(root.right)
        
    def oddsum(self,root):
        if(root==None):
            return 0
        if(root.data%2!=0):
           return root.data+self.oddsum(root.left)+self.oddsum(root.right)
        else:
            return self.oddsum(root.left)+self.oddsum(root.right)
        
    def evenodd(self,root):
        if(root==None):
            return 0
        if(root.data%2==0):
            return root.data+self.evenodd(root.left)+self.evenodd(root.right)
        else:
            return (self.evenodd(root.left)+self.evenodd(root.right))-root.data
        
    def height(self,root):
        if(root==None):
            return -1
        else:
            return max(self.height(root.left),self.height(root.right))+1
        
    def bal(self,root):
        return abs(self.height(root.left)-self.height(root.right))<=1
    
    def leafn(self,root):
        if root==None:
            return 0
        if(root.left==None and root.right==None):
            return 1
        return self.leafn(root.left)+self.leafn(root.right)
    
    def leafs(self,root):
        if root==None:
            return 0
        if(root.left==None and root.right==None):
            return root.data
        return self.leafs(root.left)+self.leafs(root.right)
    
    def search(self,root,x):
        if root==None:
            return 0
        if(root.data==x):
            return 1
        elif(self.search(root.left,x)==1 or self.search(root.right,x)==1):
            return 1
        '''#instead of elif
        if(root.data>x):
            return self.search(root.left,x)
        else:
            return self.search(root.right,x)
        '''
        
    def depth(self,root,x,c):
        if root==None:
            return -1
        if(root.data==x):
            return c
        if(root.data>x):
            return self.depth(root.left,x,c+1)
        else:
            return self.depth(root.right,x,c+1)
        
    def leftview(self,root,c):

        if(root==None):
            return
        if(c not in l):
            l.append(c)
            #print(root.data,c)
            print(root.data,end=' ')
        self.leftview(root.left,c+1)
        self.leftview(root.right,c+1)
    def rightview(self,root,c):
        if(root==None):
            return
        if(c not in r):
            r.append(c)
            #print(root.data,c)
            print(root.data,end=' ')
        self.rightview(root.right,c+1)
        self.rightview(root.left,c+1)
    def topview(self,root,c):
        if(root==None):
            return
        if c not in t or  t[c]<root.data:
            t[c]=root.data
        #print(root.data)
        self.topview(root.left,c+1)
        self.topview(root.right,c-1)
    def bottomview(self,root,c,d):
        if root==None:
            return
        d[c]=root.data
        self.bottomview(root.left,c-1,d)
        self.bottomview(root.right,c+1,d)
        return d
    '''def topview(self,root,c,l,l1):
        if root==None:
            return
        if c not in l:
            l.append(c)
            if c<0:
                l1.insert(0,root.data)
            else:
                l1.append(root.data)
        self.topview(root.left,c-1,l,l1)
        self.topview(root.right,c+1,l,l1)
        return l1
    def bottomview(self,root,c,d):
        if root==None:
            return
        d[c]=root.data
        self.bottomview(root.left,c-1,d)
        self.bottomview(root.right,c+1,d)
        return d
    '''
        
    
        
            
            
        
        

t={}
l=[]
r=[]

t1=tree()
t1.root=node(13)
'''
t1.root = node(10)
t1.root.left = node(5)
t1.root.right = node(15)
t1.root.left.left = node(2)
t1.root.left.right = node(7)'''
t1.create(t1.root,10)
t1.create(t1.root,5)
t1.create(t1.root,20)
t1.create(t1.root,7)
t1.create(t1.root,11)
t1.create(t1.root,12)
t1.create(t1.root,25)
t1.inorder(t1.root)
print()
t1.preorder(t1.root)
print()
t1.postorder(t1.root)
print()
print(t1.sum1(t1.root))
print(abs((t1.sum1(t1.root.left))-(t1.sum1(t1.root.right))))
print(t1.esum(t1.root))
print(t1.oddsum(t1.root))
print(abs(t1.evenodd(t1.root)))
print(t1.height(t1.root))
if(t1.bal(t1.root)):
    print("balanced")
else:
    print("Not balanced")
print(t1.leafn(t1.root))   #count of leaf nodes
print(t1.leafs(t1.root))   #sum of leaf nodes
if(t1.search(t1.root,12)):
    print("found")
else:
    print("not found")
print(t1.depth(t1.root,5,0))
t1.leftview(t1.root,0)
print()
t1.rightview(t1.root,0)
print()


t1.topview(t1.root,0)
tp=[]   
for i in t:
   tp.append(t[i])
tp.sort()
print(tp)
print("Bottom view:")
d1=t1.bottomview(t1.root,0,{})
l=list(d1.values())
l.sort()
print(l)


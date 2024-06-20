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
        if(root):
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
    def preorder(self,root):
        if(root):
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if(root):
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")
#ADD all nodes of tree
    def addnodes(self,root):
        if root==None:
            return 0
        return root.data+self.addnodes(root.left)+self.addnodes(root.right)
#Method-2 To add all nodes
    '''
    def addnodes(self,root,sum):
        if root is None:
            return sum
        else:
            sum+=root.data
            sum=self.addnodes(root.left, sum)
            sum=self.addnodes(root.right, sum)
            return sum
            '''
#Sum of even nodes
    def evensum(self,root):
        if root==None:
            return 0
        if(root.data%2==0):
            return root.data+self.evensum(root.left)+self.evensum(root.right)
        else:
            return self.evensum(root.left)+self.evensum(root.right)
#Sum of odd nodes
    def oddsum(self,root):
        if root==None:
            return 0
        if(root.data%2!=0):
            return root.data+self.oddsum(root.left)+self.oddsum(root.right)
        else:
            return self.oddsum(root.left)+self.oddsum(root.right)
#Absolute difference between even sum and odd sum
    def absdiff(self,root):
        if root==None:
            return 0
        if(root.data%2==0):
            return root.data+self.absdiff(root.left)+self.absdiff(root.right)
        return (self.absdiff(root.left)+self.absdiff(root.right))-root.data
#Height of tree
    def height(self,root):
        if(root==None):
            return -1
        else:
            return max(self.height(root.left),self.height(root.right))+1
#Tree is balanced or not
    def bal(self,root):
        return abs(self.height(root.left)-self.height(root.right))<=1
#Depth of tree
    def depth(self,root,x,c):
        if root==None:
            return -1
        if(root.data==x):
            return c
        if(root.data>x):
            return self.depth(root.left,x,c+1)
        else:
            return self.depth(root.right,x,c+1)
#Leftview of tree
    def leftview(self,root,c):

        if(root==None):
            return
        if(c not in l):
            l.append(c)
            #print(root.data,c)
            print(root.data,end=' ')
        self.leftview(root.left,c+1)
        self.leftview(root.right,c+1)
#Rightview of tree
    def rightview(self,root,c):
        if(root==None):
            return
        if(c not in r):
            r.append(c)
            #print(root.data,c)
            print(root.data,end=' ')
        self.rightview(root.right,c+1)
        self.rightview(root.left,c+1)

#Topview of tree
    '''
    def topview(self,root,c):
        if(root==None):
            return
        if c not in t or  t[c]<root.data:
            t[c]=root.data
        #print(root.data)
        self.topview(root.left,c+1)
        self.topview(root.right,c-1)
    '''
    def topview(self,root):
        if (root==None):
            return 
        d={}
        q=[(root,0)]
        while q:
            root=q[0][0]
            if(root.left!=None):
                q.append((root.left,q[0][1]-1))
            if(root.right!=None):
                q.append((root.right,q[0][1]+1))
            if (q[0][1] not in d):
                d[q[0][1]]=root.data
            q.pop(0)
        for i in sorted(d):
            print(d[i],sep=",")
        
#Bottomview of tree
    '''
    def bottomview(self,root,c,d):
        if root==None:
            return
        d[c]=root.data
        self.bottomview(root.left,c-1,d)
        self.bottomview(root.right,c+1,d)
        return d
    '''
    def bottom(self,root,c,d,q):
        if root==None:
            return
        
        d={}
        q=[(root,0)]
        while(q):
            root=q[0][0]
            if(root.left!=None):
                q.append((root.left,q[0][1]-1))
            if(root.right!=None):
                q.append((root.right,q[0][1]+1))
            
            d[q[0][1]]=root.data
            q.pop(0)
        print(d)
        for i in sorted(d):
            print(d[i],end=" ")

t={}
l=[]
r=[]
        
t1=tree()
t1.root=node(10)
t1.create(t1.root,5)
t1.create(t1.root,15)
t1.create(t1.root,9)
t1.create(t1.root,4)
print("Inorder Traversal")
t1.inorder(t1.root)
print()
print("Preorder Traversal")
t1.preorder(t1.root)
print()
print("Postorder Traversal")
t1.postorder(t1.root)
print()
print("Sum of nodes=",t1.addnodes(t1.root))
#print("Sum of nodes=",t1.addnodes(t1.root,0))
print("Sum of left sub-tree=",t1.addnodes(t1.root.left))
print("Sum of right sub-tree=",t1.addnodes(t1.root.right))
print("Absolute difference btw left sub tree and right sub tree=",t1.addnodes(t1.root.left)-t1.addnodes(t1.root.right))
print("Sum of even nodes= ",t1.evensum(t1.root))
print("Sum of odd nodes= ",t1.oddsum(t1.root))
print("Absolute difference = ",abs(t1.absdiff(t1.root)))
print("Height= ",t1.height(t1.root))
if(t1.bal(t1.root)):
    print("balanced")
else:
    print("Not balanced")
print("Depth= ",t1.depth(t1.root,5,0))
print("Leftview")
t1.leftview(t1.root,0)
print()
print("Rightview")
t1.rightview(t1.root,0)
print()
print("Topview")
t1.topview(t1.root,0)
tp=[]   
for i in t:
   tp.append(t[i])
tp.sort()
print(tp)
print("Bottom view")
d1=t1.bottomview(t1.root,0,{})
l=list(d1.values())
l.sort()
print(l)
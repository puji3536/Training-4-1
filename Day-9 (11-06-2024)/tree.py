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
#Find height of the tree
    def 
        
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
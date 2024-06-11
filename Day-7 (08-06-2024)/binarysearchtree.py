#Binary Search Tree
'''
[5,9,8,2,1,4]
         5
      /    \
     2      9
    / \    /
   1  4   8      
'''
def fun(root):
    if(root==None):
        root=node(x)
    elif(x<root.data):
        fun(root.left)
    else:
        fun(root.right)
x=[5,9,8,2,1,4]
print(fun(x))
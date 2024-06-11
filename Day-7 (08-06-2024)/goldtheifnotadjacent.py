#The elements are gold in house and theif should take gold from those houses which are not adjacent and finally you should output sum of highest sum fo gold
'''
          l=[13,9,4,10,5,7]
          /               \
 30  13+[4,10,5,7]      9+[10,5,7]
       /        \           /     \
     4+[5,7]   10+[7] 17 10+[7]   5+[]
    /   \      /    \     /    \
   5+[] 7+[]  7+[]  []  7+[]  []
 '''

def fun(l):
    if(len(l)==0):
        return 0
    if(len(l)==1):
        return l[0]
    if(len(l)==2):
        return max(l)
    le=l[0]+fun(l[2:])
    ri=l[1]+fun(l[3:])
    return max(le,ri)
l=[13,9,4,10,5,7]
print(fun(l))
'''
Graph
5---7---4
|   /   | \
|  /    |  ---2
| /     | /
3-------8

dictionary={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
'''
#Visit all nodes in graph
#Solution-1
'''
def dfs(n, d, l):
    if n not in l:
        print(n, end=" ")  
        l.append(n) 
        for i in d[n]:
            dfs(i, d, l)  
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
dfs(5, d, l)
'''

#Solution-2
def dfs(n, d): 
    l.append(n) 
    for i in d[n]:
        if i not in l:
            dfs(i, d)  
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
dfs(5, d)
print(l)

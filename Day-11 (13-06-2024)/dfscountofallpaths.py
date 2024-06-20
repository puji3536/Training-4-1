#Count of all possible paths
'''
Graph
5---7---4
|   /   | \--2
|  /    | /
3-------8
'''

def dfs(n,d,e,c):
    l.append(n)
    if(n==e):
        c=c+1
        l.pop()
        return c
    for i in d[n]:
        if i not in l:
            c=dfs(i,d,e,c)
    l.pop()
    return c
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
print(dfs(5,d,2,0))
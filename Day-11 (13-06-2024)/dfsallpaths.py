#print all paths
'''
Graph
5---7---4
|   /   | \--2
|  /    | /
3-------8
'''

def dfs(n,d):
    l.append(n)
    if(n==2):
        print(l)
        l.pop()
        return 
    for i in d[n]:
        if i not in l:
            dfs(i,d)
    l.pop()
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
dfs(5,d)
#print least cost
'''
Graph
     2   3
   5---7---4 1
 1 |   /4  | \--2
   |  /   5| /1
   3-------8
       2
'''
#d={5:[(7,2),(3,1)],7:[(5,2),(4,3),(3,4)],4:[(7,3),(8,5),(2,1)],8:[(3,2),(4,5),(2,1)],3:[(5,1),(7,4),(8,2)],2:[(4,1),(8,1)]}

def dfs(d,n,e,cost,m,l1):
    l.append(n)
    if n == e:
        if(cost<m):
            m=cost
            l1=l.copy()
        l.pop()
        return m,l1
    for i in d[n]:
        if i[0] not in l:  
            m,l1=dfs(d,i[0],e,cost+i[1],m,l1) 
    l.pop()
    return m,l1
d={5:[(7,2),(3,1)],7:[(5,2),(4,3),(3,4)],4:[(7,3),(8,5),(2,1)],8:[(3,2),(4,5),(2,1)],3:[(5,1),(7,4),(8,2)],2:[(4,1),(8,1)]}
l = []
print(dfs(d,5,2,0,99999,[]))
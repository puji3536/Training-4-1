'''
ip:4x3
op:
    _ _ _ _
    _ _ _ _
    _ _ _ _
'''
def fun(i,j,cnt):
    if i<0 or j<0 or i>=r or j>=c:
        return cnt
    if i==r-1 and j==c-1:
        #print(v)  #for paths
        cnt=cnt+1
        return cnt
    
    
    v.append((i,j))
    if((i-1,j) not in v):
        cnt=fun(i-1,j,cnt)
    if((i,j-1) not in v):
        cnt=fun(i,j-1,cnt)
    if((i+1,j) not in v):
        cnt=fun(i+1,j,cnt)
    if((i,j+1) not in v):
        cnt=fun(i,j+1,cnt)
    v.pop()
    return cnt
            
v=[]
r=3
c=4
l=[]
m=[]
for i in range(r):
    l=[0]*(c)
    m.append(l)
print(fun(0,0,0))

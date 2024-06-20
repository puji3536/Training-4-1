'''
2      4
  5------8----6
  |\     |     \2
  | \ 2  |      \
 2|  \   |3      9----4
  |   \  |      /1
  2------3-----7
      1     3
'''
g={5:[(3,1),(1,2),(6,3)],1:[(5,2),(2,1)],3:[(5,1),(6,3)]}
def dij(n):
    d={5:999,1:9999,3:999,6:999,2:999}
    d[n]=0
    vi=[]
    q=[n]
    while(q):
        m=999
        for i in q:
            if(d[i]<m):
                m=d[i]
                n=i
        if n in g: 
            for i in g[n]:
                if(i[0] not in vi):
                    q.append(i[0])
                    if d[i[0]]>i[1]+d[n]:
                        d[i[0]]=i[1]+d[n]
        vi.append(n)
        q.remove(n)
    return d
'''
g={5:[(3,1),(1,2),(6,3)],1:[(5,2),(2,1)],3:[(5,1),(6,3)]}
def dij(n):
    d={5:999,1:9999,3:999,6:999,2:999}
    d[n]=0
    vi=[]
    q=[n]
    while(q):
        m=999
        for i in q:
            if(d[i]<m):
                m=d[i]
                n=i
        for i in g[n]:
            if(i[0] not in vi):
                q.append(i[0])
                if d[i[0]]>i[1]+d[n]:
                    d[i[0]]=i[1]+d[n]
        vi.append(n)
        q.remove(n)
    return d
dij(5)
'''
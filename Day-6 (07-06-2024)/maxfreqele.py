'''
ip:[4,8,2,4,4,8,4]
op:4

ip:[2,1,2,2]
op:2

ip:[6,6,6,6,7]
op:6
'''
#Solution-1
'''
l=[4,8,2,4,4,8,4]
m=0
for i in l:
    if(l.count(i)>m):
        m=l.count(i)
        p=i
print(p)
'''

#Solution-2
l=[4,8,2,4,4,8,4]
c=1
p=l[0]
for i in range(1,len(l)):
    if(l[i]==p):
        c+=1
    else:
        c-=1
        if(c==0):
            c=1
            p=l[i]
print(p)
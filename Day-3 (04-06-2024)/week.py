'''
ip:
    15 3 2  7 8 4
    m  t w th f sa
op:
    6

ip:
    5 4 2 9 7 1
op:
    7
ip:
    9 8 7 6 5 4
op:
    0
    
ip:
    5 3 2 7 8 4
op:
    6
'''
#Solution-1
'''
l=[9,8,7,6,5,4]
p=0
for i in range(len(l)-1):
    for j in range(i+1,len(l)-1):
        diff=l[j]-l[i]
        p=max(p,diff)
print(p)

'''
#Solution-2
'''
l=[5,4,2,9,7,1]
p=0 
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if (l[i]<l[j] and l[j]-l[i]>p):
            p=l[j]-l[i]
print(p)
'''

l=[5,4,2,9,7,1]
b=a[0]
p=0
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        
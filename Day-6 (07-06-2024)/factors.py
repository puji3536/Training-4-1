'''
find last to 2nd element from the list
n=24
k=2
l=[1,2,3,4,6,8]
'''

n=24
k=2
l=[]
for i in range(1,n):
    if n%i==0:
        l.append(i)
print(l)
a=len(l)-k
print(l[a])
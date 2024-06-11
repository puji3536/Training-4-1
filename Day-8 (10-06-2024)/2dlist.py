'''
Testcase-1
l=[1,2,3,4,1,2,3,1,2]
op:[[1 2 3 4],[1 2 3],[1 2]]
1 2 3 4
1 2 3
1 2
duplicate elements should not be in single row. so it should be printed in next row


Testcase-2
ip:[2,3,1,3,4,3,2]
op:[[2 3 1 4],[3 2],[3]]
2 3 1 4
3 2
3 

Testcase-3
ip:[4,5,2,1]
op:[[4,5,2,1]]
'''
#Solution-1
'''
l=[1,2,3,4,1,2,3,1,2]
r1=[]
r2=[]
r3=[]
for i in l:
    if i not in r1:
        r1.append(i)
    elif i not in r2:
        r2.append(i)
    else:
        r3.append(i)
if len(r1)>0 or len(r2)>0 or len(r3)>0:
    l2=[r1,r2,r3]
    print(l2)
'''

#Solution-2
# a=[a,a,a,3,a,3,2]  Iteration 1
# a=[a,a,a,a,a,3,a]  iteration 2
# a=[a,a,a,a,a,a,a]  iteration 3
#Iteration 4 also happens to check all the elemets in list are alphabets or not
'''
a=[4,5,2,1]
m=[]
c=0
while(c!=len(a)):
    r=[]
    for i in range(len(a)):
        if(not str(a[i]).isalpha()):
            if(a[i] not in r):
                c=c+1
                r.append(a[i])
                a[i]='a'
    m.append(r)
print(m)
'''

#Solution-3
'''
dictionary={2:2,3:3,1:1,4:1}
             | |
        value  number of times the value is present
'''
a=[2,3,1,3,4,3,2]
d={}
m=[]
for i in a:
    if(i not in d):
        d[i]=1
    else:
        d[i]=d[i]+1
c=0
while(c!=len(a)):
    r=[]
    for i in d:
        if(d[i]!=0):
            d[i]=d[i]-1
            c=c+1
            r.append(i)
    m.append(r)
print(m)
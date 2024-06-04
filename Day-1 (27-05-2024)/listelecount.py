#Count number of numbers 

l=[3,5,4,3,6,7,1,2,4,3,3,7,6,8,8]
c=1
r=[]
i=0
for i in l:
    if (i not in r):
        r.append(i)
for i in r:
    print(i,"-",l.count(i))
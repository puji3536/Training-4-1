'''
#Print highest of a according to the time in nums
nums=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
a=[5,6,5,4,11,2]
'''
jobs=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
a=[5,6,5,4,11,2]
b=a.copy() #b=[5,6,5,4,11,2]
for i in range(1,len(jobs)):
    for j in range(0,i):
        if (jobs[j][1]<=jobs[i][0]):
            if(b[j]+a[i]>b[i]):
                b[i]=b[j]+a[i]
print(max(b))  #6+11=17
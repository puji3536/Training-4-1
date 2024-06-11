#Print all possible 3,3 combinations 
#l=list(map(int,input().split()))
'''
l=[3,2,5,4,1,6,8]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
            print(l[i],l[j],l[k])
'''
#Using recursion where k = number of combinations required
def combinations(l,k):
    def fun(curr,start):
        if len(curr)==k:
            print(curr)
            return
        for i in range(start,len(l)):
            fun(curr+[l[i]],i+1)
    fun([],0)
l=[3,2,5,4,1,6,8]
k=3
combinations(l,k)
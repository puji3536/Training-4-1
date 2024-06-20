'''
ip:[2,5,2,3,6,7,1,0,5,7]
op:20

ip:[4,3,4,5,6,1,0,6,7]
op:12

     |   |
    ||   |
 |  ||  ||  
 |  ||  || 
 | |||  ||
||||||  ||
||||||| ||
------------------------
'''
#Solution-1
class Solution:
    def trap(self, height):
        if not height: 
            return True
        l=0
        r=len(height)-1
        maxl=height[l]
        maxr=height[r]
        res=0
        while l<r:
            if maxl<maxr:
                l+=1
                maxl=max(maxl,height[l])
                res+=(maxl-height[l])
            else:
                r-=1
                maxr=max(maxr,height[r])
                res+=(maxr-height[r])
        return res
solution=Solution()
print(solution.trap([4,3,4,5,6,1,0,6,7]))

#Solution-2
'''
arr=[2,5,2,3,6,7,1,0,5,7]
l=[0]*len(arr)
r=[0]*len(arr)
m=0
for i in range(len(arr)):
    if arr[i]>m:
        m=arr[i]
    l[i]=m
m1=0
for i in range(len(arr)-1,-1,-1):
    if arr[i]>m1:
        m1=arr[i]
    r[i]=m1
s=0
for i in range(len(arr)):
    s=s+abs(min(l[i],r[i])-arr[i])
print(s)
'''
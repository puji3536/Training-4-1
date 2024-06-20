'''
List is building heights. Morning the sun is left side and evening the sun is right side.
ip:[3,5,9,6,8,10]
op:4
   1
 
     |
  |  |
  | ||
  | ||
  ||||
 |||||
 |||||
||||||
||||||
|||||| 
'''
l=[3,4,5,10,4,3]
n=len(l)
m=0

c1,c2=1,1
for i in range(1,n-1):
    if m<l[i+1]:
        m=l[i+1]
    if m>l[i]:
        c1=c1+1
m=0
for i in range(n-1,-1,-1):
    if m<l[i]:
        m=l[i]
    if m<l[i-1]:
        c2=c2+1
print(c1,c2)
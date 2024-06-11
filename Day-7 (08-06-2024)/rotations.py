'''
ip:school
   3
   L 2 -->hoolsc
   R 3 -->oolsch
   L 1 -->chools
op: yes
after rotation, the first characters of hoc
sch,cho,hoo,ool
check if hoc is anagram or not i.e., hoc is in subsets of string or not
'''

#SOlution-1
'''
st='school'
l=list(st)
n=3
L=2
R=3
S=1
c=[]
for i in range(len(l)-1):
    if i==L or i==R or i==S:
        c.append(l[i])
print(c)
for i in range(len(l)-n+1):
    subset = [l[i],l[i+1],l[i+2]]
    print(subset)
    if sorted(c) == sorted(subset):
        print("yes")
'''

#Solution-2
a=input()
n=int(input())
str=[]
for i in range(n):
    b=input()
    if(b[0]=='L'):
        str.append(a[int(b[2])])
    else:
        str.append(a[-int(b[2])])
print(str)
str.sort()
b=[]
for i in range(len(a)-n+1):
    t=sorted(list(a[i:n+i]))
    b.append(t)
print(b)
print(str)
for i in b:
    if(i==str):
        print("Yes")
        break
else:
    print("No")
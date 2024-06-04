'''
ip:
    3
    xyz
    pqr
    abc
    "yraxpazr"
op:
   yes
ip:
    4
    abcd
    xyze
    pqrw
    stuv
    "cyptdzsayq"
op:
    no
'''
#Solution-1
'''
n=int(input())
m = []
flag=0
for i in range(n):
    m.append(input())
s=input()
for i in range(len(s)):
    if (s[i] in m[i]):
        continue
    else:
        flag=1
        break
if flag==1:
    print("No")
else:
    print("Yes")
'''
#Solution-2

n=int(input())
m = []
flag=0
for i in range(n):
    m.append(list(input()))
s=input()
for i in range(len(s)):
    if (s[i] not in m[i%n]):
        print("No")
        flag=1
        break
    else:
        m[i].remove(s[i])
if flag==0:
    print("Yes")
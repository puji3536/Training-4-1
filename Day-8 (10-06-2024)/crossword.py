'''
QSN-79 leetcode
ip:4
tued
fwoa
roer
drui
input:word
op:Yes
#crossword 
'''
n = 4
a = [
    list("tued"),
    list("fwoa"),
    list("roer"),
    list("drui")
]
s = list("word")
def fun(i,j,k,t):
    if(k==len(s)):
        return 1
    if(i<0 or j<0 or i>=n or j>=n or a[i][j]!=s[k]):
        return
    if (a[i][j]==s[k]):
        a[i][j]=0
    t=fun(i+1,j,k+1)
    t=fun(i-1,j,k+1)
    t=fun(i,j-1,k+1)
    t=fun(i,j+1,k+1)
    return t
for i in range(n):
    for j in range(n):
        if(a[i][j]==s[0]):
            c=fun(i,j,1,0)
            if(c==1):
                print("Yes")
                break
if (c==0):
    print("No")
    
'''
n = 4
a = [
    list("tued"),
    list("fwoa"),
    list("roer"),
    list("drui")
]
s = list("ducer")

def fun(i, j, k):
    if k == len(s):
        return 1
    if i < 0 or j < 0 or i >= n or j >= n or a[i][j]!= s[k]:
        return 0
    temp = a[i][j]
    a[i][j] = 0
    if fun(i + 1, j, k + 1) or fun(i - 1, j, k + 1) or fun(i, j - 1, k + 1) or fun(i, j + 1, k + 1):
        return 1
    a[i][j] = temp
    return 0

for i in range(n):
    for j in range(n):
        if a[i][j] == s[0]:
            if fun(i, j, 0):
                print("Yes")
                exit()
print("No")
'''

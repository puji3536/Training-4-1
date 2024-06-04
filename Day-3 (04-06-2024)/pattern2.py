'''
ip:
    4
op:
    ----a----
    ---aba---
    --abcba--
    -abcbabc-
'''

n=int(input())
a=97
for i in range(n,0,-1):
    for j in range(i-1,0,-1):
        print("_",end=" ")
    print()
'''
ip:7
op:0 5 3 6 7 2 1
'''
#Solution-1
'''
n=7
list=[0,5,3,6,7,2,1]
for i in range(n+1):
    if (i not in list):
        print(i)
        break
'''
#SOlution-2
n=7
list=[0,5,3,6,7,2,1]
b=sum(list)
n=(n*(n+1))//2
print(n-b)
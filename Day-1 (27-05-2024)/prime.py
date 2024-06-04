#Check for prime number. If it is not prime number , then print next prime number
'''
n=int(input())
i=2
for i in range(2,n):
    if n%i==0:
        print("not prime")
    else:
        print("prime")
        break
'''

n=int(input())
while(1):
    c=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            c=c+1
            break
    if c==0:
        print(n)
        break
    else:
        n=n+1
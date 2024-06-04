#Count number of prime numbers in given digit
#Solution-1
'''
n=234865
c=0
while(n):
    if(n%10 in [2,3,5,7]):
        c=c+1
    n=n//10
print(c)
'''

#Solution-2
n=int(input())
k=0
while n>0:
    rem=n%10
    c=0
    for i in range(2,(rem//2)+1):
        if(rem%i==0):
            c+=1
    if(c==0):
        k+=1
    n=n//10
print(k)  
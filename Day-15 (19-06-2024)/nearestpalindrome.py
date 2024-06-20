#check for palindrome. If it is palindrome then print same. Else print next nearest palindrome
'''
def fun(n,rev):
    if (n==0):
        return rev
    rev=rev*10+(n%10)
    return fun(n//10,rev)
m=int(input())
if(m==fun(m,0)):
    print("Pal")
else:
    print("Not pal")
'''
'''
ip:122
op:131

ip:1234
op:1331

ip:24
op:33

ip:1112
op:1221

ip:7654
op:7667

ip:56472
op:56565
'''
#Solution-1
'''
def palin(n):
    temp=n
    
    rev=0
    while n>0:
        rev=rev*10+(n%10)
        n=n//10
    if(temp==rev):
        return temp
    else:
        return palin(temp+1)
n=122
print(palin(n))
'''

#Solution-2
s=123#76541#153#1112#1234#192 #12345  #192
s=str(s)
s1=''
s2=''
if(s==s[::-1]):
    print(s)
else:
    if(len(s)%2==0):
        s1=s[:len(s)//2]
        s2=s1+s1[::-1]
        if(int(s)>int(s2)):
            s1=s[:len(s)//2]
            s1=int(s1)+1
            s1=str(s1)
            s2=s1+s1[::-1]
    else:
        s1=s[:len(s)//2+1]
        s2=s1+s1[-2::-1]
        if(int(s)>int(s2)):
            s1=str(int(s1)+1)
            s2=s1+s1[-2::-1]

print(s2)
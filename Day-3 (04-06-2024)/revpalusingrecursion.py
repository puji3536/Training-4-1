#Reverse the given number and check if it is palindrome or not 
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
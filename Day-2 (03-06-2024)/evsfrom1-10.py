#Even sum from 1-10 numbers
def sum(x):
    if (x==0):
        return 0
    return x+sum(x-2)

n=10
if(n%2==0):
    print(sum(n))
else:
    print(sum(n-1))
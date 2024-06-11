'''a=3
b=9
for i in range(2,(min(a,b)//2)+1):
    if(a%i==0) and (b%i==0):
        print("np")
        break
else:
    print("co")
    '''
import math
a=5
b=41
print(math.gcd(a,b)==1)
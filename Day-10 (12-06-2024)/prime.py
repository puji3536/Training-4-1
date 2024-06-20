#Print largest prime number between two adjacent numbers in the list
def prime(num):
    for i in range(2,(num//2)+1):
        if (num%i==0):
            return 0
    return 1
l=[14,16,20,22]
p=[]
for i in range(len(l)-1):
    j=l[i]
    m=0
    while j<l[i+1]:
        
        if(prime(j)):
            
            if(j>m):
                m=j 
        j=j+1
    p.append(m)
print(p)
print(sum(p))

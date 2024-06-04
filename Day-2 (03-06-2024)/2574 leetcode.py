a=[10,4,8,3]
'''
b=[]
for i in range(len(a)):
    b.append(abs(sum(a[:i]-sum(a[i+1:]))))
print(b)
'''
'''
s=sum(a)
x=0
r=[]
for i in a:
    r.append(abs((x)-(s-i-x)))
    x=x+i
print(r)
'''

s=sum(a)
x=0
j=0
for i in a:
    a[j]=abs((x)-(s-i-x))
    x=x+i
    j=j+1
print(a)
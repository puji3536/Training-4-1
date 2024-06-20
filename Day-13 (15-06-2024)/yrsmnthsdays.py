'''
ip: 65476
op: ?y ?m ?w ?d
1 year=360 days
1 month=30 days
1 week= 6 days
'''
n=65476
y=n//360
n=n%360
m=n//30
n=n%30
w=n//6
d=n%6

print(y,"yrs",m,'m',w,'weeks',d,'days')


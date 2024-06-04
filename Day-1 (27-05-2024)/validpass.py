#Check validatoin of password with min characters=8,special character=1,lowercase=1,uppercase=1
'''
ip:asd123!@  op:1
ip:123456789 op:3
ip:ab op:6
'''

#Solution-1
'''
s="aBd126!@"
u,l,s,d=0,0,0,0
for i in s:
    if(i.isdigit()):
        d=1
    elif(i.islower()):
        l=1
    elif(i.isupper()):
        u=1
    else:
        s=1
m=4-(u+l+d+s)
if (len(n)+m)<8:
    print(8-len(n))
else:
    print(m)
'''

#Solution-2
s=input()
l,u,d,sc=0,0,0,0
c=0
for i in s:
    if(i.islower()):
        l=1
    if(i.isupper()):
        u=1
    if(i.isdigit()):
        d=1
    if(not i.isalnum()):
        sc=1
if l==0:
    c=c+1
if u==0:
    c=c+1
if d==0:
    c=c+1
if sc==0:
    c=c+1
c=4-(u+d+l+sc)
if len(s)>=8: 
    if(l!=0 and u!=0 and d!=0 and sc!=0):
        print("-1")
    else:     
        print(c)
elif len(s)<8:
    if(len(s)+c>=8):
        print(c)
    elif len(s)+c<8:
        print(8-len(s))
    else:      
        print(8-len(s)+c)
        
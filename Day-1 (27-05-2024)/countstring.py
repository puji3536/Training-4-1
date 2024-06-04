'''
ip:aaabbaaaaddd
op:a3b2a4d3
'''

s="aaabbaaaadddb"
c=1
t=''
i=0
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        t=t+s[i]+str(c)
        c=1
t=t+s[i+1]+str(c)
''' t=t+s[-1]+str(c)
both can be used'''
print(t)


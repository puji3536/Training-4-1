#Print M if male count is greater. Print F if Female count is greater. Print 0 if male and female count are equal.

s="MMFFMFMFMMFMFMFMFFF"
'''
c1=0
c2=0
for i in range(len(s)):
    if s[i]=="M":
        c1+=1
    else:
        c2+=1
if c1==c2:
    print("0")
elif c1>c2:
    print("M")
else:
    print("F")
'''

#solution-2
c=0
for i in range(len(s)):
    if s[i]=="M":
        c+=1
    else:
        c-=1
if c>0:
    print("M")
elif c<0:
    print("F")
else:
    print("0")
    
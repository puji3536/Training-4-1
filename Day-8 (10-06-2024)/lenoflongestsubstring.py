'''
ip:"abfgresagtyuiofde"
op:12
resagtyuiofd = len is 12
Print length of longest substring without repeating characters
'''
'''
#outputnot came
a = "abfgresagtyuiofds"
d={}
s=""
m=0
i=0
while(i<len(a)):
    while(i<len(a)):
        if (a[i] not in s):
            s=s+a[i]
            d[s[i]]=i
        else:
            if(len(s)>m):
                m=len(s)
            s=""
            break
        i=i+1
    i=d[a[i]]+1
print(m)
'''
a = "abfgresagtyuiofds"
m = 0
i = 0
j = 0
s = set()
while j < len(a):
    if a[j] not in s:
        s.add(a[j])
        j += 1
        m = max(m, j - i)
    else:
        s.remove(a[i])
        i += 1
print(m)
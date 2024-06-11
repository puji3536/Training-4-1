'''
ip:2
   polikujmnhytgbvfredcxswqaz
   abcd
   qwryupcsfoghjkldezxvbintma
   ativedoc
op:
    bdca
    codevita
'''

#Solution-1
'''
alp='polikujmnhytgbvfredcxswqaz'
b=''
s='abcd'
for i in range(len(alp)):
    for j in range(len(s)):
        if alp[i]==s[j]:
            b += alp[i]
print(b)
'''
#Solution-2
'''
a = "polikujmnhytgbvfredcxswqaz"
b = "abbcdd"
c= {}
for i in range(len(a)):
    c[a[i]] = i
s= ''.join(sorted(b,key =c.get))
print(s)
'''
'''

ip:2
ip:qwertyuiopasdfghjklzxcvbnm
ip:abbcdde
op:eaddcbb
ip:poiuytrewqlkjhgfdsamnbvcxz
ip:nrai
op:iran
'''

n=int(input())
while(n):
    a=input()
    c=input()
    s=''
    for i in a:
        if(i in c):
            s=s+(i*c.count(i))
    print(s)
    n=n-1
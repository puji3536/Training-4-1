'''
ip:
    "xyzabcdefklmnopqefgh"
op:
    7
abcdef is the longest subsequence
'''
#length of longest substring who has alphabet in sequence
#Sliding window algorithm for comparision of adjacent elements. Use len(s)-1 foe which i should stop at last second posiotion. If not, it gives index out of range error/.
s = input()
c=1
max=0
for i in range(len(s)-1):
    if (ord(s[i])==ord(s[i+1])-1):
        c+=1
    else:
        if c>max:
            max=c
            c=1
if c>max:
    max=c
print(max)
            

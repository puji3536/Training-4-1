l1=[2,5,7,9]
l2=[1,3,6,10,13]
"""
Solution:1

l3=l1+l2
l3.sort()
print(l3)"""
i=0
j=0
l3=[]
while i<len(l1) and j<len(l2):
    if l1[i]<l2[j]:
        l3.append(l1[i])
        i+=1
    else:
        l3.append(l2[j])
        j+=1
while j<len(l2):
    l3.append(l2[j])
    j=j+1
while i<len(l1):
    l3.append(l1[i])
    i=i+1
    

'''
Solution:3

if j<len(l2):
    l3.extend(l2[j:])
if i<len(l1):
    l3.extend(l1[i:])'''
print(l3)
    
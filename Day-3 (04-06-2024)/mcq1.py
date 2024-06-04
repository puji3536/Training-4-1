#mcq-1
a=[6,5,7,3,2]
a.append([5,8])
a.extend([4,2,1])
#a.extend(78)
a.append(50)
print(a)
print(len(a))

#mcq-2
a={5,5.2,'60',(5,2),[3,5],(2,5),{1}}
print(a)
#Gives error because lists , sets, dictionaries are not allowed in sets.

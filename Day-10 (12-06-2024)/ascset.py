#sort 3 3 elements in list
'''4  8  9  2  14  3  5  6
      2  8  9  14  3  5  6
         8  9  14  3  5  6
            3   9  14 5  6
                5  9  14 6
                   6   9 14
op= 4 2 8 3 5 6 9 14
'''
#a=list(map(int,input().split()))#object reference converted to list
'''
a=[4,9,8,2,14,3,5,6]
for i in range(len(a)-2):
    if(a[i]>a[i+1]):
      a[i],a[i+1]=a[i+1],a[i]
    if(a[i+1]>a[i+2]):
       a[i+1],a[i+2]=a[i+2],a[i+1]  
    if(a[i]>a[i+1]):
        a[i],a[i+1]=a[i+1],a[i]
print(a)

'''
l=[4,9,8,2,14,3,5,6]
n=len(l)
for i in range(n-2):
    if(l[i]>l[i+1]):
        l[i],l[i+1]=l[i+1],l[i]
    if(l[i+1]>l[i+2]):
            l[i+1],l[i+2]=l[i+2],l[i+1]
            if(l[i]>l[i+1]):
                 l[i],l[i+1]=l[i+1],l[i]
    print(l)
print(l)
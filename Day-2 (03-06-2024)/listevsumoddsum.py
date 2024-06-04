'''
#Even sum from first list and odd sum from second list
'''
def add(i,j,es,os):
    c=[]
    if i==len(a) and j==len(b):
        c.append(es)
        c.append(os)
        return c
    if i==len(a):
        return
    else:
        if(a[i]%2==0):
            es+=a[i]
    if j==len(b):
        return
    else:
        if(b[i]%2==1):
            os+=b[i]
    return add(i+1,j+1,es,os)
a=[3,8,5,4,3]
b=[5,0,9,3,2]
print(add(0,0,0,0))
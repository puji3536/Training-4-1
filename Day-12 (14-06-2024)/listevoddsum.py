#Match all the even numbers in first list(l1) with all odd numbers in second list(l2)

def fun(l1,l2):
    l=[]
    i=0
    while i<len(l1):
        if l1[i]%2==0:
            j=0
            while j<len(l2):
                if l2[j]%2!=0:
                    l.append(l1[i]+l2[j])
                j+=1
        i+=1
    return l

l1 = [6, 3, 2, 9, 4, 7]
l2 = [8, 9, 5, 3, 6, 9]
print(fun(l1,l2))
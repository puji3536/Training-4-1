n=int(input())
l=[]
res=[]
a=''
for i in range(n):
    a=input()
    if(a[0]=='1'): #insert
        if(a[2:] not in l):
            l.append(a[2:])
    if(a[0]=='2'): #search word
        if(a[2:] in l):
            #print("True")
            res.append(True)
        else:
            #print("False")
            res.append(False)
    if(a[0]=='3'): #prefix in list or not
        c=0
        al=len(a[2:])
        for i in range(len(l)):
            s=l[i]
            s=s[:al]
            #print(s)
            #print(a)
            if s==a[2:]:
                #print(c)
                c=c+1
        res.append(c)
                
    if(a[0]=='4'):    #delete
        for i in range(len(l)):
            if l[i]==a[2:]:
                l.remove(l[i])
                break

print(*res)
        
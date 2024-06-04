
#count all vowels and consonents and special characters
'''
s="dyif#so86546wytiueoA@"
i=0
c1,c2,c3=0,0,0
vow=''
cons=''
sc=''
while i<len(s):
    if s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u":
        c1+=1
    if s[i]=="A" or s[i]=="E" or s[i]=="I" or s[i]=="O" or s[i]=="U":
        c1+=1
        vow=vow+s[i]+"-"+str(c1)
    elif s[i]=="@" or s[i]=="#" or s[i]=="&":
        c2+=1
        cons=cons+s[i]+"-"+str(c2)
    else:
        c3+=1
        sc=sc+s[i]+"-"+str(c3)
print(vow)
print(cons)
print(sc)
'''

#count all Uppercase,lowercase vowels and consonants, digits and special characters
a="uf98982DSOJF8UAE&#@(*@54aik"
uv,uc,lv,lc,d,s=0,0,0,0,0,0
for i in a:
    if(i.isupper()):
        if(i in 'AEIOU'):
            uv=uv+1
        else:
            uc=uc+1
    elif(i.islower()):
        if(i in 'aeiou'):
            lv=lv+1
        else:
            lc=lc+1
    elif(i.isdigit()):
        d+=1
    elif(i.isalpha()):
        s+=1
print("Upper vowels=",uv,"Upper Consonants=",uc,"Lower vowels=",lv,"Lower Consonants=",lc,"Digits=",d,"Special Characters=",s)
    
    
'''
ip:7 #number of queries
   1 school #insert the word if 1.
   1 world
   1 word
   1 scholar
   2 word  #Search for a word if 2. Print True if present or False if not present
   2 wood
   3 sch  #Search for a word with given prefix if 3.Print True if present or False if not present
op:True
   False
   True
'''
'''
ip:
7
1 school
1 world
1 word
1 scholar
2 word
2 wood
3 sch
'''

class node:
    def __init__(self):
        self.d={}
        self.flag=0
        
class tries:
    def __init__(self):
        self.root=node() 
    def insert(self,str):
        t=self.root
        for i in str:
            if(i not in t.d):
                t.d[i]=node()
            t=t.d[i]
        t.flag=1
    def search(self,str):
        t=self.root
        for i in str:
            if(i not in t.d):
                return False
            t=t.d[i]
        if(t.flag==1):
            return True
        else:
            return False
    def search_prefix(self,str):
        t=self.root
        for i in str:
            if(i not in str):
                return False
            t=t.d[i]
        return True
#print all the words which have given prefix
    def print_all_prefix(self,str):
        def fun(t,s):
            if(t.flag==1):
                print(s)
            for i in t.d:
                fun(t.d[i],s+i)
        t=self.root
        s=""
        for i in str:
            if(i in str):
                s=s+i
                t=t.d[i]
            else:
                return
        fun(t,s)
        
t1=tries()
n=int(input())
for i in range(n):
    a,s=input().split()
    if(a=='1'):
        t1.insert(s)
    if(a=='2'):
        t1.search(s)
    if(a=='3'):
        print(t1.search_prefix(s))
    if(a=='4'):
        print(t1.print_all_prefix(s))
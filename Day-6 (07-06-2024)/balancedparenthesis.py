#Print the position where the parenthesis is not balanced
'''
#sir gave code not giving crct answer
a='(([{]))'
s=[]
f=0
c=0
for i in a:
    if(i in '{[('):
        c+=1
        s.append(i)
    elif(not s):
        if (i=='}' and i=='{' or i==')' and i=='(' or i==']' and i=='['):
            c-=1
            s.pop()
        else:
            print(c)
            f=1
            break
    else:
        print(c)
        f=1
        break
if(f==0):
    print(-1)

'''
a = '=(([]{))'
s = []
f = 0
for i in range(len(a)):
    if a[i] == '(':
        s.append(a[i])
    elif a[i] == ')':
        if not s or s.pop()!= '(':
            f = 1
            print(i+1)
            break
    elif a[i] == '{':
        s.append(a[i])
    elif a[i] == '}':
        if not s or s.pop()!= '{':
            f = 1
            print(i+1)
            break
    elif a[i] == '[':
        s.append(a[i])
    elif a[i] == ']':
        if not s or s.pop()!= '[':
            f = 1
            print(i+1)
            break
if f == 0 and not s:
    print(-1)

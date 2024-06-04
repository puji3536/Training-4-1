'''
ip:5 3.8 7 5.6 4 2 3
op:15 6 9.4
#sum of even numbers, odd numbers and decimals separately
'''
#list=list(map(int,input().split()))
list=[5,3.8,7,5.6,4,2,5]
e,o,f=0,0,0
for i in list:
    if i%2==0:  #if(int(a)==a)
        e=e+i
    elif i%2==1:
        o=o+i
    else:          
        f=f+i
print("even sum = ",int(e))
print("odd sum = ",int(o))
print("float sum = ",f)
'''
dot(.) operator is present in float numbers only 
a="7.6"
if ('.' in a):
    print("i")

'''
'''
float number modulo will not give 0
integer number modulo gives 0 as remainder
a=5
b=7.4
print(a%1)
print(b%1)
'''
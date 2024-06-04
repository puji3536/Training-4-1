#find the count of numbers divisible by 7 between the range 300 to 400 inclusive
count=0
for i in range(300,400):
    if i%7==0:
        count+=1
print(count)

'''
Formulae
print(300/7)-(400/7)
'''
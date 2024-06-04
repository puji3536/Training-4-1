'''
s=input().split()
key=int(input())
res=""
for i in range(len(s)):
    for char in s[i]:
        asc=ord(char)
        res+=chr(asc-key)
    print(res)
'''

#Solution-2
s = input().split()
key = int(input())
c = key % 26
for i in range(len(s)):
    d = ""
    for char in s[i]:
        if ((ord(char) - c) >= 97):
            d += chr(ord(char) - c)
        else:
            d += chr(ord(char) - c + 26)
    print(d)
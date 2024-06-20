#print longest palindromic substring. If not present Print -1
'''
ip:"abdbsdabca"
op:bdb
'''
def longestPalindrome(s):
    n=len(s)
    def is_palin(left,right):
        while left>=0 and right<n and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    res=""
    for i in range(len(s)):
        if len(s)==1:
            return s
        pal1=is_palin(i,i)
        if len(pal1)>len(res):
            res=pal1
        pal2=is_palin(i,i+1)
        if len(pal2)>len(res):
            res=pal2
    return res 
s='abdbsdabca'   
print(longestPalindrome(s)) 
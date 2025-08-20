def palindrome(x):
    s=''
    for i in x:
        s=i+s
    return x==s

def palino(s):
    a=[]
    for i in range(len(s)):
        st=''
        for j in range(i,len(s)):
            st=st+s[j]
            if palindrome(st):
                a.append(st)
    return a
s='aaabaaa'
print(palino(s))

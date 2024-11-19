def string_reduce(s):
    if not s:
        return ""
    res=[]
    co=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            co+=1
        else:
            res.append(s[i-1]+str(co))
            co=1
    res.append(s[-1]+str(co))
    return ''.join(res)
    
s=input()
print(string_reduce(s))

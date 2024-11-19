s=input().strip()
v="aeiouAEIOU"
c="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNOPQRSTVWXYZ"
c1=0
v1=0
for i in s:
    if i in v:
        v1+=1
    elif i in c:
        c1+=1
        
print(v1,end=",")
print(c1)    

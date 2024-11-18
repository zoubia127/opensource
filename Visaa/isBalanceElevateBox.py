n=int(input())
a=list(map(int,input().split()))
l=0
r=0
for i in range(n):
    if i!=0 or i!=n:
        l+=sum(a[0:i])
        r+=sum(a[i+1:n+1])
        res=abs(l-r)
        print(res,end=" ")
        l,r=0,0
    elif i==0:
        l=0
        r+=a[i+1:n+1]
        res=abs(l-r)
        print(res,end=" ")
    else:
        r=0
        l+=a[0:n]
        res=abs(l-r)
        print(res,end=" ")
print()

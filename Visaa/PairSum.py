n=int(input())
a=list(map(int,input().split()))
t=int(input())
c=0
for i in range(n):
    for j in range(i+1,n):
        if i<j and a[i]+a[j]==t:
            c+=1
if c>0:
    print("true")
else:
    print("false")

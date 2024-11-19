n=int(input())
a=list(map(int,input().split()))
r=a[1:]+a[:1]
print(*r)

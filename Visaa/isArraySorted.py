n=int(input())
a=list(map(int,input().split()))
if a==sorted(a):
    print("true")
else:
    print("false")

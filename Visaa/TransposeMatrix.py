n=int(input())
a=[]
t=[]
for i in range(n):
    e=list(map(int,input().split()))
    a.append(e)
for c in range(len(a[0])):
    n_m=[]
    for r in range(n):
        n_m.append(a[r][c])
        print(a[r][c],end=" ")
    print()

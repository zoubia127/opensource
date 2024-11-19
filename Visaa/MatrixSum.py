n=int(input())
a=[]
s1=[]
s2=[]
for i in range(n):
    e=list(map(int,input().split()))
    a.append(e)
for i in range(n):
    c=0
    for j in range(n):
        c+=(a[j][i])
    s1.append(c)
    c=0
for i in range(n):
    r=0
    for j in range(n):
        r+=(a[i][j])
    s2.append(r)
    r=0
for i in range(len(s1)):
    print(s1[i]+s2[i],end=" ")

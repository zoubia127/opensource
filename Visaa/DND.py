n,m=map(int,input().split())
a=list(map(int,input().split()))
n1=[]
n2=[]
for i in a:
    if i%m==0:
        n1.append(i)
    else:
        n2.append(i)
print(sum(n1)-sum(n2))

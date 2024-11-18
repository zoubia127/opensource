x,y=map(int,input().split())
p=y-x*100
x1=p/100
x2=p//100
if x1-x2>0:
    print(x2+1)
else:
    print(x2)

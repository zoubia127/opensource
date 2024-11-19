n=int(input())
m=[list(map(int,input().split())) for _ in range(n)]
for i in range (n):
    m[i]=m[i][::-1]
for row in m:
      print(*row)

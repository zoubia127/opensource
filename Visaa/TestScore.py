N, X, Y = map(int, input().split())
if Y % X == 0 and Y <= N * X:
    print("YES")
else:
    print("NO")

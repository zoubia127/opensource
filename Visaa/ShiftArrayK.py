def is_triangle(n,sides):
    sides.sort(reverse=True)
    for i in range(len(sides)-2):
        if sides[i]<sides[i+1]+sides[i+2]:
            return sides[i]+sides[i+1]+sides[i+2]
    return -1
n=int(input())
sides=list(map(int,input().split()))
print(is_triangle(n,sides))

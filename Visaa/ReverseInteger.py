n = int(input())
s = str(abs(n))
s=int(s[::-1])
if n < 0:
    s = -s
if -2**31 <= s <= 2**31 -1:
    print(s)
else:
    print(0)

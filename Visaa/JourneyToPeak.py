n=int(input())
a=list(map(int,input().split()))
c_s=0
m_s=c_s
for i in range(n):
    c_s+=a[i]
    if c_s>m_s:
        m_s=c_s
print(m_s)

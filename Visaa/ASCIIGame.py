s=input()
r=""
for i in s:
    if i.isupper():
        r+=i.lower()
    if i.islower():
        r+=i.upper()
print(r)

c=input("Nhập c: ")
if c>='a' and c<='z':
    c=c.upper() 
else:
    if c>='A' and c<='Z':
        c=c.lower()
print(c)         
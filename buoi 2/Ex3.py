c=input("Nhập kí tự c: ")
if ord(c) >= 65 and ord(c) <= 90:
    c=c.lower()
else:
    if ord(c) >= 97 and ord(c) <= 122:
        c=c.upper()
print(c)
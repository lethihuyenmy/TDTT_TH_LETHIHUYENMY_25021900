c=input("Nhập chữ cái hoa: ")
a=c.lower()
if a=='a':
    print("A là đặc biệt")
else:
    print(chr(ord(a)-1))    

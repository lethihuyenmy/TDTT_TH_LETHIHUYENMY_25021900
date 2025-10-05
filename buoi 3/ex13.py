n=int(input("Nhập số điện tiêu thụ: "))
gia=0
if n>0 : gia += 1500*min(n,50)
print(gia)
if n>50 : gia += 2000*min(n-50,50)
print(gia)
if n>100 : gia += 3000*(n-100)
print(gia)
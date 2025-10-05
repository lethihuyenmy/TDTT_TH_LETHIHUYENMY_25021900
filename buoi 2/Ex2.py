a=int(input("Nhập chiều rộng: "))
b=int(input("Nhập chiều dài: "))

#Tính diện tích hình chữ nhật
S=a*b

#Tính diện tích hình tròn
T=3.14*(a/2)**2

#Diện tích phần còn lại
A=S-T
print(f"Diện tích phần trồng cây xung quanh là: {A:.2f}")
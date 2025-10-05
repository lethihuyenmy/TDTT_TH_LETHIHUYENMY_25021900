a=int(input("Nhập năm: "))
if a % 400 ==0:
    print("Yes")
elif a % 4 ==0 and a % 100 !=0:    
    print("Yes")
else:
    print("No")                
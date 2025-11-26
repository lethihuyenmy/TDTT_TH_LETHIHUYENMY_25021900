X=int(input("Nhập tiền: "))
N=int(input("Nhập tháng: "))
for i in range (1,N+1):
    X=X*1.007
print(f"Số tiền người đó nhận được: {X:.0f}")    
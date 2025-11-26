n=abs(int(input()))
m=n
k=0
while n>1:
    k+=1
    n=n/2

if n==1:
    print(f"Số {m} có dạng 2^{k}")
elif n!=int(n):
    print("Không có dạng 2^k")    
    
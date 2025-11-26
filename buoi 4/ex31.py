n=input()
tong=0
for i in n:
    if "0"<=i<="9":
        i=int(i)
        tong+=i
print(tong)
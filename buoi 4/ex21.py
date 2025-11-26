n=int(input())
tong=0
while n>0:
    a=n%10
    n=n//10
    tong+=a
print(tong)
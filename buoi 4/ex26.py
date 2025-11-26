A=int(input())
a=1
b=1
while (a+b)<=A:
    c=b
    b=a+b
    a=c
print(b)
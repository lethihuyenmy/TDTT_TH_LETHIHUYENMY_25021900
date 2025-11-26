
a,b= map(int,input().split())
A=0
B=0
for i in range(1,a):
    c=0
    if a%i==0:
        c=1
    if c==1:
        A=A+i
for j in range(1,b):
    d=0
    if b%j==0:
        d=1
    if d==1:
        B=B+j
print(A, B)    
if A==b and B==a:
    print("True") 
else:
    print("False")       
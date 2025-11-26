def k_tr(n):
    k=1
    while n!=1:
        if n%2==0:
            n/=2
        else:
            n=3*n+1 
        k+= 1   
    return k       
n=int(input())
c=0
d=0
for i in range(1,n):
    if c<k_tr(i):
        c=k_tr(i)
        d=i
print(d,c, end="")       
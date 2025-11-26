def k_tr(n):
    if n%2==0:
        n=n/2
    else:
        n=3*n+1 

k=int(input())
d=k_tr(k)
print(d, end="")
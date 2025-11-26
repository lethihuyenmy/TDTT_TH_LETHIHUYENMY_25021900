def kiem_tra(n):
    if n<0: n=abs(n)
    m=str(n)
    chusodocnhat=set(m)
    if len(set(m))!=len(m):
        return False
    return True

n=abs(int(input()))
for i in range(1,n+1):
    k=i**2
    ds=[i**2 for i in range(1,n+1)]
dss=[k for k in ds if not kiem_tra(k)]
print(dss)
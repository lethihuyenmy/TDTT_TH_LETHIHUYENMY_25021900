m, n=map(int,input().split())
ds_1=[i for i in range(1, m+1) if m%i ==0]
ds_2=[i for i in range(1, n+1) if n%i ==0]
ds_3=[]
for item in ds_1:
    if item in ds_2:
        ds_3.append(item)
print(max(ds_3))        
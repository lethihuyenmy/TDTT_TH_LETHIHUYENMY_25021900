a, b=map(int,input().split())
ds_1=[i for i in range(1, a+1) if a%i ==0]
ds_2=[i for i in range(1, b+1) if b%i ==0]
ds_3=[]
for item in ds_1:
    if item in ds_2:
        ds_3.append(item)
print(ds_3)        
a,b=map(int,input().split())
tong=0
for i in range(a,b+1):
    c=0
    for j in range(2,i):
        if i % j == 0:  
            c=1
            break
        else:
            c=2
    if c==2:
       tong=tong+i
if a<= 2 :
    tong+=2       
print(tong)          
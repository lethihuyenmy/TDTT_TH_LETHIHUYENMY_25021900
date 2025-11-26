
n=int(input())
for i in range(2,n+1):
    if n%i == 0:
        c=0
        for j in range(2,i):
            if i%j==0:
                c=1
                break
            else:
                c=2           
        if c==2:
            max=i
print(max)            
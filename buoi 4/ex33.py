n=int(input())
m=str(n)
index=len(n)-3
while index >0:
    n=n[:index]+"."+n[index:]
    index-=3
print(n)    
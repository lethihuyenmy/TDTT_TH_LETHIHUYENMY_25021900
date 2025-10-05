a,b,c=map(int,input().split())
if a < (b+c) and b < (a+c) and c < (a+b):
    print("Yes")
else:
    print("No")    
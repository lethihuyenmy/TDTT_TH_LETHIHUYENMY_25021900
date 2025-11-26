
a,b=map(int,input().split())
#số gà là c, số chó là d
#a=c+d
#b=2c+4d
d=(b-2*a)/2
c=(4*a-b)/2
if c==abs(int(c)) and d==abs(int(d)):
    print(f"Số gà là {c:.0f} và số chó là {d:.0f}")
else:
    print("invalid")
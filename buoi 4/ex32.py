n=input()
c=0
e=0
d=0
g=0

for i in n:
    if "A"<=i<="Z" :
        c=1
    elif "a"<=i<="z":
        d=1
    elif "0"<=i<="9":
        e=1
    else:
        g=1  
if c==d==e==g==1 and len(n)>6:
    print("Mạnh")  
else:
    print("Yếu")    
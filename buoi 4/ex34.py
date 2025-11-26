a=input()
b=input()
kq=""     
i=0
while i<len(a):
    if a[i:i+len(b)]==b:
        i+=len(b)
    else:
        kq+=a[i]    
        i+=1
print(kq)        
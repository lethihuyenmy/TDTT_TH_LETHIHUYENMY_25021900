n=abs(int(input()))
k=0
q=0
while n>0:
    a=n%10
    if a%2==0: k+=1
    else: q+=1
    n=n//10
print(f"Số chẵn có {k} chữ số, số lẻ có {q} chữ số")    
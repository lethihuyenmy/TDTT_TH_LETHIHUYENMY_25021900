n=input()
k=0
q=0
p=0
for i in n:
    if "A"<=i<="Z": k+=1
    if "a"<=i<="z": q+=1
    if "0"<=i<="9": p+=1
print(f"Có {k} chữ hoa, có {q} chữ thường, có {p} chữ số") 
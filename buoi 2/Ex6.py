a,b,c=list(map(int,input().split()))
p=(a+b+c)/2
if a < (b+c) and b < (a+c) and c < (b+a):
    import math
    S= math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f"Diện tích của tam giác là: {S:.1f}")
else:
    print("Không phải ba cạnh của tam giác.")         
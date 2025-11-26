def rev(n):
    x = 0
    while (n > 0):
        x = x * 10 + n % 10
        n //= 10
    return x
n = abs(int(input()))
c = 0
rn = rev(n)
while (n != rn):
    c += 1
    n += rn
    rn = rev(n)
print(c, n)
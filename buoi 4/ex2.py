n=-1
while (n <= 0) :
  n = int(input())
for i in range(2,n) :
  if n % i == 0 :
    print("False")
    break
  else:
    print("True")
    break

  #cách 2
def check_snt(a):
  if(a==0 or a==1): return False
  for i in range(2,int(a**(1/2))+1,1):
    if(a%i ==0): return False
  return True
n=-1
while (n<=0):
  n =int(input())
if(check_snt(n)): print ("True")
else: print("False")
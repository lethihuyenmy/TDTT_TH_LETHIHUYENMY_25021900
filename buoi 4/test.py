n=int(input())
if(n%2):
  print(0)
  exit()
m=n
num=[]
i=2
while(n>=i):
  if(n%i==0):
    cnt=0
    while(n%i==0):
     cnt=cnt+1
     n=int(n/i)
    num.append([i,cnt])
  i=i+1
mul1=1
for i in num:
  mul1=mul1*(i[1]+1)
print (int(mul1-mul1/(num[0][1]+1)))
s=[]
while len(s)==0 or s[-1]!=-1:
    s.append(map(int,input().split()))
print(max(s[:-1]),min(s[:-1]))    
m
c = list(map(int,input().split()))
for i in range(1,len(c)):
    if c[i]==42:
        print("I've found the meaning of the life!")
    elif 42 not in c:
        print("It's a joke!")
        break
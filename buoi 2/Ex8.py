A=input("Nhập tên chủ hộ: ")
a=int(input("Nhập số điện tháng trước: "))
b=int(input("Nhập số điện tháng này: "))
x=b-a
bac_1=50*1984
bac_2=bac_1+ 50*2050
bac_3=bac_2+100*2380
bac_4=bac_3+100*2998
bac_5=bac_4+100*3350
if x<=50:
    s=x*1984
elif 51<=x and x<=100:
    s= bac_1 + (x-50)*2050
elif 101<=x and x<=200:
    s= bac_2 + (x-100)*2380
elif 201<=x and x<=300:
    s= bac_3 + (x-200)*2998
elif 301<=x and x<=400:
    s=bac_4 + (x-400)  
elif 401<=x:
    s=bac_5 + (x-400)*3460        
print(F"Họ và tên: {A}")
print(F"Số tiền phải trả: {s*1.08:.0F} ")
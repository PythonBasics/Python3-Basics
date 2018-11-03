from random import randint
x2=0
x3=0
x4=0
x5=0
x6=0
x7=0
x8=0
x9=0
x10=0
x11=0
x12=0

for x in range(0,1000000):
    a=randint(1,6)
    b=randint(1,6)
    if a+b==2:
        x2=x2+1
    if a+b==3:
        x3=x3+1
    if a+b==4:
        x4=x4+1
    if a+b==5:
        x5=x5+1
    if a+b==6:
        x6=x6+1
    if a+b==7:
        x7=x7+1
    if a+b==8:
        x8=x8+1
    if a+b==9:
        x9=x9+1
    if a+b==10:
        x10=x10+1
    if a+b==11:
        x11=x11+1
    if a+b==12:
        x12=x12+1
print(x2)
print(x3)
print(x4)
print(x5)
print(x6)
print(x7)
print(x8)
print(x9)
print(x10)
print(x11)
print(x12)
tulos=[x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12]
print(tulos)
#for x in range(0,11):
#    print(tulos[x] *"x")

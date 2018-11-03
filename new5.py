from random import randint
loppusumma=105
summa=0
ostokpl=13
tavara1arvo=3
tavara2arvo=6
tavara3arvo=12
random1=0
random2=0
random3=0
x=0
y=0
z=0
janne=0
pasi=0

for x in range(0,1000000):
    x=randint(0,13)
    y=randint(0,13)
    if x+y>13:
        continue
    z=13-x-y
    if (x+y+z)==13 and (12*x+6*y+3*z)==105:
        janne=janne+1
print("janne"+ str(janne))



for jisjfisj in range(0,1000000):
    random3=randint(0,ostokpl)
    summa=random3*tavara3arvo
    ostokpl=ostokpl-random3
    random2=randint(0,ostokpl)
    summa=summa+random2*tavara2arvo
    ostokpl=ostokpl-random2
    random1=randint(0,ostokpl)
    summa=summa+random1*tavara1arvo
    if summa == 105 and (random1+random2+random3)==13:
        print (random1,random2,random3)
        pasi=pasi+1
        summa=0
        ostokpl=13
print("pasi"+ str(pasi))



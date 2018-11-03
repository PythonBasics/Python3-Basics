from random import randint
#print(randint(1,10))
a=randint(1,10)
b=randint(1,10)
#b=int(input("anna b arvo: "))

if a==b:
    print("a arvo on "+str(a)+" b arvo on "+str(b)+" molemmat ovat yhtä isoja. Yhteensä ne ovat "+str(a+b))
if a<b:
    print("a arvo on "+str(a)+" b arvo on "+str(b)+" B oli isompi. Yhteensä ne ovat "+str(a+b))
if a>b:
    print("a arvo on "+str(a)+" b arvo on "+str(b)+" A oli isompi. Yhteensä ne ovat "+str(a+b))

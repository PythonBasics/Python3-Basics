#guess a number

from random import randint

randomnumero = randint(0,20)


while True:
    arvaus=int(input("Arvaa numero 0 ja 20 välillä"))
    if arvaus < randomnumero:
        print("Oikea numero on suurempi")
        continue
    elif arvaus > randomnumero:
        print("Oikea numero on pienempi")
        continue
    else:
        print("arvasit oikein")
        break


salasana = "apina"
salasanaarvaus = ""
arvausmaara = 0
maxarvausmaara = 3
tililukittu = False

while salasanaarvaus != salasana:
    if tililukittu == True:
        print("Pääsy estetty")
        break
    salasanaarvaus = input("Anna salasana: ")
    arvausmaara += 1
    if arvausmaara == 3:
        tililukittu = True
    if salasanaarvaus == salasana:
        print("Pääsir sisään")
        break

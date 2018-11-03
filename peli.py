#Tämä on harjoitus projekti
from random import randint


def hahmonluonti():         #tällä luodaan uusi pelaaja
    nimi = ""
    sukupuoli = ""

    def resetoi():          #tämä palaa hahmon luonissa alkuun jos pelaaja vastaa kysymyksiin jotain muuta kuin k
        if input("k/e?") != "k":
            hahmonluonti()

    nimi = input("Anna hahmon nimi")                            #hahmolle nimi
    print("Hahmon nimi on " + nimi + " onko se oikein? k/e?")
    resetoi() #tämä palaa hahmon luonissa alkuun jos pelaaja vastaa kysymyksiin jotain muuta kuin k

    while sukupuoli.lower() not in ("mies", "nainen"):      #hahmolle sukupuoli
        sukupuoli = input("Anna hahmon sukupuoli. Mies on yleensä voimakkampi. Nainen taa on yleensä ketterämpi ja älykkämpi")
        print("Virheellinen sukupuoli! Voit olla vain mies tai nainen")
    print("Hahmon sukupuoli on " + sukupuoli + " onko se oikein? k/e?")
    resetoi() #tämä palaa hahmon luonissa alkuun jos pelaaja vastaa kysymyksiin jotain muuta kuin k
    def arvostats(): #Arpoo hahmolle kaikki statsit
        stre = 0 #melee damage, resist melee damage, max carry weight
        dex = 0 #crit % melee and range, hit % melee and range
        con = 0 #max HP, max carry weight
        inte = 0 #max mana, resist magic
        luck = 0 #all random change +%
        stre = randint(25,100)
        dex = randint(25,100)
        con = randint(25,100)
        inte = randint(25,100)
        luck = randint(25,100)
        if sukupuoli == "mies":
            stre = stre + 8
            con = con + 6
        if sukupuoli == "nainen":
            dex = dex + 7
            inte = inte + 7
        print("Hahmosi saa seuraavat stats")
        print("Voima on " + str(stre))
        print("Ketteryys on " + str(dex))
        print("Ruuminrakenne on " + str(con))
        print("Älykkyys on " + str(inte))
        print("Onni on " + str(luck))
        print("Haluatko arpoa uudeestaan? k/e?")
        if input("k/e?") == "k":
            arvostats()
    arvostats()

hahmonluonti()

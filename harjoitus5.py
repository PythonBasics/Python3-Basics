from random import randint
charset = "qwertyuiopasdfghjkl"
salasana = "kek"

if input("Anna salasana") == salasana:
    print("Salasana oli oikein!")
else:
    print("Väärä salasana! ")
    if input("haluatko hakkeroida brute forcella? k/e?") == "k":
        while True:
            arvaus = charset[randint(0,len(charset)-1)]+charset[randint(0,len(charset)-1)]+charset[randint(0,len(charset)-1)]
            print(arvaus)
            if arvaus == salasana:
                print("Sait hakkeroitua salasanan se oli kek")
    else:
        print("Haista sit paska")

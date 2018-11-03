from random import randint

numerot = [1, 3, 12, 20, 33, 2, 7]
nimet = ["Pekka", "Janne", "Ville", "Tiina"]
nimet.append("Spede")
nimet.insert(2, "Lauri")
##nimijokapoistuu = randint(0, len(nimet) - 1)
##print(nimijokapoistuu)
print(nimet)
pois = nimet[randint(0, len(nimet) - 1)]
nimet.remove(pois)

print(nimet)

print(sorted(numerot, key=int, reverse=True))
print(numerot)


#Tuple ei voi muuttaa
coordinates = (4,5)
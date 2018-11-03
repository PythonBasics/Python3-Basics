pituus = 0
summa = 0
keskiarvo = 0
nimikpl = 0
lista = []
nimet = [line.rstrip("\n") for line in open("nimet.txt")]
for i in range(len(nimet)):
    nimi=nimet[i].lower()
    pituus = (len(nimi))
    lista.append(len(nimi)) 
    summa = summa+pituus
    nimikpl = nimikpl+1
print("Kirjaimien keskiarvo on " + str(float(summa)/float(nimikpl)))
print("Lyhin nimi sisälsi " + str(min(lista)) + " kirjainta.")
print("Pisin nimi sisälsi " + str(max(lista)) + " kirjainta.")

  

nimet = [line.rstrip("\n") for line in open("nimet.txt")]
for i in range(len(nimet)):
    nimi=nimet[i].lower()
    if nimi[0] == nimi[-1]:
        print(nimi)

##nimet = []
##nimet = file.readlines()
##
##for nimi in nimet:
##    if nimi[0].lower == nimi[-1].lower:
##        print (nimi)
##
##
##nimi = "anna"
##if nimi[0] == nimi[-1]:
##    print("sama kirjain alussa ja lopussa " + nimi[0])
##else:
##    print("Eri kirjain kirjain alussa ja lopussa")


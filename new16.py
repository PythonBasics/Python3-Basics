nimet = [line.rstrip("\n") for line in open("nimet.txt")]
#nimi=[]
#for i in range(len(nimet)):
#    nimi.append(nimet[i])
f= open("lajiteltu.txt","w")
nimet.sort()
for i in range(len(nimet)):
    f.write("%s\n" % nimet[i])
f.close()

##
##f= open("lajiteltu.txt","w+")
##for nimi in range(len(nimet)):
##    nimi.append(nimet[i])
##nimi.sort()
##f.write("%s\n" % nimi2)
##f.close()
##    

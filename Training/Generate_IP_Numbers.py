from random import randint

iplist= open("iplist.txt","w+")
ip = []
for i in range(0,10000):
    ip.append("10.10." + str(randint(0,255)) + "." + str(randint(0,255)))
for i in range(0,len(ip)):
    iplist.write(str(ip[i]+"\n"))
iplist.close()
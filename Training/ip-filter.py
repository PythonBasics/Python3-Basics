from collections import Counter

# lista ip-osoitteita
# log
# >= 5 kertaa
# banned clients

# 192.168.0.1
# 192.168.0.1
# 127.0.0.1

print("\n*** Beginning Banned Log - Project ***\n")

# iplist = open("iplist.txt", "r")
iplist = [line.rstrip("\n") for line in open("iplist.txt")]
print(iplist)

log = iplist

#ip = []
#for i in range(0,10000):
#    ip.append("10.10." + str(randint(0,255)) + "." + str(randint(0,255)))
#for i in range(0,len(ip)):
#    iplist.write(str(ip[i]+"\n"))
#iplist.close()



#log = [
#    "192.168.0.1",
#    "192.168.0.1",
#    "127.0.0.1"
#]

# jos yli 4 kertaa sama osoite
banned_log = [
    "1.1.1.1",
    "2.2.2.2"
]

cnt = Counter()
for address in log:
    cnt[address] += 1
    if cnt[address] >= 3:
        print("Address " + address + " contained in log file " + str(cnt[address]) + " times.");
        banned_log.append(address);

print(cnt)
print(cnt['192.168.0.1'])
print(cnt['127.0.0.1'])
print(cnt['localhost'])

print("banned log" + str(banned_log));

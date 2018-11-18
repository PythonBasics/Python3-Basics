from collections import Counter

print("\n*** Project: Banned IP-Address Logging ***\n")

log = []         # IP-addresses
banned_log = []  # banned IP-addresses

FILE = "iplist.txt"  # read ip-addresses from FILE
FILE = "C:\Python-files\GitHub\Training\~iplist.txt"

MIN_NUMBER_OF_MATCHES = 3
MANUALLY_BANNED_IP_ADDRESSES = \
    [ 
        "127.0.0.1",
        "2.2.2.2",
        "1.2.3.4"
    ]
    
# log = [line.rstrip("\n") for line in open(FILE)]

banned_log = MANUALLY_BANNED_IP_ADDRESSES
log = banned_log

cnt = Counter()
for ip_address in log:
    cnt[ip_address] += 1
    if cnt[ip_address] >= MIN_NUMBER_OF_MATCHES:
        print("Address " + ip_address + " contained in log file " + str(cnt[ip_address]) + " times.")
        banned_log.append(ip_address)

print("banned log: " + str(banned_log))


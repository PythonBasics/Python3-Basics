from collections import Counter

print("\n*** Beginning Banned IP-Address Log - Project ***\n")

# log --> ip-addresses
# banned_log --> banned addresses

FILE = "iplist.txt"  # read ip-addresses from FILE
MIN_NUMBER_OF_MATCHES = 3
MANUALLY_BANNED_IP_ADDRESSES = \
    [
        "127.0.0.1",
        "2.2.2.2",
        "1.2.3.4"
    ]

log = [line.rstrip("\n") for line in open(FILE)]

banned_log = MANUALLY_BANNED_IP_ADDRESSES

cnt = Counter()
for address in log:
    cnt[address] += 1
    if cnt[address] >= MIN_NUMBER_OF_MATCHES:  # edit the number
        print("Address " + address + " contained in log file " + str(cnt[address]) + " times.")
        banned_log.append(address)

print("banned log: " + str(banned_log))
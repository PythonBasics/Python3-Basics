from collections import Counter

# "log" --> all ip-addresses
# "banned_log" --> all banned addresses

# examples of ip-addresses:
# 192.168.0.1
# 192.168.0.1
# 127.0.0.1

print("\n*** Beginning Banned Log - Project ***\n")

# read ip-addresses from .txt file
file = "iplist.txt"
log = [line.rstrip("\n") for line in open("iplist.txt")]

banned_log = [
    # manually banned ip-addresses
    "127.0.0.1",
    "2.2.2.2"
]

cnt = Counter()
for address in log:
    cnt[address] += 1
    if cnt[address] >= 3:
        print("Address " + address + " contained in log file " + str(cnt[address]) + " times.")
        banned_log.append(address)

print("banned log" + str(banned_log))
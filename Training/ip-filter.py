from collections import Counter

# "log" --> all ip-addresses
# "banned_log" --> all banned addresses

# 192.168.0.1
# 192.168.0.1
# 127.0.0.1

print("\n*** Beginning Banned Log - Project ***\n")

ip_list = [line.rstrip("\n") for line in open("iplist.txt")]

log = ip_list

banned_log = [
    "1.1.1.1",
    "2.2.2.2"
]

cnt = Counter()
for address in log:
    cnt[address] += 1
    if cnt[address] >= 3:
        print("Address " + address + " contained in log file " + str(cnt[address]) + " times.")
        banned_log.append(address)

print("banned log" + str(banned_log))

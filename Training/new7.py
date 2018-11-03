


n = 999999999999999999999999
p = 2
for p in range(9999, n+1):
    for i in range(2, p):
        if p % i == 0:
            break
    else:
        print (p),

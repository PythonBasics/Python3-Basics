crypto = {
    "ada": "Cardano",
    "neo": "NEO",
    "btc": "Bitcoin",
    "eth": "Ethereum",
}

print(crypto.get(input("Anna ticker"), "Ticker ei löydy"))


i = 1
while i <= 10:
    print(i)
    i = i + 1
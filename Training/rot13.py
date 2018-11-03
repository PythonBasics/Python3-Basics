inp="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
output="NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"

text=input("Syötä teksti")

for x in range(0, len(text)):
    rot13 = inp.find(text[x])
    if rot13 == -1:
        print(text[x], end="")
    else:
        print(output[rot13], end="")
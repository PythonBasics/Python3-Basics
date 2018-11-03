from random import randint

charset = "1234567890+´qwertyuiopåäsdfghjklöä'zxcvbnm,.-!\"#¤%&/()=?`QWERTYUIOPÅÂSDFGHJKLÖÄ*ZXCVBNM;:_"

for x in range(0,randint(1, 100)):
    for y in range(0,randint(1, 100)):
        random = randint(0,len(charset)-1)
        print(charset[random], end="")
    print()
##print("hw")
##
### lotto, alkuluvut: 3, 5, 7, 11, 13,
##
### print(3 % 0)
##print(0 % 2) # 0
##print(1 % 2) # 1
##print(2 % 2) # 0
##print(3 % 2) # 1
##print(4 % 2) # 0
##
##print("tulos")
##print(12 % 5)
##
##t1 = []
##
##for x in range(3, 20):
##
##    alkuluku = False
##
##    for y in range(3, x):
##
##        alkuluku = True
##
##        # print(x, y)
##
##        if (x % y) == 0:
##            # print(str(x) + " ei alkuluku")
##            alkuluku = False
##            break
##
##
##    if alkuluku and x > 4:
##        t1 = t1 + [str(x)]
##
##print("Alkuluvut ovat: " + str(t1))
##
##t = []

##
##for i in range(1, 101):
##    if (i % 3 == 0) and (i % 5 == 0):
##        t = t + ["fizz puzz"]
##    elif (i % 3) == 0:
##        t = t + ["fizz"];
##    elif (i % 5 == 0):
##        t = t + ["puzz"]
##    else:
##        t = t + [str(i)]
##
##print(t)
##
##for i in t:
##    print(i)
##
##print("*** Shell ***")
##
### import subprocess
### subprocess.Popen("notepad.exe",shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
##
##print("*** Client-Server ***")

# koko suorakulmio täytetään

##leveys = int(input("leveys: "))
##korkeus = int(input("korkeus: "))

def laatikko(leveys, korkeus):

    for i in range(0, korkeus):

        for j in range(0, leveys):

            print("*", end=" ")

        print()

# koko suorakulmiota ei täytetä

##def laatikko_tyhja(leveys, korkeus):
##
##    # eka rivi
##    for i in range(0, leveys):
##        print("*", end="")
##
##    print()
##
##    for j in range(1, korkeus-1):
##
##        print("*", end=(leveys - 2) * " ")
##        print("*")
##
##    for i in range(0, leveys):
##        print("*", end="")
##
##def reverse():
##
##    s = "Hello World"
##    t = s.split(" ")
##    print(t[1] + " " + t[0])
##
##    s = "yy kaa koo"
##    l = s.split()
##    l2 = []
##    for i in reversed(l):
##        l2.append(i)
##    print(" ".join(l2))
##
##reverse()

# noppa, keskiarvo, mediaani, moodi

##from random import randint
##
##t = []
##
##for i in range(0, 6):
##
##    r = randint(1, 6)
##    t.append(r)
##
##t.sort()
##print(t)

### lue teksti, xxx ###

##from collections import Counter
##
##t = ['a', 'b', 'c', 'c', 'c', 'abba', 'abba']
##
##cnt = Counter()
##for word in t:
##    cnt[word] += 1
##
##print(cnt)
##print(cnt['a'])
##print(cnt['b'])
##print(cnt['c'])
##
##print()
##
##for chr in cnt:
##    print(chr + ": " + str(cnt[chr]))
##
##print()
##
##print(cnt.most_common())


# lue nimet -->
# lastennimi.com

#lines = [line.rstrip('\n') for line in open("nimet.txt")]

##for i in range(len(lines)):
##
##    nimi = lines[i].lower()
##
##    if nimi[0] == nimi[-1]:
##        print(nimi)
##
##print(lines)

# nimien pituus?
# lyhin, pisin, keskiarvo

##def pituus_keskiarvo(lines):
##    pituus = 0.0
##    for i in range(len(lines)):
##        nimi = lines[i]
##        print(nimi)
##        print(len(nimi))
##        pituus = pituus + len(nimi)
##
##    return pituus / i
##
##p = 999.9
##lines = [line.rstrip('\n') for line in open("nimet.txt")]
##taulukko = []
##
##def pienin(lines):
##
##    for i in range(len(lines)):
##        taulukko.append(len(lines[i]))
##
##    return min(taulukko)
##
##print(pienin(lines))
##print(pituus_keskiarvo(lines))
##
### avaa/tallenna + lajittele lista
##
##lines = [line.rstrip('\n') for line in open("nimet.txt")]
##
##def aakkosjarjestys(lines):
##
##    lines.sort()
##    print(lines)
##
##    with open('nimet_aakosjarjestyksessa.txt', 'w') as f:
##        for item in lines:
##            f.write("%s\n" % item)

### aakkosjarjestys(lines)
##
##print("\nRandom tähtiä:")
##
### kolina, hajonta
### valvomo peli
##
##from random import randint
##
##rows = 7
##
##for x in range(0, rows):
##
##    r = randint(1, 6) + x
##
##    print(r * "*")
##    
# charset
# rivit, 0-100
# sarakkeet, 0-100 random-merkkiä
##
##from random import randint
##
##charset = "1234567890ABCDEF"
##
##rows = randint(0, 10)
##
##for row in range(0, rows):
##
##    col = randint(0, 10)
##
##    for col in range(0, col):
##
##        r = randint(0, len(charset)-1)
##
##        print(charset[r], end="")
##
##    print()        

# ROT13

import hashlib

inp =    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
output = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"

word = "4398754?!66AAABBA"
# word = input("Syötä ROT13 ")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def ROT13_v1(self, word):

        for i in range(0, len(word)):

            loc = inp.find(word[i])

            if loc == -1:
                print(word[i], end="")
            else:
                print(output[loc], end="")

    def MD5(self, word):    
        return hashlib.md5(word.encode('utf-8')).hexdigest()


    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
p1.ROT13_v1("rot")
p1.ROT13_v1("rot2")

def ROT13_v2(word):
    ROT13_v1(word)  

# ROT13_v2(word)

# custom bitcoin wallet !!! !!! !!!
# generoi n bitcoin lompakkoa

import time

time.sleep(1)

t1 = [1, 2, 4, 1, 2]

for i in range(0, 10): 

    start = time.time()
    end = time.time()
    print (end - start)

from math import *

print(sqrt(4096))

# opettaja & oppilas

friends = ["a", "b", "c"]
# lucky_numbers = [1, 2, 3, 4, 7]

# print(friends[1:2])
# print(lucky_numbers[0:1])
# print(lucky_numbers[0:2])
# print(lucky_numbers[-3])

# friends.extend(lucky_numbers)
# friends.remove("b")

##for i in range(0, 10):
##    
##    from random import randint
##    r = randint(0, len(friends)-1)
##    friends.remove(friends[r])
##    friends.append("a")
##    friends.sort()
##    friends.reverse()
##    print(friends)    


##num = 0
##while True:
##    num += 1
##    print(num, end=", ")
##    time.sleep(0.01)

friends = ["bo", "abe", "cecilia"]
from random import randint
r = randint(0, len(friends)-1)
# friends.remove(friends[r])
friends.append("dan")
friends.sort()
friends.reverse()
print(friends)    

f2 = friends.copy()

coordinates = (1, 2, 4)
coordinates = (42, 4, 1, 33)

print(coordinates)

def cube(number):
    return number * number * number

def reason_of_life():
    return 42

print(cube(3))

from random import randint

inp = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

password = "1234"
right = 0
wrong = 0
million = 1000000

for i in range(0, million): 

    match = []

    for j in range(0, len(password)):

        r = randint(0, len(inp)-1)

        if password[j] == inp[r]:
            match.extend(password[j])
            right += 1
        else:
            wrong += 1
            break

    if len(match) == len(password): 
        print("Match. Password hacked: ", end="")
        print(match)
                
print("Right answers: " + str(right))
print("Wrong answers: " + str(wrong))

print(100 * right/(right + wrong))
print(100 * (1/len(inp)))

# accountant

class Employee():
        
    def __init__(self, str, int):

        self.str = str
        self.int = int
        self.oma_funktio        

    def __f18__(self):
        if self.str == 18:
            print("18-vuotias")

    def __not_f18__(self):
        if self.str != 18:
            print("ei 18-vuotias")

    def oma_funktio():
        print("oma funktio")

sahkomies = Employee(18, 16)
sahkomies.__not_f18__()

### guess a number from 1 to 20
##from random import randint
##
##min_number = 1
##max_number = 20
##
##r = randint(1, 21)
##
##while True:
##    inp = int(input("Guess an number between " + str(min_number) + " and " + str(max_number) + ": "))
##
##    if inp == r:
##        print("oikein")
##        break
##
##    elif r > inp:
##        print("luku on suurempi")
##
##    else:
##        print("luku on pienempi")
##
##
##r = randint(1, 21)
##
##while True:
##    inp = 20
## 
##    if inp == r:


# World

import matplotlib.pyplot as plt # pip install matplotlib AS ADMINISTRATOR!

population_by_continents = {
    "Asia" :         4545133094,
    "Africa" :       1287920518,
    "Europe" :        742648010,
    "South America" : 428240515,
    "North America" : 363844490,
    "Australia" :      24854497
}

print()

c = []
p = []

for continent, population in population_by_continents.items():
    c.append(continent)
    p.append(population)
    print(continent, population)

world_population = 0
for continent, population in population_by_continents.items():    
    world_population += population

print("World population is: ", world_population)

# plt.plot(c, p)
plt.bar(c, p, label="Population", color="blue")

plt.xlabel("Continents")
plt.ylabel("Population")
plt.title("Population by continents")

#plt.show()

# plt.plot([1,2,3], [2, 4, 9])
# plt.plot([3,2,1], [7, 7, 9])

##population_ages = [22, 33, 44, 3, 2, 100]
##ids = [x for x in range(len(population_ages))]
##print(ids)
##plt.bar(ids, population_ages)
###plt.show()
##
##bins = [0, 10, 20, 30, 50]
##plt.hist(population_ages, bins, histtype="bar", rwidth=0.8)
### plt.show()
##
##### Union
##print("Union")
##x = [{1, 2, 3}, {2, 3, 4}, {3, 4, 42}]
##print(set.union(*x))
##print(set.intersection(*x))

####

num_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(num_grid[1][0])

for row in range(len(num_grid)):
    # print(row)

    for column in range(len(num_grid[row])):

        print(num_grid[row][column])

        
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation += "g"
        else:
            translation += letter

    return translation

print(translate("aeixxx"))

# Ethereum-address
# 0x
# 0-9-a-f
# 42 character
# .lower()

print("\nChecking Ethereum address...")
alphabet = "0x1234567890abcdef"
address =  "0x1234567890abcdefaa0x1234567890abcdefaa42"
address = address.lower()
print("Alphabet is:\t" + alphabet)
print("Address  is:\t" + address)

if address[0:2] != "0x":
    print("Error: Not 0x in beginning.")         

if len(address) != 42:
    print("Error: False length.")

def check_address(address, alphabet): 

    for a in address:
        
        if alphabet.find(a) == -1:
            return False
            
    return True
            
if check_address(address, alphabet) == True:
    print("Address  is:\tOk.")
else:
    print("Error: Address is invalid.")

print("")

# lista ip-osoitteita
# log
# >= 5 kertaa
# banned clients

# 192.168.0.1
# 192.168.0.1
# 127.0.0.1

print("")

log = [
    "192.168.0.1",
    "192.168.0.1",
    "127.0.0.1"
]

# jos yli 4 kertaa sama osoite
banned-log = [
    
]

from collections import Counter

t = ['a', 'b', 'c', 'c', 'c', 'abba', 'abba']

cnt = Counter()
for word in log:
    cnt[word] += 1
    if cnt[word] >= 2:
        print("Osoite " + word + " esiintyy yli " + cnt[word] + " kertaa log tiedostossa")        


print(cnt)
print(cnt['a'])
print(cnt['b'])
print(cnt['c'])

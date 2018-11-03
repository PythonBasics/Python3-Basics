##a=int(input("anna leveys: "))
##b=int(input("anna korkeus: "))
##for korkeus in range(0,b):
##    for leveys in range(0,a):
##        print(end="*")
##    print()

a=int(input("anna leveys: "))
b=int(input("anna korkeus: "))
reuna=a-1
for leveys in range(0,a):
    print(end="*")
print()

for korkeus in range(2,b):
    for leveys in range(0,1):
        print(end="*")
        for leveys in range(1,reuna):
            print(end=" ")
        print(end="*")
    print()
        
for leveys in range(0,a):
        print(end="*")

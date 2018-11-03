from random import randint

lista="QWERTYUIOPÅASDFGHJKLÖÄZXCVBNMqwertyuiopåasdfghjklöäzxcvbnm0987654321"




##for i in range(0,50):
##    for x in range(0,50):
##        randomkirjain=randint(1,58)
##        if luku == 1:
##            print(lista[randomkirjain],end="")
##        elif luku != 1:
##            print("*",end="")  
##    print()




for i in range(0,50):
    for x in range(0,50):
        randomkirjain=randint(0,(len(lista)-1))
        print(lista[randomkirjain],end="")   
    print()


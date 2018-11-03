##from random import randint
##t=[]
##for x in range(0,20):
##    t.append(randint(1,6))
##
##print(t)
##t.sort()
##print(t)
from collections import Counter
a=[]
a=(input("anna lista: "))
#print(a)
a=a.lower()
a=a.split()
a.sort()
#print(a)

print(Counter(a))


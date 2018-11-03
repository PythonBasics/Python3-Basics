import time
x = 0.0
start = time.time()
for x in range(3,10000000):

    if x%2 == 0:
        continue
    end = time.time()
    aika=end-start
    print("Alkuluku" +str(x) +"aikaa meni" +str(aika))



    
    

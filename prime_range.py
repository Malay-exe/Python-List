#To find the prime nu bers in the given range
def pri():
    for i in range(2,15):
        x=[]
        for j in range(2,i):
            if i%j==0:
                break
                
        else:    
                x.append(i)
                print(i, end =' ')
(pri())       
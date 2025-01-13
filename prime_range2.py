def prim(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def sted(s,e):
    
    for i in range(s,e+1):
        if prim(i):
            print(i,end =' ')
prim(6)
sted(2,15)   

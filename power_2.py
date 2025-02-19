#check whether the n is power of 2 or not
def pow(n):
    if n==0:
         return True
    for i in range(n):
         x=2**i
         if x==n:
              return True
    return False
print(pow(4))

  

#multiply all the elements
def mul(lst):
    x=1
    for i in range(len(lst)):
        x*=lst[i]
    return x 
lst=[1,2,3,4,5]
print(mul(lst))   
#another method
import math
a=math.prod(lst)
print(a)
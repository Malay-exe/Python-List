#interchange the first and the last elements of the list
def inter(lst):
    x=lst[0],lst[-1]=lst[-1],lst[0]
    return x
lst=[1,2,3,4,5]
print(inter(lst))
#another
list=[1,2,3,4,5,35,63,7]
list[0],list[-1]=list[-1],list[0]
print(list)
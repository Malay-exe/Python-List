# for list
def l(lst):
    x=[]
    for i in lst:
        x.insert(0,i)
    return x
print(l([1,2,3,4,5]))
#print all the duplicate from the list
def duolicate(lst):
    a=[]
    s=set()
    for i in lst:
        if i in s:
            a.append(i)
        else:
            s.add(i)
    return a
lst=[1,1,2,2,3,4,4,5,6,6,7,8,9,9]
print(duolicate(lst))            
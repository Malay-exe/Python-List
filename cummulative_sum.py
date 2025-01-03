def csum(lst):
    a=0
    list=[]
    for i in range(0,len(lst)):
        a+=lst[i]
        list.append(a)
    print(list)
lst=[1,2,3,4,5]
csum(lst)  
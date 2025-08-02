def missing(lst):
    lst.sort()
    for i in range(len(lst)-1):
        if lst[i + 1] != lst[i] + 1:
            x=lst[i]+1
            return x
    # if lst[-1] != lst[i]+1:
    #     return lst[i]+1
lst=[4,5,7]
print(missing(lst))
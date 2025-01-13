def sm(lst):
    x=str(lst)
    y=0
    for i in range(0,len(x)-1):
        y=y+int(i)
    return y
print(sm([123]))
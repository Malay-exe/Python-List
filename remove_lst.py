#remove empty list
a = [[1, 2], [], [3, 4], [], [5]]
b=[]
for i in a:
    if i:
        b.append(i)
print(b)        
#same for the tuple
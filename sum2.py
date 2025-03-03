#print the sum of the elements of the list
def su(l):
    for i in l:
        i+=i
    return i
print(su([1,2,3,4]))
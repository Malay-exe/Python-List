#break the list into chunk of size

def br(lst,n):
    
    for i in range(0,len(lst),n):
        x=i
        print(lst[x:x+n])
list=[1,2,3,4,5,6,7,8,9]
print(br(list,2))
    

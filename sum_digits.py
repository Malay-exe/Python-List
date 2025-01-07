def sumdig(lst):
    x = []
    for i in lst:
        a = 0
        while i > 0:
            a += i % 10  
            i //= 10  
        x.append(a)
    return x

numbers = [123, 456, 789]
print(sumdig(numbers))  
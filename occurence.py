#Count occurrences of an element in a list in Pythoncount = 0
count=0
a = [1, 3, 2, 6, 3, 2, 8, 2,8, 9, 2, 7, 3]
user_value = 2
for i in a:
    if i == user_value:
        count += 1
print(count)
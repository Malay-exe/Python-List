#find eatch number is how many times repeated in list

a = [1, 3, 2, 6, 3, 2, 8, 2, 8, 9, 2, 7, 3]
counts = {}

for i in a:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1
        
for i in counts:
    print(f"{i}: {counts[i]}")
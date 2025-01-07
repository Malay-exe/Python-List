lst=[1,2,3,4,5]
x=lst[2]
lst[2]=lst[4]
lst[4]=x
print(lst)
# print(len(lst))
#two variables
a=2
b=3
a^=b
b^=a
a^=b
print(a)
print(b)
#another method
a=a+b
b=a-b
a=a-b
print(a)
print(b)
#another method
a,b=b,a
print(a)
print(b)
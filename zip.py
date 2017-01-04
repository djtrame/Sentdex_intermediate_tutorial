#zip joins lists together
x = [1, 2, 3, 4]
y = [7, 6, 2, 1]
z = ['a', 'b', 'c', 'd']

for a,b,c in zip(x,y,z):
    print(a,b)

print('-------')

print(zip(x,y,z))
print('-------')

for i in zip(x,y,z):
    print(i)

print('-------')
[print(a,b) for a,b in zip(x,y)]

print('-------')
#this overwrites the a,b values
#don't use the same variable names as the for loop
for a,b in zip(x,y):
    print(a,b)

print(a)
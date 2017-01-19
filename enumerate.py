example = ['left', 'right', 'up', 'down']

for i in range(len(example)):
    print(i, example[i])

print('-------')
for i, j in enumerate(example):
    print(i,j)


print('-------')
print('dictionary:')
new_dict = dict(enumerate(example))

print(new_dict)

print('-------')
[print(i, j) for i, j in enumerate(new_dict)]
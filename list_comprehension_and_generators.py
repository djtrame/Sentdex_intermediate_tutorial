#lists are faster because they use RAM to store the list, but could run out of memory
#generators are slower because they stream the values but do not use memory

#xyz and abc have the same output and are both lists
xyz = [i for i in range(5)]
print(xyz)

abc = []
for i in range(5):
    abc.append(i)

print(abc)

#generator expression - not in memory
#notice the paranthesis instead of the brackets
uvw = (i for i in range(5))

#this print shows that uvw is a generator object
print(uvw)

for i in uvw:
    print(i)

print('What is divisible by 5?')

input_list = [5,6,2,10,15,20,5,2,1,3]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

#generator
xyz = (i for i in input_list if div_by_five(i))

#list
# abc = []
# for i in input_list:
#     if div_by_five(i):
#         abc.append(i)

for i in xyz:
    print(i)

print('This prints nothing in Python 3.4')
[print(i) for i in xyz]

print('------')
#list comprehension
abc = [i for i in input_list if div_by_five(i)]
print(abc)

print('------')
[[print(i, ii) for ii in range(5)] for i in range(5)]


print('------')
#same as above
for i in range(5):
    for ii in range(5):
        print(i, ii)

#this makes a list of tuples
xyz = [[(i, ii) for ii in range(5)] for i in range(5)]
print(xyz)

print('------')

#build our own generator - part 9
def simple_gen():
    yield 'Oh'
    yield 'Hello'
    yield 'there'

for i in simple_gen():
    print(i)

print('-------')

correct_combo = (3, 1, 4)
found_combo = False

for c1 in range(10):
    if found_combo:
        break
    for c2 in range(10):
        if found_combo:
            break
        for c3 in range(10):
            if found_combo:
                break
            if (c1, c2, c3) == correct_combo:
                print('Found the combo: {}'.format((c1,c2,c3)))
                found_combo = True
                break
            #print(c1,c2,c3)

print('-------')

#make our own generator and iterate over it
def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)

for (c1, c2, c3) in combo_gen():
    print(c1, c2, c3)
    if (c1, c2, c3) == correct_combo:
        print('Found the combo: {}'.format((c1, c2, c3)))
        break
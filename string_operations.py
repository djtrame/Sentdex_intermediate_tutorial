names = ['Jeff', 'Gary', 'Jill', 'Samantha']

for name in names:
    #print('Hello there, ' + name)
    print(' '.join(['Hello there,', name]))

#print the list of the names as a string
print(', '.join(names))

import os

location_of_files = 'C:\\Code\\Python\\Sentdex_Intermediate_Tutorial'
file_name = 'testfile.txt'

print(location_of_files + '\\' + file_name)

#easy way to join file paths
with open(os.path.join(location_of_files,file_name)) as f:
    print(f.read())

who = 'Gary'
how_many = 12

# Gary bought 12 apples today!

print(who, 'bought', how_many, 'apples today!')

#correct way to do string formatting
#python 2 needs those braces to be indexed 0 and 1
print('{} bought {} apples today!'.format(who, how_many))

